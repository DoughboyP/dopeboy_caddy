"""
gun_store/cli.py
----------------
Interactive CLI for Paseo Guns — the full point-of-sale and management terminal.
"""

from __future__ import annotations

import os
import textwrap
import uuid
from datetime import datetime, date
from typing import List, Optional

from .database import Database
from .models import (
    Accessory,
    Ammunition,
    Customer,
    Employee,
    Firearm,
    Modification,
    Product,
    Transaction,
)
from .store import Store


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

WIDTH = 72


def _hr(char: str = "═") -> str:
    return char * WIDTH


def _header(title: str) -> None:
    print()
    print(_hr())
    print(f"  {title}")
    print(_hr())


def _section(title: str) -> None:
    print(f"\n  ── {title} {'─' * max(1, WIDTH - len(title) - 6)}")


def _pause() -> None:
    input("\n  Press ENTER to continue...")


def _clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def _input(prompt: str) -> str:
    return input(f"  {prompt}").strip()


def _yn(prompt: str) -> bool:
    return _input(f"{prompt} [y/N]: ").lower() == "y"


def _wrap(text: str, indent: int = 4) -> str:
    prefix = " " * indent
    return textwrap.fill(text, width=WIDTH, initial_indent=prefix, subsequent_indent=prefix)


# ---------------------------------------------------------------------------
# Product display
# ---------------------------------------------------------------------------

def _print_product(p: Product, index: Optional[int] = None) -> None:
    prefix = f"  [{index}]" if index is not None else "  "
    low = "  ⚠ LOW STOCK" if p.is_low_stock() else ""
    print(f"{prefix} {p.id:<10} {p.brand} {p.model:<28} ${p.price:>8,.2f}  Qty:{p.quantity}{low}")


def _print_product_detail(p: Product) -> None:
    _section(f"{p.brand} {p.model}")
    print(f"    ID          : {p.id}")
    print(f"    Name        : {p.name}")
    print(f"    Category    : {p.category}")
    print(f"    Price       : ${p.price:,.2f}")
    print(f"    In Stock    : {p.quantity}")
    print(f"    Reorder At  : {p.reorder_level}")
    print(_wrap(p.description))

    if isinstance(p, Firearm):
        print(f"    Type        : {p.firearm_type}")
        print(f"    Caliber     : {p.caliber}")
        print(f"    Action      : {p.action}")
        print(f"    Barrel      : {p.barrel_length}")
        print(f"    Capacity    : {p.capacity}")
        print(f"    Finish      : {p.finish}")
    elif isinstance(p, Ammunition):
        print(f"    Caliber     : {p.caliber}")
        print(f"    Type        : {p.ammo_type}")
        print(f"    Grain       : {p.grain}")
        print(f"    Rds/Box     : {p.rounds_per_box}")
        print(f"    Velocity    : {p.velocity}")
    elif isinstance(p, Accessory):
        print(f"    Type        : {p.accessory_type}")
        print(f"    Compatible  : {p.compatible_with}")
    elif isinstance(p, Modification):
        print(f"    Mod Type    : {p.mod_type}")
        print(f"    Compatible  : {p.compatible_with}")
        print(f"    Pro Install : {'Yes' if p.installation_required else 'No — Drop-In'}")


# ---------------------------------------------------------------------------
# Main CLI class
# ---------------------------------------------------------------------------

