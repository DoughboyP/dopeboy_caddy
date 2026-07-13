"""
gun_store/database.py
---------------------
JSON-based persistence layer for Paseo Guns.
All store data is saved to a single JSON file in the working directory.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List

from .models import (
    Ammunition,
    Customer,
    Employee,
    Firearm,
    Modification,
    Accessory,
    Product,
    Transaction,
    product_from_dict,
)
from . import seed_data


DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "paseo_guns_data.json")


class Database:
    """Read/write store data from a JSON file."""

    def __init__(self, db_path: str = DEFAULT_DB_PATH) -> None:
        self.db_path = db_path
        self._data: Dict[str, Any] = {}

    # ------------------------------------------------------------------
    # Load / save
    # ------------------------------------------------------------------

    def load(self) -> None:
        """Load from disk, seeding with default data if the file does not exist."""
        if os.path.exists(self.db_path):
            with open(self.db_path, "r", encoding="utf-8") as fh:
                self._data = json.load(fh)
        else:
            self._seed()
            self.save()

    def save(self) -> None:
        """Persist current state to disk."""
        with open(self.db_path, "w", encoding="utf-8") as fh:
            json.dump(self._data, fh, indent=2, ensure_ascii=False)

    def _seed(self) -> None:
        """Populate with initial demo data."""
        self._data = {
            "products": (
                seed_data.FIREARMS
                + seed_data.AMMUNITION
                + seed_data.ACCESSORIES
                + seed_data.MODIFICATIONS
            ),
            "employees": seed_data.EMPLOYEES,
            "customers": seed_data.CUSTOMERS,
            "transactions": [],
            "receipt_counter": 1000,
        }

    # ------------------------------------------------------------------
    # Products
    # ------------------------------------------------------------------

    def get_products(self) -> List[Product]:
        return [product_from_dict(d) for d in self._data.get("products", [])]

    def get_product_by_id(self, product_id: str) -> Product | None:
        for d in self._data.get("products", []):
            if d["id"] == product_id:
                return product_from_dict(d)
        return None

    def save_product(self, product: Product) -> None:
        products = self._data.get("products", [])
        for i, d in enumerate(products):
            if d["id"] == product.id:
                products[i] = product.to_dict()
                self.save()
                return
        products.append(product.to_dict())
        self._data["products"] = products
        self.save()

    def delete_product(self, product_id: str) -> bool:
        products = self._data.get("products", [])
        new_list = [d for d in products if d["id"] != product_id]
        if len(new_list) == len(products):
            return False
        self._data["products"] = new_list
        self.save()
        return True

    # ------------------------------------------------------------------
    # Employees
    # ------------------------------------------------------------------

    def get_employees(self) -> List[Employee]:
        return [Employee.from_dict(d) for d in self._data.get("employees", [])]

    def get_employee_by_id(self, emp_id: str) -> Employee | None:
        for d in self._data.get("employees", []):
            if d["id"] == emp_id:
                return Employee.from_dict(d)
        return None

    def save_employee(self, employee: Employee) -> None:
        employees = self._data.get("employees", [])
        for i, d in enumerate(employees):
            if d["id"] == employee.id:
                employees[i] = employee.to_dict()
                self.save()
                return
        employees.append(employee.to_dict())
        self._data["employees"] = employees
        self.save()

    # ------------------------------------------------------------------
    # Customers
    # ------------------------------------------------------------------

    def get_customers(self) -> List[Customer]:
        return [Customer.from_dict(d) for d in self._data.get("customers", [])]

    def get_customer_by_id(self, cust_id: str) -> Customer | None:
        for d in self._data.get("customers", []):
            if d["id"] == cust_id:
                return Customer.from_dict(d)
        return None

    def save_customer(self, customer: Customer) -> None:
        customers = self._data.get("customers", [])
        for i, d in enumerate(customers):
            if d["id"] == customer.id:
                customers[i] = customer.to_dict()
                self.save()
                return
        customers.append(customer.to_dict())
        self._data["customers"] = customers
        self.save()

    # ------------------------------------------------------------------
    # Transactions
    # ------------------------------------------------------------------

    def get_transactions(self) -> List[Transaction]:
        return [Transaction.from_dict(d) for d in self._data.get("transactions", [])]

    def save_transaction(self, transaction: Transaction) -> None:
        transactions = self._data.get("transactions", [])
        transactions.append(transaction.to_dict())
        self._data["transactions"] = transactions
        self.save()

    # ------------------------------------------------------------------
    # Receipt counter
    # ------------------------------------------------------------------

    def next_receipt_number(self) -> str:
        n = self._data.get("receipt_counter", 1000)
        self._data["receipt_counter"] = n + 1
        self.save()
        return f"PG-{n:05d}"
