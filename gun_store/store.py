"""
gun_store/store.py
------------------
Business-logic layer for Paseo Guns.
Coordinates inventory, sales, customers, employees, and reporting.
"""

from __future__ import annotations

import uuid
from datetime import datetime, date
from typing import Any, Dict, List, Optional, Tuple

from .database import Database
from .models import (
    Accessory,
    Ammunition,
    CartItem,
    Customer,
    Employee,
    Firearm,
    Modification,
    Product,
    Transaction,
    product_from_dict,
)


TAX_RATE = 0.0825  # 8.25 % — example state/local rate


class Store:
    """
    Centralises all store operations.
    A single Store instance is shared across the entire CLI session.
    """

    NAME = "Paseo Guns"
    ADDRESS = "1500 W Commerce St, San Antonio, TX 78207"
    PHONE = "(210) 555-GUNS"
    HOURS = "Mon–Sat 9 AM – 7 PM  |  Sun 10 AM – 5 PM"
    FFL = "FFL# 5-74-XXX-01-8C-12345"

    def __init__(self, db: Database) -> None:
        self.db = db
        self.current_employee: Optional[Employee] = None
        self.cart: List[CartItem] = []

    # ------------------------------------------------------------------
    # Employee / authentication
    # ------------------------------------------------------------------

    def login(self, emp_id: str, pin: str) -> Tuple[bool, str]:
        """Attempt employee login. Returns (success, message)."""
        emp = self.db.get_employee_by_id(emp_id.upper())
        if emp is None:
            return False, "Employee ID not found."
        if not emp.active:
            return False, "Employee account is inactive."
        if emp.pin != pin:
            return False, "Incorrect PIN."
        self.current_employee = emp
        return True, f"Welcome, {emp.full_name} ({emp.role.capitalize()})!"

    def logout(self) -> None:
        self.current_employee = None
        self.cart = []

    def require_role(self, level: str) -> bool:
        if self.current_employee is None:
            return False
        return self.current_employee.has_permission(level)

    # ------------------------------------------------------------------
    # Inventory — read
    # ------------------------------------------------------------------

    def get_all_products(self) -> List[Product]:
        return self.db.get_products()

    def get_products_by_category(self, category: str) -> List[Product]:
        return [p for p in self.db.get_products() if p.category.lower() == category.lower()]

    def get_firearms(self, firearm_type: Optional[str] = None) -> List[Product]:
        firearms = [p for p in self.db.get_products() if isinstance(p, Firearm)]
        if firearm_type:
            firearms = [p for p in firearms if p.firearm_type.lower() == firearm_type.lower()]  # type: ignore[attr-defined]
        return firearms

    def search_products(self, query: str) -> List[Product]:
        q = query.lower()
        results = []
        for p in self.db.get_products():
            if (
                q in p.name.lower()
                or q in p.brand.lower()
                or q in p.model.lower()
                or q in p.description.lower()
                or q in p.category.lower()
            ):
                results.append(p)
        return results

    def get_low_stock(self) -> List[Product]:
        return [p for p in self.db.get_products() if p.is_low_stock()]

    def get_product_by_id(self, product_id: str) -> Optional[Product]:
        return self.db.get_product_by_id(product_id.upper())

    # ------------------------------------------------------------------
    # Inventory — write (manager+)
    # ------------------------------------------------------------------

    def add_product(self, product: Product) -> Tuple[bool, str]:
        if not self.require_role("manager"):
            return False, "Manager or owner access required."
        existing = self.db.get_product_by_id(product.id)
        if existing:
            return False, f"Product ID {product.id} already exists."
        self.db.save_product(product)
        return True, f"Product '{product.name}' added."

    def update_product(self, product: Product) -> Tuple[bool, str]:
        if not self.require_role("manager"):
            return False, "Manager or owner access required."
        self.db.save_product(product)
        return True, f"Product '{product.name}' updated."

    def adjust_stock(self, product_id: str, delta: int) -> Tuple[bool, str]:
        """Add (positive delta) or remove (negative delta) stock units."""
        if not self.require_role("manager"):
            return False, "Manager or owner access required."
        product = self.db.get_product_by_id(product_id)
        if product is None:
            return False, "Product not found."
        new_qty = product.quantity + delta
        if new_qty < 0:
            return False, f"Cannot reduce stock below 0 (current: {product.quantity})."
        product.quantity = new_qty
        self.db.save_product(product)
        return True, f"Stock updated: {product.name} → {new_qty} units."

    def remove_product(self, product_id: str) -> Tuple[bool, str]:
        if not self.require_role("manager"):
            return False, "Manager or owner access required."
        ok = self.db.delete_product(product_id)
        return (True, "Product removed.") if ok else (False, "Product not found.")

    # ------------------------------------------------------------------
    # Cart / POS
    # ------------------------------------------------------------------

    def add_to_cart(self, product_id: str, quantity: int) -> Tuple[bool, str]:
        if self.current_employee is None:
            return False, "Not logged in."
        product = self.db.get_product_by_id(product_id)
        if product is None:
            return False, "Product not found."
        if product.quantity < quantity:
            return False, f"Only {product.quantity} unit(s) in stock."
        # Update or add cart item
        for item in self.cart:
            if item.product_id == product.id:
                needed = item.quantity + quantity
                if product.quantity < needed:
                    return False, f"Only {product.quantity} unit(s) in stock."
                item.quantity = needed
                return True, f"Cart updated: {product.name} x{needed}."
        self.cart.append(CartItem(
            product_id=product.id,
            product_name=product.name,
            quantity=quantity,
            unit_price=product.price,
        ))
        return True, f"Added to cart: {product.name} x{quantity}."

    def remove_from_cart(self, product_id: str) -> Tuple[bool, str]:
        for i, item in enumerate(self.cart):
            if item.product_id == product_id.upper():
                name = item.product_name
                self.cart.pop(i)
                return True, f"Removed '{name}' from cart."
        return False, "Item not in cart."

    def clear_cart(self) -> None:
        self.cart = []

    def cart_totals(self) -> Tuple[float, float, float]:
        """Return (subtotal, tax_amount, total)."""
        subtotal = sum(item.subtotal for item in self.cart)
        tax_amount = round(subtotal * TAX_RATE, 2)
        total = round(subtotal + tax_amount, 2)
        return subtotal, tax_amount, total

    def checkout(
        self,
        payment_method: str,
        customer_id: Optional[str] = None,
    ) -> Tuple[bool, str, Optional[Transaction]]:
        """
        Finalise the current cart as a transaction.
        Returns (success, message, Transaction|None).
        """
        if not self.cart:
            return False, "Cart is empty.", None
        if self.current_employee is None:
            return False, "No employee logged in.", None

        # Verify stock is still available and decrement
        for item in self.cart:
            product = self.db.get_product_by_id(item.product_id)
            if product is None:
                return False, f"Product {item.product_id} no longer exists.", None
            if product.quantity < item.quantity:
                return False, f"Insufficient stock for {product.name}.", None

        for item in self.cart:
            product = self.db.get_product_by_id(item.product_id)
            product.quantity -= item.quantity  # type: ignore[union-attr]
            self.db.save_product(product)  # type: ignore[arg-type]

        subtotal, tax_amount, total = self.cart_totals()
        receipt_number = self.db.next_receipt_number()
        txn = Transaction(
            id=str(uuid.uuid4()),
            timestamp=datetime.now().isoformat(timespec="seconds"),
            customer_id=customer_id,
            employee_id=self.current_employee.id,
            employee_name=self.current_employee.full_name,
            items=list(self.cart),
            subtotal=round(subtotal, 2),
            tax_rate=TAX_RATE,
            tax_amount=tax_amount,
            total=total,
            payment_method=payment_method,
            receipt_number=receipt_number,
        )
        self.db.save_transaction(txn)

        # Update employee stats
        emp = self.db.get_employee_by_id(self.current_employee.id)
        if emp:
            emp.sales_total = round(emp.sales_total + total, 2)
            emp.transactions_count += 1
            self.db.save_employee(emp)
            self.current_employee = emp

        # Update customer purchase history
        if customer_id:
            customer = self.db.get_customer_by_id(customer_id)
            if customer:
                customer.purchase_history.append(txn.id)
                self.db.save_customer(customer)

        self.cart = []
        return True, f"Sale complete! Receipt: {receipt_number}", txn

    # ------------------------------------------------------------------
    # Customers
    # ------------------------------------------------------------------

    def get_customers(self) -> List[Customer]:
        return self.db.get_customers()

    def get_customer_by_id(self, cust_id: str) -> Optional[Customer]:
        return self.db.get_customer_by_id(cust_id.upper())

    def search_customers(self, query: str) -> List[Customer]:
        q = query.lower()
        return [
            c for c in self.db.get_customers()
            if q in c.full_name.lower()
            or q in c.email.lower()
            or q in c.phone
            or q in c.id.lower()
        ]

    def add_customer(self, customer: Customer) -> Tuple[bool, str]:
        existing = self.db.get_customer_by_id(customer.id)
        if existing:
            return False, "Customer ID already exists."
        self.db.save_customer(customer)
        return True, f"Customer '{customer.full_name}' added."

    def update_customer(self, customer: Customer) -> Tuple[bool, str]:
        self.db.save_customer(customer)
        return True, f"Customer '{customer.full_name}' updated."

    # ------------------------------------------------------------------
    # Employees (manager+)
    # ------------------------------------------------------------------

    def get_employees(self) -> List[Employee]:
        return self.db.get_employees()

    def add_employee(self, employee: Employee) -> Tuple[bool, str]:
        if not self.require_role("manager"):
            return False, "Manager or owner access required."
        self.db.save_employee(employee)
        return True, f"Employee '{employee.full_name}' added."

    # ------------------------------------------------------------------
    # Reports (manager+)
    # ------------------------------------------------------------------

    def report_sales_summary(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Return a dict summarising sales, optionally filtered by date range (YYYY-MM-DD)."""
        transactions = self.db.get_transactions()
        if start_date:
            transactions = [t for t in transactions if t.timestamp >= start_date]
        if end_date:
            transactions = [t for t in transactions if t.timestamp <= end_date + "T23:59:59"]

        total_revenue = sum(t.total for t in transactions)
        total_tax = sum(t.tax_amount for t in transactions)
        total_transactions = len(transactions)
        items_sold = sum(sum(i.quantity for i in t.items) for t in transactions)

        # Revenue by category
        revenue_by_category: Dict[str, float] = {}
        for t in transactions:
            for item in t.items:
                product = self.db.get_product_by_id(item.product_id)
                cat = product.category if product else "Unknown"
                revenue_by_category[cat] = round(
                    revenue_by_category.get(cat, 0.0) + item.subtotal, 2
                )

        # Top-selling items
        item_sales: Dict[str, Dict[str, Any]] = {}
        for t in transactions:
            for item in t.items:
                if item.product_id not in item_sales:
                    item_sales[item.product_id] = {
                        "name": item.product_name,
                        "qty": 0,
                        "revenue": 0.0,
                    }
                item_sales[item.product_id]["qty"] += item.quantity
                item_sales[item.product_id]["revenue"] = round(
                    item_sales[item.product_id]["revenue"] + item.subtotal, 2
                )
        top_items = sorted(item_sales.values(), key=lambda x: x["qty"], reverse=True)[:10]

        # Employee leaderboard
        emp_sales: Dict[str, Dict[str, Any]] = {}
        for t in transactions:
            eid = t.employee_id
            if eid not in emp_sales:
                emp_sales[eid] = {"name": t.employee_name, "total": 0.0, "count": 0}
            emp_sales[eid]["total"] = round(emp_sales[eid]["total"] + t.total, 2)
            emp_sales[eid]["count"] += 1
        employee_leaderboard = sorted(emp_sales.values(), key=lambda x: x["total"], reverse=True)

        return {
            "total_revenue": round(total_revenue, 2),
            "total_tax": round(total_tax, 2),
            "total_transactions": total_transactions,
            "items_sold": items_sold,
            "revenue_by_category": revenue_by_category,
            "top_items": top_items,
            "employee_leaderboard": employee_leaderboard,
        }

    def report_inventory(self) -> Dict[str, Any]:
        """Return an inventory report."""
        products = self.db.get_products()
        low_stock = [p for p in products if p.is_low_stock()]
        out_of_stock = [p for p in products if p.quantity == 0]
        total_value = sum(p.price * p.quantity for p in products)
        by_category: Dict[str, int] = {}
        for p in products:
            by_category[p.category] = by_category.get(p.category, 0) + 1
        return {
            "total_skus": len(products),
            "total_inventory_value": round(total_value, 2),
            "by_category": by_category,
            "low_stock": low_stock,
            "out_of_stock": out_of_stock,
        }
