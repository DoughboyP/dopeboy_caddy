# dopeboy_caddy

A Python simulation of a **multidimensional DopeBoy** who hustles across parallel dimensions and moonlights as a professional **golf caddy** — all while rolling in a fully customised **Cadillac**.

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

## Project layout

```
dopeboy_caddy/
├── src/
│   └── dopeboy_caddy/
│       ├── __init__.py
│       ├── dopeboy.py      # DopeBoy class + golf-caddy helpers
│       └── cadillac.py     # Cadillac, SoundSystem, HeadUnit classes
├── tests/
│   ├── __init__.py
│   ├── test_dopeboy.py
│   └── test_cadillac.py
├── main.py                 # Entry point demo
├── requirements.txt
└── README.md
```

---

## Quick start

```bash
# Install test dependency
pip install -r requirements.txt

# Run the demo
python main.py

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
