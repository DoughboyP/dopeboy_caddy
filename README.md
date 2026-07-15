# dopeboy_caddy

A program of a **multidimensional DopeBoy** who hustles across parallel dimensions and moonlights as a professional **golf caddy** — all while rolling in a fully customised **Cadillac**.

Also home to **Paseo Guns** — a full Python CLI gun-store management system.

---

## Features

### DopeBoy (`src/dopeboy_caddy/dopeboy.py`)
- Operate across unlimited named **dimensions** (Prime, Alpha, Quantum, Astral, …)
- Register products and record **sales per dimension**
- Aggregate revenue with full **ledger history** and **per-dimension breakdown**
- Activate / deactivate dimensions on the fly
- Full **golf caddy** toolkit:
  - Club recommendations by yardage
  - Green-reading tips with break direction and slope percentage
  - Yardage-card generator with pin-position adjustments

### Cadillac (`src/dopeboy_caddy/cadillac.py`)
| Feature | Detail |
|---|---|
| Roof | Gloss white |
| Rims | 24-inch gold spoke × 4 |
| Seats | New white leather |
| Sound system | 12 speakers · 2 subs · 2 000 W amp |
| Head unit | Alpine 9″ touch screen |
| Hidden compartment | Code-locked panel behind the head unit |

---

## Paseo Guns — Store Management System

A fully interactive Python CLI that simulates running a physical gun store.

### Features
- **Inventory** — 115 SKUs across Firearms, Ammunition, Accessories, Modifications, and the **Interdimensional Collection** (Dim. 1–5)
- **Point of Sale** — cart system, tax calculation, receipts, payment methods
- **Customer Management** — records, background-check status, purchase history
- **Employee System** — PIN login, role-based access (Cashier / Manager / Owner)
- **Reports** — sales summary, inventory report, low-stock alerts, employee leaderboard
- **Data persistence** — JSON file, auto-seeded on first run

### Interdimensional Collection
DopeBoy's personal cache of exotic firearms and modifications sourced from parallel dimensions (Dim. 1–5) — catalogued in the store computer as rare / collector-grade inventory.

| Dimension | Theme |
|---|---|
| Dim. 1 | Prime — the original world |
| Dim. 2 | The upside-down market — mirror-forged, inverted mechanics |
| Dim. 3 | Probability-wave — quantum superposition weapons |
| Dim. 4 | Dream-state — phase-through Astral alloy |
| Dim. 5 | The inter-dimensional nexus — Void-steel, dark matter |

### Demo login credentials
| Employee | ID | PIN | Role |
|---|---|---|---|
| Carlos Paseo | EMP001 | 1234 | Owner |
| Maria Reyes | EMP002 | 5678 | Manager |
| Diego Vega | EMP003 | 4321 | Cashier |
| Ana Torres | EMP004 | 8765 | Cashier |

---

## Project layout

```
dopeboy_caddy/
├── src/
│   └── dopeboy_caddy/
│       ├── __init__.py
│       ├── dopeboy.py          # DopeBoy class + golf-caddy helpers
│       └── cadillac.py         # Cadillac, SoundSystem, HeadUnit classes
├── gun_store/
│   ├── __init__.py
│   ├── models.py               # Product, Firearm, Ammo, Accessory, Mod, Customer, Employee, Transaction
│   ├── seed_data.py            # Full inventory database (real-world + interdimensional)
│   ├── database.py             # JSON persistence layer
│   ├── store.py                # Business-logic layer
│   └── cli.py                  # Interactive CLI menus
├── tests/
│   ├── __init__.py
│   ├── test_dopeboy.py
│   └── test_cadillac.py
├── main.py                     # DopeBoy/Cadillac demo entry point
├── paseo_guns.py               # Paseo Guns store entry point
├── requirements.txt
└── README.md
```

---

## Quick start

```bash
# Install test dependency
pip install -r requirements.txt

# Run the DopeBoy demo
python main.py

# Launch the Paseo Guns store terminal
python paseo_guns.py

# Run the full test suite
python -m pytest tests/ -v
```

---

## Example output

```
============================================================
  Introducing: D-Boy
  Active dimensions: ['Prime', 'Alpha', 'Quantum', 'Astral']
============================================================

📦  Sales ledger:
   [Prime] 10x premium_blend @ $25.00 = $250.00
   [Alpha] 5x rare_strain @ $75.00 = $375.00
   ...

💰  Total revenue across all dimensions: $1,505.00

⛳  Golf caddy duties:
   Caddy D-Boy says: '3-Wood' for 210 yards.
   Caddy D-Boy reads: Breaking left with moderate break (6.5% slope). Aim ~9 inches left of the hole.

====================================================
  1996 Cadillac DeVille
====================================================
  Roof    : gloss white
  Rims    : 24-inch gold spoke (×4)
  Seats   : New white leather
  Audio   : SoundSystem(12 speakers, 2 subs, 2000W amp)
  Head unit: Alpine 9.0" | hidden compartment [locked]
====================================================
```
