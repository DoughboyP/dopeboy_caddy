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
    dp = DopeBoy(name="D-Boy", home_dimension="3rd World")

    # Register additional dimensions he operates in
    dp.add_dimension("Alpha",   description="P")
    dp.add_dimension("Quantum", description="P")
    dp.add_dimension("Astral",  description="P")

    print("=" * 60)
    print(f"  Introducing: {dp.name}")
    print(f"  Active dimensions: {dp.list_dimensions()}")
    print("=" * 60)

    # ------------------------------------------------------------------
    # Move product in all dimensions. You keep your fair share of profit (33%) and leave me with mine
    # ------------------------------------------------------------------
    sales =  sales = [
        ("1",   "Heroin",     1,  32000.00),
        ("2",   "Cannabis",    1,  1300.00),
        ("3", "Cocaine powder",       1,  40000.00),
        ("4",  "Ecstacy pills",     1,  4000.00),
        ("5",  "Dimethyltryptamine", 1, 5000.00),
        ("6",  "Fentanyl",       1, 2000.00),
        ("7",   "Actavis, Wockhardt 16 oz.", 1,  1000.00),
        ("8",   "Ketamine",      1,  1200.00),
        ("9",   "Crack cocaine", 1,  23000.00),
        ("10",  "Mushrooms",     1,  1400.00),
        ("11",  "LSD",           1,  500.00),
        ("12",  "Nitrous Tank",       1,  300.00),
        ("13",  "Spice",         1,  4000.00),
        ("14",  "R-AD's",        1,  1000.00),
        ("15",  "MDMA",          1,  1300.00),
        ("16",  "Oxycontin",     1,  50.00),
        ("17",  "Shatter",       1,  400.00),
        ("18",  "Methamphetamine",  1, 13000.00),
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
    print(f"   {ride.play('Terrorist in da city- Husalah')}")
    print(f"   {ride.set_volume(85)}")

    print("\n🔒  Head-unit compartment:")
    print(f"   {ride.unlock_compartment('1234')}")       # wrong code
    print(f"   {ride.unlock_compartment('2432')}")       # correct
    print(f"   {ride.store_in_compartment('', '2432')}")  # store the piece
    print(f"   {ride.lock_compartment()}")
    print(f"   Locked? {ride.head_unit.is_locked}")

    print("\n" + str(dp))


if __name__ == "__main__":
    main()
