"""
dopeboy.py
----------
Models a DopeBoy who operates across multiple dimensions and moonlights
as a golf caddy — reading greens, tracking yardages, and recommending
clubs across every realm he inhabits.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# Supporting data structures
# ---------------------------------------------------------------------------

@dataclass
class Transaction:
    """A single sale recorded in a given dimension."""
    dimension: str
    product: str
    quantity: int
    price_per_unit: float

    @property
    def total(self) -> float:
        return self.quantity * self.price_per_unit

    def __str__(self) -> str:
        return (
            f"[{self.dimension}] {self.quantity}x {self.product} "
            f"@ ${self.price_per_unit:.2f} = ${self.total:.2f}"
        )


@dataclass
class Dimension:
    """
    A realm in which the DopeBoy operates.
    Each dimension has its own market, rules, and golf course.
    """
    name: str
    description: str = ""
    products: List[str] = field(default_factory=list)
    active: bool = True

    def add_product(self, product: str) -> None:
        if product not in self.products:
            self.products.append(product)

    def __str__(self) -> str:
        status = "ACTIVE" if self.active else "INACTIVE"
        return f"Dimension '{self.name}' [{status}] — {self.description}"


# ---------------------------------------------------------------------------
# Golf-caddy helpers
# ---------------------------------------------------------------------------

# Standard club distance ranges (yards) — longest first
CLUB_CHART: List[tuple] = [
    ("Driver",       250, 350),
    ("3-Wood",       210, 260),
    ("5-Wood",       190, 240),
    ("3-Iron",       180, 220),
    ("4-Iron",       170, 210),
    ("5-Iron",       160, 200),
    ("6-Iron",       150, 185),
    ("7-Iron",       140, 175),
    ("8-Iron",       130, 165),
    ("9-Iron",       115, 145),
    ("Pitching Wedge", 100, 130),
    ("Gap Wedge",     80, 110),
    ("Sand Wedge",    60,  90),
    ("Lob Wedge",     40,  70),
    ("Putter",         0,  40),
]


def recommend_club(distance_yards: int) -> str:
    """Return the best club recommendation for a given yardage."""
    for club, low, high in CLUB_CHART:
        if low <= distance_yards <= high:
            return club
    if distance_yards > 350:
        return "Driver (max power)"
    return "Putter"


def read_green(break_direction: str, slope_percent: float) -> str:
    """
    Produce a caddy read for a putt given break direction and slope.

    Args:
        break_direction: compass direction the putt will break toward,
                         e.g. 'left', 'right', 'straight'.
        slope_percent:   gradient as a percentage (0–100).

    Returns:
        A human-readable caddy tip.
    """
    slope_percent = max(0.0, min(slope_percent, 100.0))

    if slope_percent < 2:
        severity = "barely any break"
    elif slope_percent < 5:
        severity = "slight break"
    elif slope_percent < 10:
        severity = "moderate break"
    else:
        severity = "heavy break"

    direction = break_direction.strip().lower()
    if direction == "straight":
        return f"Putt is straight — {severity} ({slope_percent:.1f}% slope). Hit it firm."

    aim_offset = int(slope_percent * 1.5)
    return (
        f"Breaking {direction} with {severity} ({slope_percent:.1f}% slope). "
        f"Aim ~{aim_offset} inches {direction} of the hole."
    )


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------

class DopeBoy:
    """
    A multidimensional operator and elite golf caddy.

    The DopeBoy navigates multiple dimensions simultaneously — each with its
    own market and product catalogue.  Between rounds he serves as a
    professional caddy: tracking yardages, reading greens, and selecting
    the right club for every shot.
    """

    def __init__(self, name: str, home_dimension: str = "Prime") -> None:
        self.name = name
        self._dimensions: Dict[str, Dimension] = {}
        self._ledger: List[Transaction] = []

        # Always start with a home dimension
        self.add_dimension(home_dimension, description="Home base dimension")

    # ------------------------------------------------------------------
    # Dimension management
    # ------------------------------------------------------------------

    def add_dimension(
        self,
        name: str,
        description: str = "",
        products: Optional[List[str]] = None,
    ) -> Dimension:
        """Register a new dimension for operations."""
        if name in self._dimensions:
            raise ValueError(f"Dimension '{name}' already exists.")
        dim = Dimension(name=name, description=description, products=products or [])
        self._dimensions[name] = dim
        return dim

    def get_dimension(self, name: str) -> Dimension:
        if name not in self._dimensions:
            raise KeyError(f"Unknown dimension: '{name}'")
        return self._dimensions[name]

    def list_dimensions(self) -> List[str]:
        """Return names of all registered dimensions."""
        return list(self._dimensions.keys())

    def deactivate_dimension(self, name: str) -> None:
        """Mark a dimension as inactive (lay low)."""
        self.get_dimension(name).active = False

    def activate_dimension(self, name: str) -> None:
        """Reactivate a previously deactivated dimension."""
        self.get_dimension(name).active = True

    # ------------------------------------------------------------------
    # Sales / ledger
    # ------------------------------------------------------------------

    def sell(
        self,
        dimension: str,
        product: str,
        quantity: int,
        price_per_unit: float,
    ) -> Transaction:
        """
        Record a sale in the specified dimension.

        Raises:
            KeyError:   if the dimension has not been registered.
            ValueError: if the dimension is currently inactive.
        """
        dim = self.get_dimension(dimension)
        if not dim.active:
            raise ValueError(
                f"Dimension '{dimension}' is inactive — can't move product right now."
            )
        dim.add_product(product)
        txn = Transaction(
            dimension=dimension,
            product=product,
            quantity=quantity,
            price_per_unit=price_per_unit,
        )
        self._ledger.append(txn)
        return txn

    def total_sales(self) -> float:
        """Sum all revenue across every dimension."""
        return sum(t.total for t in self._ledger)

    def sales_by_dimension(self) -> Dict[str, float]:
        """Break down total revenue per dimension."""
        breakdown: Dict[str, float] = {}
        for txn in self._ledger:
            breakdown[txn.dimension] = breakdown.get(txn.dimension, 0.0) + txn.total
        return breakdown

    def ledger(self) -> List[Transaction]:
        """Return a read-only view of all recorded transactions."""
        return list(self._ledger)

    # ------------------------------------------------------------------
    # Golf caddy duties
    # ------------------------------------------------------------------

    def caddy_club(self, distance_yards: int) -> str:
        """Recommend a club for the given distance."""
        club = recommend_club(distance_yards)
        return f"Caddy {self.name} says: '{club}' for {distance_yards} yards."

    def caddy_green_read(self, break_direction: str, slope_percent: float) -> str:
        """Deliver a green-reading tip."""
        read = read_green(break_direction, slope_percent)
        return f"Caddy {self.name} reads: {read}"

    def caddy_yardage_card(self, hole: int, tee_distance: int, pin_position: str = "middle") -> str:
        """
        Produce a yardage-card entry for a given hole.

        Args:
            hole:          hole number (1–18).
            tee_distance:  total hole length in yards from the tee.
            pin_position:  'front', 'middle', or 'back'.
        """
        offsets = {"front": -15, "middle": 0, "back": 15}
        adjustment = offsets.get(pin_position.lower(), 0)
        adjusted = tee_distance + adjustment
        club = recommend_club(adjusted)
        return (
            f"Hole {hole:>2} | {tee_distance} yds (pin {pin_position}) "
            f"→ play {adjusted} yds → {club}"
        )

    # ------------------------------------------------------------------
    # Dunder helpers
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"DopeBoy(name={self.name!r}, "
            f"dimensions={len(self._dimensions)}, "
            f"total_sales=${self.total_sales():.2f})"
        )

    def __str__(self) -> str:
        dims = ", ".join(self.list_dimensions())
        return (
            f"🎱 {self.name} — operating in [{dims}] | "
            f"Total revenue: ${self.total_sales():.2f}"
        )
