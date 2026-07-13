"""
gun_store/models.py
-------------------
Data-model classes for the Paseo Guns management system.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Product hierarchy
# ---------------------------------------------------------------------------

@dataclass
class Product:
    """Base class for every sellable item in the store."""

    id: str
    name: str
    brand: str
    model: str
    description: str
    price: float
    quantity: int
    reorder_level: int
    category: str          # "Firearm" | "Ammunition" | "Accessory" | "Modification"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "model": self.model,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "reorder_level": self.reorder_level,
            "category": self.category,
            "product_type": self.__class__.__name__,
        }

    def is_low_stock(self) -> bool:
        return self.quantity <= self.reorder_level

    def __str__(self) -> str:  # pragma: no cover
        stock_tag = " ⚠ LOW STOCK" if self.is_low_stock() else ""
        return (
            f"[{self.id}] {self.brand} {self.model} — {self.name}  "
            f"${self.price:,.2f}  Qty:{self.quantity}{stock_tag}"
        )


@dataclass
class Firearm(Product):
    """A firearm (handgun, rifle, or shotgun)."""

    firearm_type: str = ""    # Handgun | Rifle | Shotgun
    caliber: str = ""
    action: str = ""          # Semi-Auto | Bolt-Action | Pump | Revolver | etc.
    barrel_length: str = ""
    capacity: str = ""
    finish: str = ""

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "firearm_type": self.firearm_type,
            "caliber": self.caliber,
            "action": self.action,
            "barrel_length": self.barrel_length,
            "capacity": self.capacity,
            "finish": self.finish,
        })
        return d


@dataclass
class Ammunition(Product):
    """A box / pack of ammunition."""

    caliber: str = ""
    ammo_type: str = ""       # FMJ | JHP | Buckshot | Slug | Birdshot | etc.
    grain: str = ""
    rounds_per_box: int = 0
    velocity: str = ""

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "caliber": self.caliber,
            "ammo_type": self.ammo_type,
            "grain": self.grain,
            "rounds_per_box": self.rounds_per_box,
            "velocity": self.velocity,
        })
        return d


@dataclass
class Accessory(Product):
    """An accessory (optic, magazine, holster, light, sling, cleaning kit, …)."""

    accessory_type: str = ""   # Optics | Magazines | Holsters | Lights & Lasers | ...
    compatible_with: str = ""

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "accessory_type": self.accessory_type,
            "compatible_with": self.compatible_with,
        })
        return d


@dataclass
class Modification(Product):
    """A drop-in or gunsmith-installed firearm modification."""

    mod_type: str = ""         # Triggers | Barrels | Slides | Stocks | Muzzle Devices | ...
    compatible_with: str = ""
    installation_required: bool = True

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "mod_type": self.mod_type,
            "compatible_with": self.compatible_with,
            "installation_required": self.installation_required,
        })
        return d


def product_from_dict(data: Dict[str, Any]) -> Product:
    """Deserialise a product dict back into the appropriate subclass instance."""
    ptype = data.get("product_type", "Product")
    common = {
        "id": data["id"],
        "name": data["name"],
        "brand": data["brand"],
        "model": data["model"],
        "description": data["description"],
        "price": data["price"],
        "quantity": data["quantity"],
        "reorder_level": data["reorder_level"],
        "category": data["category"],
    }
    if ptype == "Firearm":
        return Firearm(
            **common,
            firearm_type=data.get("firearm_type", ""),
            caliber=data.get("caliber", ""),
            action=data.get("action", ""),
            barrel_length=data.get("barrel_length", ""),
            capacity=data.get("capacity", ""),
            finish=data.get("finish", ""),
        )
    if ptype == "Ammunition":
        return Ammunition(
            **common,
            caliber=data.get("caliber", ""),
            ammo_type=data.get("ammo_type", ""),
            grain=data.get("grain", ""),
            rounds_per_box=data.get("rounds_per_box", 0),
            velocity=data.get("velocity", ""),
        )
    if ptype == "Accessory":
        return Accessory(
            **common,
            accessory_type=data.get("accessory_type", ""),
            compatible_with=data.get("compatible_with", ""),
        )
    if ptype == "Modification":
        return Modification(
            **common,
            mod_type=data.get("mod_type", ""),
            compatible_with=data.get("compatible_with", ""),
            installation_required=data.get("installation_required", True),
        )
    return Product(**common)


# ---------------------------------------------------------------------------
# Cart & Transaction
# ---------------------------------------------------------------------------

@dataclass
class CartItem:
    product_id: str
    product_name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return round(self.quantity * self.unit_price, 2)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "subtotal": self.subtotal,
        }


@dataclass
class Transaction:
    id: str
    timestamp: str
    customer_id: Optional[str]
    employee_id: str
    employee_name: str
    items: List[CartItem]
    subtotal: float
    tax_rate: float
    tax_amount: float
    total: float
    payment_method: str
    receipt_number: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "customer_id": self.customer_id,
            "employee_id": self.employee_id,
            "employee_name": self.employee_name,
            "items": [i.to_dict() for i in self.items],
            "subtotal": self.subtotal,
            "tax_rate": self.tax_rate,
            "tax_amount": self.tax_amount,
            "total": self.total,
            "payment_method": self.payment_method,
            "receipt_number": self.receipt_number,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Transaction":
        items = [
            CartItem(
                product_id=i["product_id"],
                product_name=i["product_name"],
                quantity=i["quantity"],
                unit_price=i["unit_price"],
            )
            for i in data.get("items", [])
        ]
        return cls(
            id=data["id"],
            timestamp=data["timestamp"],
            customer_id=data.get("customer_id"),
            employee_id=data["employee_id"],
            employee_name=data.get("employee_name", ""),
            items=items,
            subtotal=data["subtotal"],
            tax_rate=data["tax_rate"],
            tax_amount=data["tax_amount"],
            total=data["total"],
            payment_method=data["payment_method"],
            receipt_number=data["receipt_number"],
        )


# ---------------------------------------------------------------------------
# Customer
# ---------------------------------------------------------------------------

@dataclass
class Customer:
    id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    dob: str                         # YYYY-MM-DD for age verification
    id_verified: bool
    background_check_status: str     # "approved" | "pending" | "denied"
    notes: str
    purchase_history: List[str]      # transaction IDs
    created_at: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "dob": self.dob,
            "id_verified": self.id_verified,
            "background_check_status": self.background_check_status,
            "notes": self.notes,
            "purchase_history": self.purchase_history,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Customer":
        return cls(
            id=data["id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone=data["phone"],
            address=data["address"],
            dob=data["dob"],
            id_verified=data["id_verified"],
            background_check_status=data["background_check_status"],
            notes=data.get("notes", ""),
            purchase_history=data.get("purchase_history", []),
            created_at=data["created_at"],
        )


# ---------------------------------------------------------------------------
# Employee
# ---------------------------------------------------------------------------

@dataclass
class Employee:
    id: str
    first_name: str
    last_name: str
    role: str                 # "cashier" | "manager" | "owner"
    pin: str                  # 4-digit PIN (stored plain for demo; hash in production)
    email: str
    phone: str
    hire_date: str
    active: bool
    sales_total: float
    transactions_count: int

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def has_permission(self, level: str) -> bool:
        """Return True if the employee has at least the requested access level."""
        hierarchy = {"cashier": 1, "manager": 2, "owner": 3}
        return hierarchy.get(self.role, 0) >= hierarchy.get(level, 99)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role,
            "pin": self.pin,
            "email": self.email,
            "phone": self.phone,
            "hire_date": self.hire_date,
            "active": self.active,
            "sales_total": self.sales_total,
            "transactions_count": self.transactions_count,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Employee":
        return cls(
            id=data["id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            role=data["role"],
            pin=data["pin"],
            email=data["email"],
            phone=data["phone"],
            hire_date=data["hire_date"],
            active=data["active"],
            sales_total=data.get("sales_total", 0.0),
            transactions_count=data.get("transactions_count", 0),
        )