class GunStoreCLI:

    def __init__(self, db_path: Optional[str] = None) -> None:
        db = Database(db_path) if db_path else Database()
        db.load()
        self.store = Store(db)

    # ------------------------------------------------------------------
    # Top-level flow
    # ------------------------------------------------------------------

    def run(self) -> None:
        _clear()
        self._splash()
        while True:
            if self.store.current_employee is None:
                if not self._login_screen():
                    break
            else:
                if not self._main_menu():
                    break

    def _splash(self) -> None:
        print()
        print(_hr("═"))
        print()
        print("  ██████╗  █████╗ ███████╗███████╗ ██████╗      ██████╗ ██╗   ██╗███╗   ██╗███████╗")
        print("  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗    ██╔════╝ ██║   ██║████╗  ██║██╔════╝")
        print("  ██████╔╝███████║███████╗█████╗  ██║   ██║    ██║  ███╗██║   ██║██╔██╗ ██║███████╗")
        print("  ██╔═══╝ ██╔══██║╚════██║██╔══╝  ██║   ██║    ██║   ██║██║   ██║██║╚██╗██║╚════██║")
        print("  ██║     ██║  ██║███████║███████╗╚██████╔╝    ╚██████╔╝╚██████╔╝██║ ╚████║███████║")
        print("  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
        print()
        print(f"  {Store.NAME}")
        print(f"  {Store.ADDRESS}")
        print(f"  {Store.PHONE}  |  {Store.HOURS}")
        print(f"  {Store.FFL}")
        print()
        print(_hr("═"))

    # ------------------------------------------------------------------
    # Login
    # ------------------------------------------------------------------

    def _login_screen(self) -> bool:
        _header("EMPLOYEE LOGIN")
        print("  Enter your Employee ID and PIN to begin.")
        print("  Type 'quit' to exit.\n")
        emp_id = _input("Employee ID: ")
        if emp_id.lower() == "quit":
            print("\n  Goodbye — stay safe out there.\n")
            return False
        pin = _input("PIN       : ")
        ok, msg = self.store.login(emp_id, pin)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        if not ok:
            _pause()
        return True

    # ------------------------------------------------------------------
    # Main menu (role-aware)
    # ------------------------------------------------------------------

    def _main_menu(self) -> bool:
        _clear()
        emp = self.store.current_employee
        _header(f"MAIN MENU  —  {emp.full_name}  [{emp.role.upper()}]")  # type: ignore[union-attr]
        print()
        print("  [1] Browse Inventory")
        print("  [2] Search Products")
        print("  [3] Point of Sale (POS)")
        print("  [4] View Cart")
        print("  [5] Customer Management")
        if self.store.require_role("manager"):
            print("  [6] Inventory Management")
            print("  [7] Reports")
        if self.store.require_role("owner"):
            print("  [8] Employee Management")
        print()
        print("  [9] Store Information")
        print("  [L] Logout")
        print("  [Q] Quit")
        print()
        choice = _input("Select: ").upper()

        if choice == "1":
            self._browse_inventory()
        elif choice == "2":
            self._search_products()
        elif choice == "3":
            self._pos_menu()
        elif choice == "4":
            self._view_cart()
        elif choice == "5":
            self._customer_menu()
        elif choice == "6" and self.store.require_role("manager"):
            self._inventory_management()
        elif choice == "7" and self.store.require_role("manager"):
            self._reports_menu()
        elif choice == "8" and self.store.require_role("owner"):
            self._employee_management()
        elif choice == "9":
            self._store_info()
        elif choice == "L":
            self.store.logout()
            print("\n  Logged out.\n")
            _pause()
        elif choice == "Q":
            if _yn("  Exit Paseo Guns?"):
                print("\n  Closing terminal. Stay strapped, stay safe.\n")
                return False
        return True

    # ------------------------------------------------------------------
    # Browse inventory
    # ------------------------------------------------------------------

    def _browse_inventory(self) -> None:
        _clear()
        _header("BROWSE INVENTORY")
        print()
        print("  [1] Firearms — Handguns")
        print("  [2] Firearms — Rifles")
        print("  [3] Firearms — Shotguns")
        print("  [4] Ammunition")
        print("  [5] Accessories")
        print("  [6] Modifications")
        print("  [7] Interdimensional Collection ★")
        print("  [8] All Products")
        print("  [B] Back")
        print()
        choice = _input("Select: ").upper()

        cat_map = {
            "1": ("Firearm",   "Handgun"),
            "2": ("Firearm",   "Rifle"),
            "3": ("Firearm",   "Shotgun"),
            "4": ("Ammunition", None),
            "5": ("Accessory",  None),
            "6": ("Modification", None),
            "7": ("Interdimensional", None),
        }

        if choice == "B":
            return
        if choice == "8":
            products = self.store.get_all_products()
            self._product_list_view(products, "ALL PRODUCTS")
            return
        if choice in cat_map:
            cat, ftype = cat_map[choice]
            if ftype:
                products = self.store.get_firearms(ftype)
            else:
                products = self.store.get_products_by_category(cat)
            label = f"{cat.upper()} — {ftype}" if ftype else cat.upper()
            self._product_list_view(products, label)

    def _product_list_view(self, products: List[Product], title: str) -> None:
        if not products:
            print("\n  No products found.")
            _pause()
            return
        _clear()
        _header(title)
        print(f"  {'ID':<10} {'Brand + Model':<35} {'Price':>9}  Qty")
        print("  " + "─" * (WIDTH - 2))
        for p in products:
            _print_product(p)
        print(f"\n  {len(products)} item(s) found.")
        print()
        pid = _input("Enter product ID to view details (or ENTER to go back): ").upper()
        if pid:
            product = self.store.get_product_by_id(pid)
            if product:
                _clear()
                _print_product_detail(product)
                print()
                if _yn("  Add to cart?"):
                    self._add_to_cart_prompt(product)
            else:
                print("  Product not found.")
            _pause()

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def _search_products(self) -> None:
        _clear()
        _header("SEARCH PRODUCTS")
        query = _input("Search (brand, model, caliber, description…): ")
        if not query:
            return
        results = self.store.search_products(query)
        self._product_list_view(results, f"SEARCH: '{query}'")

    # ------------------------------------------------------------------
    # POS
    # ------------------------------------------------------------------

    def _pos_menu(self) -> None:
        _clear()
        _header("POINT OF SALE")
        print()
        print("  [1] Add item to cart by ID")
        print("  [2] View / edit cart")
        print("  [3] Checkout")
        print("  [4] Clear cart")
        print("  [B] Back")
        print()
        choice = _input("Select: ").upper()
        if choice == "1":
            self._add_item_by_id()
        elif choice == "2":
            self._view_cart()
        elif choice == "3":
            self._checkout()
        elif choice == "4":
            if _yn("  Clear all items from cart?"):
                self.store.clear_cart()
                print("  Cart cleared.")
                _pause()

    def _add_item_by_id(self) -> None:
        pid = _input("Product ID: ").upper()
        if not pid:
            return
        product = self.store.get_product_by_id(pid)
        if not product:
            print("  Product not found.")
            _pause()
            return
        _print_product_detail(product)
        try:
            qty = int(_input("Quantity: ") or "1")
        except ValueError:
            qty = 1
        ok, msg = self.store.add_to_cart(pid, qty)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        _pause()

    def _add_to_cart_prompt(self, product: Product) -> None:
        try:
            qty = int(_input("Quantity: ") or "1")
        except ValueError:
            qty = 1
        ok, msg = self.store.add_to_cart(product.id, qty)
        print(f"\n  {'✓' if ok else '✗'} {msg}")

    def _view_cart(self) -> None:
        _clear()
        _header("CURRENT CART")
        if not self.store.cart:
            print("\n  Cart is empty.")
            _pause()
            return
        print(f"\n  {'Product':<38} {'Qty':>4}  {'Unit':>9}  {'Subtotal':>10}")
        print("  " + "─" * (WIDTH - 2))
        for item in self.store.cart:
            name = item.product_name[:37]
            print(f"  {name:<38} {item.quantity:>4}  ${item.unit_price:>8,.2f}  ${item.subtotal:>9,.2f}")
        subtotal, tax, total = self.store.cart_totals()
        print("  " + "─" * (WIDTH - 2))
        print(f"  {'Subtotal':>54}  ${subtotal:>9,.2f}")
        print(f"  {'Tax (8.25%)':>54}  ${tax:>9,.2f}")
        print(f"  {'TOTAL':>54}  ${total:>9,.2f}")
        print()
        pid = _input("Enter product ID to remove (or ENTER to go back): ").upper()
        if pid:
            ok, msg = self.store.remove_from_cart(pid)
            print(f"  {'✓' if ok else '✗'} {msg}")
            _pause()

    def _checkout(self) -> None:
        _clear()
        _header("CHECKOUT")
        if not self.store.cart:
            print("\n  Cart is empty.")
            _pause()
            return
        self._view_cart()
        print("\n  Payment methods: [1] Cash  [2] Card  [3] Check")
        pay_choice = _input("Payment method: ")
        pay_map = {"1": "Cash", "2": "Card", "3": "Check"}
        payment = pay_map.get(pay_choice, "Cash")

        cust_id: Optional[str] = None
        if _yn("  Link to a customer record?"):
            cust_id = self._pick_customer()

        ok, msg, txn = self.store.checkout(payment, cust_id)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        if txn:
            self._print_receipt(txn)
        _pause()

    def _print_receipt(self, txn: Transaction) -> None:
        print()
        print(_hr("─"))
        print(f"  {Store.NAME}")
        print(f"  {Store.ADDRESS}")
        print(f"  {Store.PHONE}")
        print(f"  Receipt #: {txn.receipt_number}   {txn.timestamp}")
        print(f"  Payment  : {txn.payment_method}")
        print(_hr("─"))
        for item in txn.items:
            name = item.product_name[:36]
            print(f"  {name:<36} x{item.quantity:<3} ${item.subtotal:>8,.2f}")
        print(_hr("─"))
        print(f"  {'Subtotal':>50}  ${txn.subtotal:>8,.2f}")
        print(f"  {'Tax (8.25%)':>50}  ${txn.tax_amount:>8,.2f}")
        print(f"  {'TOTAL':>50}  ${txn.total:>8,.2f}")
        print(_hr("─"))
        print("  Thank you for shopping at Paseo Guns!")
        print("  All sales final. Valid ID required for firearm transfers.")
        print(_hr("─"))

    # ------------------------------------------------------------------
    # Customer management
    # ------------------------------------------------------------------

    def _customer_menu(self) -> None:
        while True:
            _clear()
            _header("CUSTOMER MANAGEMENT")
            print()
            print("  [1] Search customers")
            print("  [2] View all customers")
            print("  [3] Add new customer")
            print("  [4] Edit customer")
            print("  [B] Back")
            print()
            choice = _input("Select: ").upper()
            if choice == "B":
                return
            elif choice == "1":
                self._search_customers()
            elif choice == "2":
                self._list_customers(self.store.get_customers())
            elif choice == "3":
                self._add_customer()
            elif choice == "4":
                self._edit_customer()

    def _search_customers(self) -> None:
        q = _input("Search (name, email, phone, ID): ")
        results = self.store.search_customers(q)
        self._list_customers(results)

    def _list_customers(self, customers: List[Customer]) -> None:
        _clear()
        _header("CUSTOMERS")
        if not customers:
            print("\n  No customers found.")
            _pause()
            return
        print(f"\n  {'ID':<10} {'Name':<24} {'Phone':<16} {'BG Check':<12} {'Verified'}")
        print("  " + "─" * (WIDTH - 2))
        for c in customers:
            ver = "✓" if c.id_verified else "✗"
            print(f"  {c.id:<10} {c.full_name:<24} {c.phone:<16} {c.background_check_status:<12} {ver}")
        print()
        cid = _input("Enter customer ID to view details (or ENTER to go back): ").upper()
        if cid:
            cust = self.store.get_customer_by_id(cid)
            if cust:
                self._print_customer_detail(cust)
            else:
                print("  Customer not found.")
            _pause()

    def _print_customer_detail(self, c: Customer) -> None:
        _section(c.full_name)
        print(f"    ID              : {c.id}")
        print(f"    Email           : {c.email}")
        print(f"    Phone           : {c.phone}")
        print(f"    Address         : {c.address}")
        print(f"    DOB             : {c.dob}")
        print(f"    ID Verified     : {'Yes' if c.id_verified else 'No'}")
        print(f"    Background Check: {c.background_check_status.upper()}")
        print(f"    Notes           : {c.notes or '—'}")
        print(f"    Purchases       : {len(c.purchase_history)} transaction(s)")
        print(f"    Member Since    : {c.created_at}")

    def _pick_customer(self) -> Optional[str]:
        q = _input("Search customer by name/ID (or ENTER to skip): ")
        if not q:
            return None
        results = self.store.search_customers(q)
        if not results:
            print("  No customers found.")
            return None
        for i, c in enumerate(results[:10], 1):
            print(f"  [{i}] {c.id} — {c.full_name}")
        try:
            idx = int(_input("Select #: ")) - 1
            if 0 <= idx < len(results):
                return results[idx].id
        except (ValueError, IndexError):
            pass
        return None

    def _add_customer(self) -> None:
        _clear()
        _header("ADD NEW CUSTOMER")
        cid = f"CUST{str(uuid.uuid4())[:8].upper()}"
        first = _input("First name  : ")
        last  = _input("Last name   : ")
        email = _input("Email       : ")
        phone = _input("Phone       : ")
        addr  = _input("Address     : ")
        dob   = _input("DOB (YYYY-MM-DD): ")
        id_ver = _yn("ID verified?")
        bg    = _input("Background check status (approved/pending/denied): ").lower() or "pending"
        notes = _input("Notes       : ")

        cust = Customer(
            id=cid,
            first_name=first,
            last_name=last,
            email=email,
            phone=phone,
            address=addr,
            dob=dob,
            id_verified=id_ver,
            background_check_status=bg,
            notes=notes,
            purchase_history=[],
            created_at=date.today().isoformat(),
        )
        ok, msg = self.store.add_customer(cust)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        if ok:
            print(f"  Customer ID: {cid}")
        _pause()

    def _edit_customer(self) -> None:
        cid = _input("Customer ID to edit: ").upper()
        cust = self.store.get_customer_by_id(cid)
        if not cust:
            print("  Customer not found.")
            _pause()
            return
        self._print_customer_detail(cust)
        print()
        print("  Fields: notes / bg_status / id_verified")
        field = _input("Field to update: ").lower()
        if field == "notes":
            cust.notes = _input("New notes: ")
        elif field == "bg_status":
            cust.background_check_status = _input("New status (approved/pending/denied): ").lower()
        elif field == "id_verified":
            cust.id_verified = _yn("ID verified?")
        else:
            print("  Unknown field.")
            _pause()
            return
        ok, msg = self.store.update_customer(cust)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        _pause()

    # ------------------------------------------------------------------
    # Inventory management (manager+)
    # ------------------------------------------------------------------

    def _inventory_management(self) -> None:
        while True:
            _clear()
            _header("INVENTORY MANAGEMENT")
            print()
            print("  [1] View low-stock alerts")
            print("  [2] Adjust stock quantity")
            print("  [3] Update product price")
            print("  [4] Remove product")
            print("  [5] Add new product (manual)")
            print("  [B] Back")
            print()
            choice = _input("Select: ").upper()
            if choice == "B":
                return
            elif choice == "1":
                self._low_stock_view()
            elif choice == "2":
                self._adjust_stock()
            elif choice == "3":
                self._update_price()
            elif choice == "4":
                self._remove_product()
            elif choice == "5":
                self._add_product_manual()

    def _low_stock_view(self) -> None:
        _clear()
        _header("LOW STOCK ALERTS")
        items = self.store.get_low_stock()
        if not items:
            print("\n  ✓ All products are adequately stocked.")
        else:
            print(f"\n  {len(items)} item(s) at or below reorder level:\n")
            print(f"  {'ID':<10} {'Name':<38} {'Qty':>5}  {'Reorder@':>8}")
            print("  " + "─" * (WIDTH - 2))
            for p in items:
                name = f"{p.brand} {p.model}"[:37]
                marker = " ✗ OUT" if p.quantity == 0 else ""
                print(f"  {p.id:<10} {name:<38} {p.quantity:>5}  {p.reorder_level:>8}{marker}")
        _pause()

    def _adjust_stock(self) -> None:
        pid = _input("Product ID: ").upper()
        try:
            delta = int(_input("Quantity change (+add / -remove): "))
        except ValueError:
            print("  Invalid number.")
            _pause()
            return
        ok, msg = self.store.adjust_stock(pid, delta)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        _pause()

    def _update_price(self) -> None:
        pid = _input("Product ID: ").upper()
        product = self.store.get_product_by_id(pid)
        if not product:
            print("  Product not found.")
            _pause()
            return
        print(f"  Current price: ${product.price:,.2f}")
        try:
            new_price = float(_input("New price: $"))
        except ValueError:
            print("  Invalid price.")
            _pause()
            return
        product.price = round(new_price, 2)
        ok, msg = self.store.update_product(product)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        _pause()

    def _remove_product(self) -> None:
        pid = _input("Product ID to remove: ").upper()
        product = self.store.get_product_by_id(pid)
        if not product:
            print("  Product not found.")
            _pause()
            return
        print(f"\n  {product.brand} {product.model} — ${product.price:,.2f}")
        if _yn("  Confirm removal?"):
            ok, msg = self.store.remove_product(pid)
            print(f"  {'✓' if ok else '✗'} {msg}")
        _pause()

    def _add_product_manual(self) -> None:
        _clear()
        _header("ADD NEW PRODUCT")
        print("  Categories: Firearm | Ammunition | Accessory | Modification | Interdimensional")
        cat = _input("Category: ").strip()
        pid = _input("Product ID (e.g. FH099): ").upper()
        brand = _input("Brand      : ")
        model = _input("Model      : ")
        name  = _input("Name       : ")
        desc  = _input("Description: ")
        try:
            price = float(_input("Price ($)  : "))
            qty   = int(_input("Quantity   : "))
            reorder = int(_input("Reorder at : "))
        except ValueError:
            print("  Invalid numeric input.")
            _pause()
            return

        from .models import Product as BaseProduct
        p = BaseProduct(
            id=pid, name=name, brand=brand, model=model,
            description=desc, price=price, quantity=qty,
            reorder_level=reorder, category=cat,
        )
        ok, msg = self.store.add_product(p)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        _pause()

    # ------------------------------------------------------------------
    # Reports (manager+)
    # ------------------------------------------------------------------

    def _reports_menu(self) -> None:
        while True:
            _clear()
            _header("REPORTS")
            print()
            print("  [1] Sales summary (all time)")
            print("  [2] Sales summary (date range)")
            print("  [3] Inventory report")
            print("  [4] Employee leaderboard")
            print("  [B] Back")
            print()
            choice = _input("Select: ").upper()
            if choice == "B":
                return
            elif choice == "1":
                self._print_sales_report(None, None)
            elif choice == "2":
                start = _input("Start date YYYY-MM-DD: ")
                end   = _input("End date   YYYY-MM-DD: ")
                self._print_sales_report(start or None, end or None)
            elif choice == "3":
                self._print_inventory_report()
            elif choice == "4":
                self._print_employee_leaderboard()

    def _print_sales_report(self, start: Optional[str], end: Optional[str]) -> None:
        _clear()
        label = "ALL TIME"
        if start or end:
            label = f"{start or '…'} → {end or '…'}"
        _header(f"SALES REPORT — {label}")
        r = self.store.report_sales_summary(start, end)

        print(f"\n  Total Revenue        : ${r['total_revenue']:>12,.2f}")
        print(f"  Total Tax Collected  : ${r['total_tax']:>12,.2f}")
        print(f"  Transactions         : {r['total_transactions']:>12,}")
        print(f"  Items Sold           : {r['items_sold']:>12,}")

        if r["revenue_by_category"]:
            _section("Revenue by Category")
            for cat, rev in sorted(r["revenue_by_category"].items(), key=lambda x: -x[1]):
                print(f"    {cat:<25}  ${rev:>10,.2f}")

        if r["top_items"]:
            _section("Top-Selling Items")
            print(f"  {'Product':<40} {'Qty':>5}  {'Revenue':>10}")
            for item in r["top_items"]:
                name = item["name"][:39]
                print(f"  {name:<40} {item['qty']:>5}  ${item['revenue']:>9,.2f}")

        _pause()

    def _print_inventory_report(self) -> None:
        _clear()
        _header("INVENTORY REPORT")
        r = self.store.report_inventory()
        print(f"\n  Total SKUs           : {r['total_skus']:>10,}")
        print(f"  Total Inventory Value: ${r['total_inventory_value']:>10,.2f}")
        _section("By Category")
        for cat, count in r["by_category"].items():
            print(f"    {cat:<25}  {count:>5} SKU(s)")
        _section("Low Stock / Out of Stock")
        if not r["low_stock"]:
            print("    All items adequately stocked.")
        else:
            for p in r["low_stock"]:
                out = " — OUT OF STOCK" if p.quantity == 0 else ""
                print(f"    {p.id:<10} {p.brand} {p.model[:30]:<30} Qty:{p.quantity}{out}")
        _pause()

    def _print_employee_leaderboard(self) -> None:
        _clear()
        _header("EMPLOYEE LEADERBOARD")
        r = self.store.report_sales_summary()
        lb = r["employee_leaderboard"]
        if not lb:
            print("\n  No sales recorded yet.")
        else:
            print(f"\n  {'Name':<25} {'Transactions':>14} {'Total Sales':>13}")
            print("  " + "─" * (WIDTH - 2))
            for rank, emp in enumerate(lb, 1):
                print(f"  {rank}. {emp['name']:<23} {emp['count']:>14,}  ${emp['total']:>12,.2f}")
        # Also show current DB stats
        _section("Current Employee Records")
        for emp in self.store.get_employees():
            status = "ACTIVE" if emp.active else "inactive"
            print(f"    {emp.id:<8} {emp.full_name:<22} {emp.role.upper():<10} {status}")
        _pause()

    # ------------------------------------------------------------------
    # Employee management (owner only)
    # ------------------------------------------------------------------

    def _employee_management(self) -> None:
        while True:
            _clear()
            _header("EMPLOYEE MANAGEMENT  [OWNER]")
            print()
            print("  [1] List all employees")
            print("  [2] Add employee")
            print("  [3] Deactivate / activate employee")
            print("  [B] Back")
            print()
            choice = _input("Select: ").upper()
            if choice == "B":
                return
            elif choice == "1":
                self._list_employees()
            elif choice == "2":
                self._add_employee()
            elif choice == "3":
                self._toggle_employee()

    def _list_employees(self) -> None:
        _clear()
        _header("EMPLOYEES")
        emps = self.store.get_employees()
        print(f"\n  {'ID':<8} {'Name':<24} {'Role':<10} {'Sales Total':>12}  {'Status'}")
        print("  " + "─" * (WIDTH - 2))
        for e in emps:
            status = "ACTIVE" if e.active else "inactive"
            print(f"  {e.id:<8} {e.full_name:<24} {e.role:<10} ${e.sales_total:>11,.2f}  {status}")
        _pause()

    def _add_employee(self) -> None:
        _clear()
        _header("ADD EMPLOYEE")
        eid = f"EMP{str(uuid.uuid4())[:6].upper()}"
        first = _input("First name  : ")
        last  = _input("Last name   : ")
        print("  Roles: cashier | manager | owner")
        role  = _input("Role        : ").lower()
        pin   = _input("PIN (4-digit): ")
        email = _input("Email       : ")
        phone = _input("Phone       : ")

        emp = Employee(
            id=eid,
            first_name=first,
            last_name=last,
            role=role,
            pin=pin,
            email=email,
            phone=phone,
            hire_date=date.today().isoformat(),
            active=True,
            sales_total=0.0,
            transactions_count=0,
        )
        ok, msg = self.store.add_employee(emp)
        print(f"\n  {'✓' if ok else '✗'} {msg}")
        if ok:
            print(f"  Employee ID: {eid}")
        _pause()

    def _toggle_employee(self) -> None:
        eid = _input("Employee ID: ").upper()
        emp = self.store.db.get_employee_by_id(eid)
        if not emp:
            print("  Employee not found.")
            _pause()
            return
        emp.active = not emp.active
        self.store.db.save_employee(emp)
        status = "activated" if emp.active else "deactivated"
        print(f"\n  ✓ {emp.full_name} {status}.")
        _pause()

    # ------------------------------------------------------------------
    # Store info
    # ------------------------------------------------------------------

    def _store_info(self) -> None:
        _clear()
        _header("STORE INFORMATION")
        print(f"\n  Name    : {Store.NAME}")
        print(f"  Address : {Store.ADDRESS}")
        print(f"  Phone   : {Store.PHONE}")
        print(f"  Hours   : {Store.HOURS}")
        print(f"  FFL#    : {Store.FFL}")
        print(f"  Tax Rate: {Store.NAME} collects 8.25% sales tax")
        print()
        print("  ── Interdimensional Collection Notice ──────────────────────────")
        print(_wrap(
            "The Interdimensional Collection (Dim. 1–5) contains exotic firearms "
            "and modifications sourced from parallel dimensions by the proprietor. "
            "All items are catalogued as rare / collector-grade. Standard 4473 "
            "and background check requirements apply to all firearm transfers "
            "regardless of dimensional origin.",
            indent=2,
        ))
        _pause()
