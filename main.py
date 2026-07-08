"""
main.py
-------
Entry point — brings the DopeBoy and his Cadillac to life.
"""

from src.dopeboy_caddy import DopeBoy, Cadillac


def main() -> None:
    # ------------------------------------------------------------------
    # Set up the DopeBoy
    # ------------------------------------------------------------------
    dp = DopeBoy(name="D-Boy", home_dimension="Prime")

    # Register additional dimensions he operates in
    dp.add_dimension("Alpha",   description="The upside-down market")
    dp.add_dimension("Quantum", description="Probability-wave hustling")
    dp.add_dimension("Astral",  description="Dream-state distribution")

    print("=" * 60)
    print(f"  Introducing: {dp.name}")
    print(f"  Active dimensions: {dp.list_dimensions()}")
    print("=" * 60)

    # ------------------------------------------------------------------
    # Move product across dimensions
    # ------------------------------------------------------------------
    sales = [
        ("Prime",   "premium_blend", 10,  25.00),
        ("Alpha",   "rare_strain",    5,  75.00),
        ("Quantum", "void_dust",      8,  50.00),
        ("Astral",  "dream_wave",    12,  40.00),
    ]

    print("\n📦  Sales ledger:")
    for dim, product, qty, price in sales:
        txn = dp.sell(dim, product, qty, price)
        print(f"   {txn}")

    print(f"\n💰  Total revenue across all dimensions: ${dp.total_sales():,.2f}")

    breakdown = dp.sales_by_dimension()
    print("\n📊  Revenue by dimension:")
    for dim, rev in breakdown.items():
        print(f"   {dim:<10} ${rev:,.2f}")

    # ------------------------------------------------------------------
    # Golf caddy duties
    # ------------------------------------------------------------------
    print("\n⛳  Golf caddy duties:")
    print(f"   {dp.caddy_club(210)}")
    print(f"   {dp.caddy_club(145)}")
    print(f"   {dp.caddy_green_read('left', 6.5)}")
    print(f"   {dp.caddy_green_read('straight', 1.0)}")

    print("\n📋  Yardage card (front 4 holes):")
    holes = [(1, 420, "middle"), (2, 185, "back"), (3, 375, "front"), (4, 510, "middle")]
    for hole, dist, pin in holes:
        print(f"   {dp.caddy_yardage_card(hole, dist, pin)}")

    # ------------------------------------------------------------------
    # The Cadillac
    # ------------------------------------------------------------------
    print("\n" + "=" * 60)
    ride = Cadillac(year=1972, model="Eldorado")
    print(ride.specs())

    print("\n🔊  Audio:")
    print(f"   {ride.play('Represent — Nas')}")
    print(f"   {ride.set_volume(85)}")

    print("\n🔒  Head-unit compartment:")
    print(f"   {ride.unlock_compartment('1234')}")       # wrong code
    print(f"   {ride.unlock_compartment('0000')}")       # correct
    print(f"   {ride.store_in_compartment('Roscoe', '0000')}")  # store the piece
    print(f"   {ride.lock_compartment()}")
    print(f"   Locked? {ride.head_unit.is_locked}")

    print("\n" + str(dp))


if __name__ == "__main__":
    main()
