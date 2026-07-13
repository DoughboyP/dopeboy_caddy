"""
gun_store/seed_data.py
----------------------
Initial inventory, employees, and customers for the Paseo Guns demo.

Also contains the INTERDIMENSIONAL COLLECTION — DopeBoy's personal cache of
firearms and modifications sourced from parallel dimensions (Dim. 1 – Dim. 5,
Dim-4, Void, and beyond).  These exotic pieces are catalogued in the store
computer under the "Interdimensional" category and are treated as rare /
collector-grade inventory.
"""

from __future__ import annotations

from typing import Any, Dict, List


# ---------------------------------------------------------------------------
# Firearms
# ---------------------------------------------------------------------------

FIREARMS: List[Dict[str, Any]] = [
    # ----- Glock Handguns -----
    {
        "id": "FH001", "product_type": "Firearm", "category": "Firearm",
        "name": "Glock 17 Gen5 9mm", "brand": "Glock", "model": "G17 Gen5",
        "description": "Full-size 9mm striker-fired pistol. 17+1 capacity, nDLC finish, front serrations.",
        "price": 649.99, "quantity": 8, "reorder_level": 3,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "4.49\"", "capacity": "17+1", "finish": "nDLC Black",
    },
    {
        "id": "FH002", "product_type": "Firearm", "category": "Firearm",
        "name": "Glock 19 Gen5 9mm", "brand": "Glock", "model": "G19 Gen5",
        "description": "Compact 9mm, the best-selling pistol in America. 15+1 capacity.",
        "price": 599.99, "quantity": 12, "reorder_level": 4,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "4.02\"", "capacity": "15+1", "finish": "nDLC Black",
    },
    {
        "id": "FH003", "product_type": "Firearm", "category": "Firearm",
        "name": "Glock 43X 9mm", "brand": "Glock", "model": "G43X",
        "description": "Slimline subcompact 9mm ideal for concealed carry. 10+1 capacity.",
        "price": 529.99, "quantity": 7, "reorder_level": 3,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "3.41\"", "capacity": "10+1", "finish": "nDLC Silver",
    },
    {
        "id": "FH004", "product_type": "Firearm", "category": "Firearm",
        "name": "Glock 48 9mm", "brand": "Glock", "model": "G48",
        "description": "Slimline single-stack 9mm with 4.17\" barrel. Slim yet full grip.",
        "price": 539.99, "quantity": 5, "reorder_level": 2,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "4.17\"", "capacity": "10+1", "finish": "nDLC Silver",
    },
    # ----- Sig Sauer -----
    {
        "id": "FH005", "product_type": "Firearm", "category": "Firearm",
        "name": "Sig Sauer P320 Full-Size 9mm", "brand": "Sig Sauer", "model": "P320 Full",
        "description": "Modular striker-fired pistol. U.S. Army M17 pattern. 17+1.",
        "price": 679.99, "quantity": 6, "reorder_level": 2,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "4.7\"", "capacity": "17+1", "finish": "Nitron Black",
    },
    {
        "id": "FH006", "product_type": "Firearm", "category": "Firearm",
        "name": "Sig Sauer P365 9mm", "brand": "Sig Sauer", "model": "P365",
        "description": "Micro-compact 9mm with 10+1 capacity in a sub-compact frame. Top EDC choice.",
        "price": 599.99, "quantity": 9, "reorder_level": 3,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "3.1\"", "capacity": "10+1", "finish": "Nitron Black",
    },
    # ----- S&W M&P -----
    {
        "id": "FH007", "product_type": "Firearm", "category": "Firearm",
        "name": "S&W M&P9 M2.0 Full-Size", "brand": "Smith & Wesson", "model": "M&P9 M2.0",
        "description": "Polymer-frame 9mm service pistol with aggressive grip texture and 17+1 capacity.",
        "price": 569.99, "quantity": 6, "reorder_level": 2,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "4.25\"", "capacity": "17+1", "finish": "Armornite Black",
    },
    {
        "id": "FH008", "product_type": "Firearm", "category": "Firearm",
        "name": "S&W M&P Shield Plus 9mm", "brand": "Smith & Wesson", "model": "M&P Shield Plus",
        "description": "Slim carry pistol with 13+1 capacity in a compact frame.",
        "price": 549.99, "quantity": 8, "reorder_level": 3,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "3.1\"", "capacity": "13+1", "finish": "Armornite Black",
    },
    # ----- 1911s -----
    {
        "id": "FH009", "product_type": "Firearm", "category": "Firearm",
        "name": "Springfield Armory 1911 Mil-Spec .45 ACP", "brand": "Springfield Armory", "model": "1911 Mil-Spec",
        "description": "Classic GI-pattern 1911 in .45 ACP. Parkerized finish, 7+1 capacity.",
        "price": 699.99, "quantity": 4, "reorder_level": 2,
        "firearm_type": "Handgun", "caliber": ".45 ACP", "action": "Semi-Auto Single-Action",
        "barrel_length": "5.0\"", "capacity": "7+1", "finish": "Parkerized",
    },
    {
        "id": "FH010", "product_type": "Firearm", "category": "Firearm",
        "name": "Kimber Custom II 1911 .45 ACP", "brand": "Kimber", "model": "Custom II",
        "description": "Premium American 1911 with match-grade barrel, aluminum frame.",
        "price": 939.99, "quantity": 3, "reorder_level": 1,
        "firearm_type": "Handgun", "caliber": ".45 ACP", "action": "Semi-Auto Single-Action",
        "barrel_length": "5.0\"", "capacity": "7+1", "finish": "Satin Silver",
    },
    # ----- Revolvers -----
    {
        "id": "FH011", "product_type": "Firearm", "category": "Firearm",
        "name": "S&W 686 .357 Mag 4\"", "brand": "Smith & Wesson", "model": "686",
        "description": "L-Frame stainless revolver chambered in .357 Magnum / .38 Special. 6-shot.",
        "price": 849.99, "quantity": 3, "reorder_level": 1,
        "firearm_type": "Handgun", "caliber": ".357 Mag / .38 Special", "action": "DA/SA Revolver",
        "barrel_length": "4.0\"", "capacity": "6", "finish": "Stainless",
    },
    {
        "id": "FH012", "product_type": "Firearm", "category": "Firearm",
        "name": "Ruger GP100 .357 Mag 4\"", "brand": "Ruger", "model": "GP100",
        "description": "Rugged double-action revolver in .357 Mag. Known for durability.",
        "price": 779.99, "quantity": 2, "reorder_level": 1,
        "firearm_type": "Handgun", "caliber": ".357 Mag / .38 Special", "action": "DA/SA Revolver",
        "barrel_length": "4.2\"", "capacity": "6", "finish": "Stainless",
    },
    # ----- Additional Handguns -----
    {
        "id": "FH013", "product_type": "Firearm", "category": "Firearm",
        "name": "Glock 20 10mm Auto", "brand": "Glock", "model": "G20 Gen4",
        "description": "Full-size 10mm Auto pistol. Hard-hitting power in a reliable platform. 15+1.",
        "price": 669.99, "quantity": 4, "reorder_level": 2,
        "firearm_type": "Handgun", "caliber": "10mm Auto", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "4.61\"", "capacity": "15+1", "finish": "nDLC Black",
    },
    {
        "id": "FH014", "product_type": "Firearm", "category": "Firearm",
        "name": "S&W 629 .44 Mag 6\"", "brand": "Smith & Wesson", "model": "629 Classic",
        "description": "N-Frame stainless .44 Magnum revolver. 6-shot, 6\" barrel.",
        "price": 999.99, "quantity": 2, "reorder_level": 1,
        "firearm_type": "Handgun", "caliber": ".44 Mag / .44 Special", "action": "DA/SA Revolver",
        "barrel_length": "6.0\"", "capacity": "6", "finish": "Stainless",
    },
    # ----- AR-15 Rifles -----
    {
        "id": "FR001", "product_type": "Firearm", "category": "Firearm",
        "name": "Aero Precision M4E1 AR-15 5.56 NATO", "brand": "Aero Precision", "model": "M4E1",
        "description": "Mid-length gas system, 16\" barrel, M-LOK handguard. Enhanced upper/lower receiver set.",
        "price": 899.99, "quantity": 5, "reorder_level": 2,
        "firearm_type": "Rifle", "caliber": "5.56 NATO / .223 Rem", "action": "Semi-Auto Gas-Impingement",
        "barrel_length": "16.0\"", "capacity": "30+1", "finish": "Anodized Black",
    },
    {
        "id": "FR002", "product_type": "Firearm", "category": "Firearm",
        "name": "Ruger AR-556 5.56 NATO", "brand": "Ruger", "model": "AR-556",
        "description": "Reliable budget AR-15, 16.1\" barrel, Magpul furniture, 30-rd mag included.",
        "price": 749.99, "quantity": 6, "reorder_level": 2,
        "firearm_type": "Rifle", "caliber": "5.56 NATO / .223 Rem", "action": "Semi-Auto Gas-Impingement",
        "barrel_length": "16.1\"", "capacity": "30+1", "finish": "Matte Black",
    },
    # ----- AK Rifles -----
    {
        "id": "FR003", "product_type": "Firearm", "category": "Firearm",
        "name": "PSAK-47 GF3 7.62x39", "brand": "Palmetto State Armory", "model": "PSAK-47 GF3",
        "description": "American-made AK-47 pattern rifle. 16\" barrel, forged trunnion, classic wood furniture.",
        "price": 799.99, "quantity": 5, "reorder_level": 2,
        "firearm_type": "Rifle", "caliber": "7.62x39mm", "action": "Semi-Auto Piston",
        "barrel_length": "16.0\"", "capacity": "30+1", "finish": "Blued / Wood",
    },
    {
        "id": "FR004", "product_type": "Firearm", "category": "Firearm",
        "name": "PSAK-74 5.45x39", "brand": "Palmetto State Armory", "model": "PSAK-74",
        "description": "AK-74 pattern rifle in 5.45x39mm. Polymer furniture, 30-rd mag.",
        "price": 849.99, "quantity": 3, "reorder_level": 1,
        "firearm_type": "Rifle", "caliber": "5.45x39mm", "action": "Semi-Auto Piston",
        "barrel_length": "16.25\"", "capacity": "30+1", "finish": "Plum Polymer / Blued",
    },
    # ----- Bolt-Action Rifles -----
    {
        "id": "FR005", "product_type": "Firearm", "category": "Firearm",
        "name": "Ruger American .308 Win", "brand": "Ruger", "model": "American Rifle",
        "description": "Accurate and affordable bolt-action in .308 Win. 22\" barrel, detachable box magazine.",
        "price": 529.99, "quantity": 4, "reorder_level": 2,
        "firearm_type": "Rifle", "caliber": ".308 Win / 7.62x51mm NATO", "action": "Bolt-Action",
        "barrel_length": "22.0\"", "capacity": "4+1", "finish": "Matte Black / Synthetic",
    },
    {
        "id": "FR006", "product_type": "Firearm", "category": "Firearm",
        "name": "Savage 110 Hunter .30-06 Springfield", "brand": "Savage Arms", "model": "110 Hunter",
        "description": "Classic hunting bolt-action with AccuTrigger. 22\" barrel.",
        "price": 649.99, "quantity": 3, "reorder_level": 1,
        "firearm_type": "Rifle", "caliber": ".30-06 Springfield", "action": "Bolt-Action",
        "barrel_length": "22.0\"", "capacity": "4+1", "finish": "Matte Blued / Walnut",
    },
    {
        "id": "FR007", "product_type": "Firearm", "category": "Firearm",
        "name": "Remington 700 ADL .300 Win Mag", "brand": "Remington", "model": "700 ADL",
        "description": "Long-action 700 in .300 Win Mag. 24\" barrel. Excellent long-range accuracy.",
        "price": 749.99, "quantity": 2, "reorder_level": 1,
        "firearm_type": "Rifle", "caliber": ".300 Win Mag", "action": "Bolt-Action",
        "barrel_length": "24.0\"", "capacity": "3+1", "finish": "Blued / Synthetic",
    },
    # ----- Shotguns -----
    {
        "id": "FS001", "product_type": "Firearm", "category": "Firearm",
        "name": "Mossberg 500 Tactical 12ga", "brand": "Mossberg", "model": "500 Tactical",
        "description": "Pump-action 12-gauge with 18.5\" barrel, synthetic stock, 6+1 capacity.",
        "price": 449.99, "quantity": 6, "reorder_level": 2,
        "firearm_type": "Shotgun", "caliber": "12 Gauge", "action": "Pump-Action",
        "barrel_length": "18.5\"", "capacity": "6+1", "finish": "Matte Black",
    },
    {
        "id": "FS002", "product_type": "Firearm", "category": "Firearm",
        "name": "Mossberg 590A1 12ga", "brand": "Mossberg", "model": "590A1",
        "description": "Heavy-walled pump-action. Mil-spec 590A1, 9-shot capacity, ghost ring sights.",
        "price": 649.99, "quantity": 4, "reorder_level": 2,
        "firearm_type": "Shotgun", "caliber": "12 Gauge", "action": "Pump-Action",
        "barrel_length": "20.0\"", "capacity": "9+1", "finish": "Parkerized",
    },
    {
        "id": "FS003", "product_type": "Firearm", "category": "Firearm",
        "name": "Remington 870 Express 12ga", "brand": "Remington", "model": "870 Express",
        "description": "America's all-time best-selling pump shotgun. 28\" barrel, wood stock.",
        "price": 419.99, "quantity": 5, "reorder_level": 2,
        "firearm_type": "Shotgun", "caliber": "12 Gauge", "action": "Pump-Action",
        "barrel_length": "28.0\"", "capacity": "4+1", "finish": "Blued / Hardwood",
    },
    {
        "id": "FS004", "product_type": "Firearm", "category": "Firearm",
        "name": "Benelli M4 Tactical 12ga", "brand": "Benelli", "model": "M4 Tactical",
        "description": "Semi-auto 12ga inertia-driven. USMC M1014 pattern. 18.5\" barrel, ghost ring sights.",
        "price": 1989.99, "quantity": 2, "reorder_level": 1,
        "firearm_type": "Shotgun", "caliber": "12 Gauge", "action": "Semi-Auto Inertia",
        "barrel_length": "18.5\"", "capacity": "7+1", "finish": "Matte Black",
    },
    {
        "id": "FS005", "product_type": "Firearm", "category": "Firearm",
        "name": "Mossberg 500 20ga Youth", "brand": "Mossberg", "model": "500 Youth",
        "description": "Compact pump-action 20ga for younger shooters. 22\" barrel.",
        "price": 379.99, "quantity": 3, "reorder_level": 1,
        "firearm_type": "Shotgun", "caliber": "20 Gauge", "action": "Pump-Action",
        "barrel_length": "22.0\"", "capacity": "5+1", "finish": "Matte Blue / Wood",
    },
]

# ---------------------------------------------------------------------------
# Ammunition
# ---------------------------------------------------------------------------

AMMUNITION: List[Dict[str, Any]] = [
    # 9mm
    {
        "id": "AM001", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal American Eagle 9mm 115gr FMJ (50 rds)", "brand": "Federal", "model": "AE9AP",
        "description": "50-round box of 115gr FMJ 9mm. Reliable, clean-burning range ammo.",
        "price": 18.99, "quantity": 80, "reorder_level": 20,
        "caliber": "9mm", "ammo_type": "FMJ", "grain": "115gr",
        "rounds_per_box": 50, "velocity": "1125 fps",
    },
    {
        "id": "AM002", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal HST 9mm 124gr JHP (20 rds)", "brand": "Federal", "model": "P9HST3",
        "description": "Premium 9mm hollow point for self-defense. Consistent expansion.",
        "price": 29.99, "quantity": 40, "reorder_level": 10,
        "caliber": "9mm", "ammo_type": "JHP", "grain": "124gr",
        "rounds_per_box": 20, "velocity": "1150 fps",
    },
    {
        "id": "AM003", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Speer Gold Dot 9mm 124gr +P (20 rds)", "brand": "Speer", "model": "Gold Dot +P",
        "description": "+P 9mm self-defense load with bonded core Gold Dot HP bullet.",
        "price": 34.99, "quantity": 30, "reorder_level": 10,
        "caliber": "9mm", "ammo_type": "JHP +P", "grain": "124gr",
        "rounds_per_box": 20, "velocity": "1220 fps",
    },
    # .45 ACP
    {
        "id": "AM004", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Winchester 230gr FMJ .45 ACP (50 rds)", "brand": "Winchester", "model": "USA45AVP",
        "description": "50-round box of 230gr FMJ .45 ACP range ammo.",
        "price": 34.99, "quantity": 50, "reorder_level": 15,
        "caliber": ".45 ACP", "ammo_type": "FMJ", "grain": "230gr",
        "rounds_per_box": 50, "velocity": "835 fps",
    },
    {
        "id": "AM005", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Hornady Critical Defense .45 ACP 185gr FTX (20 rds)", "brand": "Hornady", "model": "CD 45",
        "description": "Premium .45 ACP self-defense with Flex Tip bullet for reliable expansion.",
        "price": 39.99, "quantity": 25, "reorder_level": 8,
        "caliber": ".45 ACP", "ammo_type": "JHP", "grain": "185gr",
        "rounds_per_box": 20, "velocity": "1000 fps",
    },
    # .40 S&W
    {
        "id": "AM006", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal American Eagle .40 S&W 180gr FMJ (50 rds)", "brand": "Federal", "model": "AE40R1",
        "description": "50-round .40 S&W range ammo. 180gr FMJ.",
        "price": 28.99, "quantity": 40, "reorder_level": 10,
        "caliber": ".40 S&W", "ammo_type": "FMJ", "grain": "180gr",
        "rounds_per_box": 50, "velocity": "990 fps",
    },
    # .357 Mag
    {
        "id": "AM007", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Remington .357 Mag 125gr SJHP (50 rds)", "brand": "Remington", "model": "R357M2",
        "description": "50-round .357 Magnum semi-jacketed hollow point.",
        "price": 44.99, "quantity": 25, "reorder_level": 8,
        "caliber": ".357 Magnum", "ammo_type": "JHP", "grain": "125gr",
        "rounds_per_box": 50, "velocity": "1450 fps",
    },
    # .38 Special
    {
        "id": "AM008", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal .38 Special 130gr FMJ (50 rds)", "brand": "Federal", "model": "C38AP",
        "description": "50-round .38 Special FMJ range ammo.",
        "price": 34.99, "quantity": 30, "reorder_level": 10,
        "caliber": ".38 Special", "ammo_type": "FMJ", "grain": "130gr",
        "rounds_per_box": 50, "velocity": "890 fps",
    },
    # .44 Mag
    {
        "id": "AM009", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Winchester .44 Mag 240gr JHP (20 rds)", "brand": "Winchester", "model": "X44MHP2",
        "description": "20-round .44 Magnum 240gr JHP. Maximum stopping power.",
        "price": 39.99, "quantity": 20, "reorder_level": 5,
        "caliber": ".44 Magnum", "ammo_type": "JHP", "grain": "240gr",
        "rounds_per_box": 20, "velocity": "1350 fps",
    },
    # 10mm
    {
        "id": "AM010", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal American Eagle 10mm 180gr FMJ (50 rds)", "brand": "Federal", "model": "AE10A",
        "description": "50-round 10mm Auto range ammo. 180gr FMJ.",
        "price": 39.99, "quantity": 30, "reorder_level": 10,
        "caliber": "10mm Auto", "ammo_type": "FMJ", "grain": "180gr",
        "rounds_per_box": 50, "velocity": "1030 fps",
    },
    # 5.56 / .223
    {
        "id": "AM011", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal XM193 5.56 NATO 55gr FMJ (20 rds)", "brand": "Federal", "model": "XM193",
        "description": "20-round 5.56 NATO M193 spec FMJ. Mil-spec performance.",
        "price": 14.99, "quantity": 100, "reorder_level": 25,
        "caliber": "5.56 NATO / .223 Rem", "ammo_type": "FMJ", "grain": "55gr",
        "rounds_per_box": 20, "velocity": "3165 fps",
    },
    {
        "id": "AM012", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Hornady Black 5.56 NATO 75gr BTHP (20 rds)", "brand": "Hornady", "model": "Black 5.56",
        "description": "Premium 5.56 with 75gr BTHP bullet. Excellent accuracy.",
        "price": 21.99, "quantity": 50, "reorder_level": 15,
        "caliber": "5.56 NATO / .223 Rem", "ammo_type": "HP", "grain": "75gr",
        "rounds_per_box": 20, "velocity": "2790 fps",
    },
    # 7.62x39
    {
        "id": "AM013", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Wolf 7.62x39mm 122gr FMJ (20 rds)", "brand": "Wolf", "model": "7.62x39 FMJ",
        "description": "Steel-case 7.62x39mm 122gr FMJ. Reliable AK ammo at a great price.",
        "price": 12.99, "quantity": 100, "reorder_level": 30,
        "caliber": "7.62x39mm", "ammo_type": "FMJ", "grain": "122gr",
        "rounds_per_box": 20, "velocity": "2329 fps",
    },
    # .308 Win
    {
        "id": "AM014", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal Gold Medal .308 Win 168gr BTHP (20 rds)", "brand": "Federal", "model": "GM308M",
        "description": "Premium match-grade .308 Win ammo. Sierra MatchKing BTHP.",
        "price": 44.99, "quantity": 30, "reorder_level": 10,
        "caliber": ".308 Win / 7.62x51mm NATO", "ammo_type": "HP Match", "grain": "168gr",
        "rounds_per_box": 20, "velocity": "2650 fps",
    },
    # .30-06
    {
        "id": "AM015", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Winchester Super-X .30-06 Springfield 180gr PP (20 rds)", "brand": "Winchester", "model": "X30064",
        "description": "Classic .30-06 hunting load with 180gr Power Point bullet.",
        "price": 42.99, "quantity": 20, "reorder_level": 5,
        "caliber": ".30-06 Springfield", "ammo_type": "Soft Point", "grain": "180gr",
        "rounds_per_box": 20, "velocity": "2700 fps",
    },
    # .300 Win Mag
    {
        "id": "AM016", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Hornady Superformance .300 Win Mag 180gr SST (20 rds)", "brand": "Hornady", "model": "SF 300WM",
        "description": "Long-range .300 Win Mag with Super Shock Tip bullet.",
        "price": 69.99, "quantity": 15, "reorder_level": 5,
        "caliber": ".300 Win Mag", "ammo_type": "Polymer Tip", "grain": "180gr",
        "rounds_per_box": 20, "velocity": "3130 fps",
    },
    # 5.45x39
    {
        "id": "AM017", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Silver Bear 5.45x39mm 60gr FMJ (20 rds)", "brand": "Silver Bear", "model": "5.45x39 FMJ",
        "description": "Steel-case 5.45x39mm 60gr FMJ for AK-74 pattern rifles.",
        "price": 13.99, "quantity": 60, "reorder_level": 15,
        "caliber": "5.45x39mm", "ammo_type": "FMJ", "grain": "60gr",
        "rounds_per_box": 20, "velocity": "2953 fps",
    },
    # 12 Gauge
    {
        "id": "AM018", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal 12ga 00 Buckshot (5 rds)", "brand": "Federal", "model": "F127 00B",
        "description": "5-round box of 12-gauge 00 buckshot. 9-pellet load. Standard pressure.",
        "price": 9.99, "quantity": 80, "reorder_level": 20,
        "caliber": "12 Gauge", "ammo_type": "Buckshot", "grain": "00 Buck",
        "rounds_per_box": 5, "velocity": "1325 fps",
    },
    {
        "id": "AM019", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Remington 12ga Slug (5 rds)", "brand": "Remington", "model": "Slugger",
        "description": "5-round box of 12-gauge 1oz rifled slugs for deer and tactical use.",
        "price": 8.99, "quantity": 50, "reorder_level": 15,
        "caliber": "12 Gauge", "ammo_type": "Slug", "grain": "1oz Slug",
        "rounds_per_box": 5, "velocity": "1560 fps",
    },
    {
        "id": "AM020", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Winchester 12ga #8 Birdshot (25 rds)", "brand": "Winchester", "model": "AA12008",
        "description": "25-round target/sporting load of 12ga #8 birdshot.",
        "price": 14.99, "quantity": 60, "reorder_level": 15,
        "caliber": "12 Gauge", "ammo_type": "Birdshot", "grain": "#8 Shot",
        "rounds_per_box": 25, "velocity": "1200 fps",
    },
    # 20 Gauge
    {
        "id": "AM021", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Federal 20ga 3\" #3 Buckshot (5 rds)", "brand": "Federal", "model": "F209 3B",
        "description": "5-round box of 20-gauge 3\" #3 buckshot.",
        "price": 9.49, "quantity": 30, "reorder_level": 8,
        "caliber": "20 Gauge", "ammo_type": "Buckshot", "grain": "#3 Buck",
        "rounds_per_box": 5, "velocity": "1100 fps",
    },
    # .410 bore
    {
        "id": "AM022", "product_type": "Ammunition", "category": "Ammunition",
        "name": "Winchester .410 Bore 3\" #6 Shot (5 rds)", "brand": "Winchester", "model": "XU41H6",
        "description": "5-round box of .410 bore 3\" shells with #6 shot.",
        "price": 8.99, "quantity": 25, "reorder_level": 5,
        "caliber": ".410 Bore", "ammo_type": "Birdshot", "grain": "#6 Shot",
        "rounds_per_box": 5, "velocity": "1135 fps",
    },
]

# ---------------------------------------------------------------------------
# Accessories
# ---------------------------------------------------------------------------

ACCESSORIES: List[Dict[str, Any]] = [
    # Optics
    {
        "id": "AC001", "product_type": "Accessory", "category": "Accessory",
        "name": "Holosun HS507C-X2 Red Dot Sight", "brand": "Holosun", "model": "HS507C-X2",
        "description": "Solar plus battery powered micro red dot. Multi-reticle system, shake awake.",
        "price": 319.99, "quantity": 8, "reorder_level": 3,
        "accessory_type": "Optics", "compatible_with": "Pistols (Shield/RMR footprint)",
    },
    {
        "id": "AC002", "product_type": "Accessory", "category": "Accessory",
        "name": "Trijicon RMR Type 2 3.25 MOA", "brand": "Trijicon", "model": "RMR Type 2 RM06",
        "description": "The gold standard pistol red dot. Adjustable LED. RMR footprint.",
        "price": 699.99, "quantity": 5, "reorder_level": 2,
        "accessory_type": "Optics", "compatible_with": "Pistols (RMR footprint), Glock MOS",
    },
    {
        "id": "AC003", "product_type": "Accessory", "category": "Accessory",
        "name": "EOTech EXPS3 Holographic Sight", "brand": "EOTech", "model": "EXPS3-0",
        "description": "Holographic weapon sight with 68 MOA ring + 1 MOA center dot. Rifles/carbines.",
        "price": 679.99, "quantity": 4, "reorder_level": 2,
        "accessory_type": "Optics", "compatible_with": "AR-15, rifles with Picatinny/Weaver rail",
    },
    {
        "id": "AC004", "product_type": "Accessory", "category": "Accessory",
        "name": "Vortex Crossfire II 3-9x40 Rifle Scope", "brand": "Vortex", "model": "Crossfire II 3-9x40",
        "description": "Entry-level rifle scope, BDC reticle, fully multi-coated lenses.",
        "price": 179.99, "quantity": 6, "reorder_level": 2,
        "accessory_type": "Optics", "compatible_with": "Bolt-action rifles, AR-pattern rifles",
    },
    {
        "id": "AC005", "product_type": "Accessory", "category": "Accessory",
        "name": "Vortex Viper PST Gen II 5-25x50 FFP Scope", "brand": "Vortex", "model": "Viper PST Gen II",
        "description": "First focal plane long-range scope. EBR-2C MRAD reticle.",
        "price": 999.99, "quantity": 3, "reorder_level": 1,
        "accessory_type": "Optics", "compatible_with": "Long-range bolt-action rifles",
    },
    # Magazines
    {
        "id": "AC006", "product_type": "Accessory", "category": "Accessory",
        "name": "Glock OEM 9mm 17-Round Magazine", "brand": "Glock", "model": "G17 Mag 17rd",
        "description": "Factory Glock 17-round 9mm magazine. Fits G17, G19, G26, G34.",
        "price": 34.99, "quantity": 20, "reorder_level": 8,
        "accessory_type": "Magazines", "compatible_with": "Glock 9mm (G17, G19, G26, G34)",
    },
    {
        "id": "AC007", "product_type": "Accessory", "category": "Accessory",
        "name": "Magpul PMAG 30 AR/M4 Gen M3 5.56", "brand": "Magpul", "model": "PMAG 30 Gen M3",
        "description": "Industry-standard 30-round AR-15/M4 5.56 NATO polymer magazine.",
        "price": 14.99, "quantity": 40, "reorder_level": 15,
        "accessory_type": "Magazines", "compatible_with": "AR-15/M4 pattern rifles (5.56/.223)",
    },
    {
        "id": "AC008", "product_type": "Accessory", "category": "Accessory",
        "name": "Sig Sauer P320/P365 Extended 21-Round Mag 9mm", "brand": "Sig Sauer", "model": "P320/365 21rd",
        "description": "Factory extended 21-round 9mm magazine for Sig P320 and P365XL.",
        "price": 49.99, "quantity": 12, "reorder_level": 4,
        "accessory_type": "Magazines", "compatible_with": "Sig Sauer P320, P365XL",
    },
    # Holsters
    {
        "id": "AC009", "product_type": "Accessory", "category": "Accessory",
        "name": "Safariland 6378 ALS Paddle Holster (Glock 17/22)", "brand": "Safariland", "model": "6378",
        "description": "Level I retention OWB paddle holster with Automatic Locking System.",
        "price": 79.99, "quantity": 6, "reorder_level": 2,
        "accessory_type": "Holsters", "compatible_with": "Glock 17, Glock 22",
    },
    {
        "id": "AC010", "product_type": "Accessory", "category": "Accessory",
        "name": "Vedder LightTuck IWB Kydex Holster (Glock 19)", "brand": "Vedder", "model": "LightTuck G19",
        "description": "Minimal footprint IWB Kydex holster for concealed carry.",
        "price": 64.99, "quantity": 8, "reorder_level": 3,
        "accessory_type": "Holsters", "compatible_with": "Glock 19",
    },
    {
        "id": "AC011", "product_type": "Accessory", "category": "Accessory",
        "name": "Blackhawk SERPA Level 2 Duty Holster (Sig P320)", "brand": "Blackhawk", "model": "SERPA P320",
        "description": "Duty OWB holster with SERPA auto-lock and active retention.",
        "price": 54.99, "quantity": 5, "reorder_level": 2,
        "accessory_type": "Holsters", "compatible_with": "Sig Sauer P320",
    },
    # Lights and Lasers
    {
        "id": "AC012", "product_type": "Accessory", "category": "Accessory",
        "name": "Streamlight TLR-1 HL 1000 Lumen Tactical Light", "brand": "Streamlight", "model": "TLR-1 HL",
        "description": "1000-lumen rail-mount tactical light for pistols and rifles. C4 LED.",
        "price": 139.99, "quantity": 10, "reorder_level": 4,
        "accessory_type": "Lights & Lasers", "compatible_with": "Picatinny/Weaver rail firearms",
    },
    {
        "id": "AC013", "product_type": "Accessory", "category": "Accessory",
        "name": "SureFire X300U-A 1000 Lumen Weapon Light", "brand": "SureFire", "model": "X300U-A",
        "description": "Premium 1000-lumen weapon light. DualLock mounting system.",
        "price": 299.99, "quantity": 6, "reorder_level": 2,
        "accessory_type": "Lights & Lasers", "compatible_with": "Picatinny/Weaver rail firearms",
    },
    {
        "id": "AC014", "product_type": "Accessory", "category": "Accessory",
        "name": "Crimson Trace CMR-206 Rail Master Red Laser", "brand": "Crimson Trace", "model": "CMR-206",
        "description": "Universal rail mount red laser sight. Instant-on activation.",
        "price": 99.99, "quantity": 8, "reorder_level": 3,
        "accessory_type": "Lights & Lasers", "compatible_with": "Rail-equipped pistols and rifles",
    },
    # Slings
    {
        "id": "AC015", "product_type": "Accessory", "category": "Accessory",
        "name": "Magpul MS1 Padded Sling", "brand": "Magpul", "model": "MAG1001",
        "description": "Multi-mission single/two-point sling with padded section.",
        "price": 49.99, "quantity": 12, "reorder_level": 4,
        "accessory_type": "Slings", "compatible_with": "AR-15/M4 and other long guns with QD/loops",
    },
    {
        "id": "AC016", "product_type": "Accessory", "category": "Accessory",
        "name": "Viking Tactics VTAC Padded 2-Point Sling", "brand": "Viking Tactics", "model": "VTAC MK2",
        "description": "Industry-standard VTAC sling. Fast adjustment, padded center section.",
        "price": 69.99, "quantity": 8, "reorder_level": 2,
        "accessory_type": "Slings", "compatible_with": "Rifles with QD sling swivels or loops",
    },
    # Cleaning & Maintenance
    {
        "id": "AC017", "product_type": "Accessory", "category": "Accessory",
        "name": "Otis 9mm Pistol Cleaning System", "brand": "Otis", "model": "FG-9000-9",
        "description": "Complete 9mm pistol cleaning kit in reusable case. B.O.R.E. Tech.",
        "price": 29.99, "quantity": 15, "reorder_level": 5,
        "accessory_type": "Cleaning & Maintenance", "compatible_with": "9mm pistols",
    },
    {
        "id": "AC018", "product_type": "Accessory", "category": "Accessory",
        "name": "Real Avid Gun Boss Pro Universal Cleaning Kit", "brand": "Real Avid", "model": "AVGBPRO",
        "description": "Universal cleaning kit for pistols, rifles, and shotguns. 65-piece set.",
        "price": 49.99, "quantity": 10, "reorder_level": 3,
        "accessory_type": "Cleaning & Maintenance", "compatible_with": "Universal — pistols, rifles, shotguns",
    },
    {
        "id": "AC019", "product_type": "Accessory", "category": "Accessory",
        "name": "Hoppe's No. 9 Gun Bore Cleaner 4oz", "brand": "Hoppe's", "model": "No. 9 4oz",
        "description": "The classic gun bore cleaner. Removes fouling, rust, and residue.",
        "price": 8.99, "quantity": 30, "reorder_level": 10,
        "accessory_type": "Cleaning & Maintenance", "compatible_with": "All firearms",
    },
    {
        "id": "AC020", "product_type": "Accessory", "category": "Accessory",
        "name": "Ballistol Multi-Purpose Oil 6oz", "brand": "Ballistol", "model": "120069",
        "description": "Lubricant, cleaner, preservative in one. Safe on wood, polymer, and metal.",
        "price": 12.99, "quantity": 25, "reorder_level": 8,
        "accessory_type": "Cleaning & Maintenance", "compatible_with": "All firearms",
    },
]

# ---------------------------------------------------------------------------
# Modifications
# ---------------------------------------------------------------------------

MODIFICATIONS: List[Dict[str, Any]] = [
    # Triggers
    {
        "id": "MO001", "product_type": "Modification", "category": "Modification",
        "name": "Apex Tactical Action Enhancement Trigger Kit (Glock)", "brand": "Apex Tactical", "model": "AEK Glock",
        "description": "Drop-in enhanced Glock trigger. Smooth flat-face trigger, reduced pre-travel.",
        "price": 119.99, "quantity": 10, "reorder_level": 3,
        "mod_type": "Triggers", "compatible_with": "Glock Gen 3/4/5", "installation_required": False,
    },
    {
        "id": "MO002", "product_type": "Modification", "category": "Modification",
        "name": "Geissele Super Dynamic Enhanced (SD-E) Trigger AR-15", "brand": "Geissele", "model": "SD-E",
        "description": "Two-stage AR-15 trigger. Crisp break, minimal reset. Competition grade.",
        "price": 249.99, "quantity": 6, "reorder_level": 2,
        "mod_type": "Triggers", "compatible_with": "AR-15/M4 (Mil-Spec lower)", "installation_required": True,
    },
    {
        "id": "MO003", "product_type": "Modification", "category": "Modification",
        "name": "Timney Alpha Competition Trigger (Remington 700)", "brand": "Timney", "model": "Alpha 700",
        "description": "Adjustable single-stage trigger for Remington 700. 1.5–4 lb pull range.",
        "price": 199.99, "quantity": 4, "reorder_level": 1,
        "mod_type": "Triggers", "compatible_with": "Remington 700 bolt-action", "installation_required": True,
    },
    {
        "id": "MO004", "product_type": "Modification", "category": "Modification",
        "name": "Wilson Combat Glock Match Grade Trigger Kit", "brand": "Wilson Combat", "model": "WC Glock Trigger",
        "description": "Premium drop-in Glock trigger kit. Polished internals, reduced takeup.",
        "price": 149.99, "quantity": 8, "reorder_level": 3,
        "mod_type": "Triggers", "compatible_with": "Glock Gen 3/4/5", "installation_required": False,
    },
    # Barrels
    {
        "id": "MO005", "product_type": "Modification", "category": "Modification",
        "name": "Agency Arms Glock 19 Match Grade Threaded Barrel", "brand": "Agency Arms", "model": "G19 TB",
        "description": "Stainless match-grade threaded barrel for Glock 19. 1/2x28 threads.",
        "price": 239.99, "quantity": 5, "reorder_level": 2,
        "mod_type": "Barrels", "compatible_with": "Glock 19 Gen 3/4/5", "installation_required": False,
    },
    {
        "id": "MO006", "product_type": "Modification", "category": "Modification",
        "name": "SLR Rifleworks Ion 16\" 5.56 Barrel", "brand": "SLR Rifleworks", "model": "Ion 16 5.56",
        "description": "Mid-length gas, 5.56 NATO, 1:8 twist, QPQ finish. Top-tier AR barrel.",
        "price": 249.99, "quantity": 4, "reorder_level": 1,
        "mod_type": "Barrels", "compatible_with": "AR-15 (direct impingement, mil-spec extension)", "installation_required": True,
    },
    {
        "id": "MO007", "product_type": "Modification", "category": "Modification",
        "name": "Walther Arms Glock 17 Match Barrel", "brand": "Walther Arms", "model": "G17 Match",
        "description": "Polygonal match-grade barrel for Glock 17. Improved accuracy.",
        "price": 159.99, "quantity": 6, "reorder_level": 2,
        "mod_type": "Barrels", "compatible_with": "Glock 17 Gen 3/4/5", "installation_required": False,
    },
    # Slides
    {
        "id": "MO008", "product_type": "Modification", "category": "Modification",
        "name": "Agency Arms Syndicate Glock 19 Slide (RMR Cut)", "brand": "Agency Arms", "model": "Syndicate G19",
        "description": "Machined 416 stainless slide for G19. Milled for RMR/Holosun optic, front/rear serrations.",
        "price": 449.99, "quantity": 3, "reorder_level": 1,
        "mod_type": "Slides", "compatible_with": "Glock 19 Gen 3/4/5", "installation_required": False,
    },
    {
        "id": "MO009", "product_type": "Modification", "category": "Modification",
        "name": "Zev Technologies Pro Compensated Slide (Glock 17)", "brand": "Zev Technologies", "model": "Pro Comp G17",
        "description": "Zev Pro slide for G17 with integrated compensator cut, optics ready.",
        "price": 529.99, "quantity": 2, "reorder_level": 1,
        "mod_type": "Slides", "compatible_with": "Glock 17 Gen 4/5", "installation_required": False,
    },
    # Stocks & Braces
    {
        "id": "MO010", "product_type": "Modification", "category": "Modification",
        "name": "Magpul MOE SL-M Carbine Stock (AR-15)", "brand": "Magpul", "model": "MOE SL-M",
        "description": "Compact carbine stock with rubber butt pad. Mil-spec tube compatible.",
        "price": 79.99, "quantity": 10, "reorder_level": 4,
        "mod_type": "Stocks & Braces", "compatible_with": "AR-15/M4 (Mil-spec buffer tube)", "installation_required": False,
    },
    {
        "id": "MO011", "product_type": "Modification", "category": "Modification",
        "name": "Magpul PRS Gen3 Precision Rifle Stock", "brand": "Magpul", "model": "PRS Gen3",
        "description": "Full adjustable precision stock with LOP and comb adjustments. Aluminum chassis.",
        "price": 249.99, "quantity": 4, "reorder_level": 1,
        "mod_type": "Stocks & Braces", "compatible_with": "AR-10, AR-15, Remington 700 LA/SA", "installation_required": False,
    },
    # Muzzle Devices
    {
        "id": "MO012", "product_type": "Modification", "category": "Modification",
        "name": "SureFire SOCOM762-RC2 Suppressor QD Mount", "brand": "SureFire", "model": "SOCOM762-RC2",
        "description": "Quick-detach suppressor adapter for SOCOM QD mounts. 7.62mm bore. NFA item.",
        "price": 189.99, "quantity": 5, "reorder_level": 2,
        "mod_type": "Muzzle Devices", "compatible_with": "7.62mm caliber rifles with 5/8x24 thread", "installation_required": True,
    },
    {
        "id": "MO013", "product_type": "Modification", "category": "Modification",
        "name": "Precision Armament AFAB Hybrid Muzzle Brake 5.56", "brand": "Precision Armament", "model": "AFAB 5.56",
        "description": "Hybrid brake/compensator for 5.56 AR-15. 1/2x28 thread.",
        "price": 89.99, "quantity": 8, "reorder_level": 3,
        "mod_type": "Muzzle Devices", "compatible_with": "5.56 AR-15 with 1/2x28 threaded barrel", "installation_required": True,
    },
    {
        "id": "MO014", "product_type": "Modification", "category": "Modification",
        "name": "Griffin Armament M4SD Flash Hider 5.56", "brand": "Griffin Armament", "model": "M4SD FH",
        "description": "Stainless steel flash hider with sound suppressor interface. 1/2x28 threads.",
        "price": 69.99, "quantity": 10, "reorder_level": 3,
        "mod_type": "Muzzle Devices", "compatible_with": "5.56 AR-15 with 1/2x28 thread", "installation_required": True,
    },
    {
        "id": "MO015", "product_type": "Modification", "category": "Modification",
        "name": "Lone Wolf Glock 19 Ported Compensator", "brand": "Lone Wolf", "model": "G19 Comp",
        "description": "Threaded-on compensator for Glock 19. Reduces muzzle flip. 1/2x28 thread.",
        "price": 59.99, "quantity": 6, "reorder_level": 2,
        "mod_type": "Muzzle Devices", "compatible_with": "Glock 19 (requires threaded barrel)", "installation_required": False,
    },
    # Rails & Mounting
    {
        "id": "MO016", "product_type": "Modification", "category": "Modification",
        "name": "LaRue Tactical LT101 QD Riser Mount (Trijicon RMR)", "brand": "LaRue Tactical", "model": "LT101 QD",
        "description": "Co-witness height riser for Trijicon RMR on Picatinny rail.",
        "price": 149.99, "quantity": 6, "reorder_level": 2,
        "mod_type": "Rails & Mounting", "compatible_with": "Trijicon RMR on Picatinny rail", "installation_required": False,
    },
    {
        "id": "MO017", "product_type": "Modification", "category": "Modification",
        "name": "Magpul M-LOK Offset Rail Section", "brand": "Magpul", "model": "M-LOK Offset",
        "description": "45-degree M-LOK to Picatinny offset rail section. For canted accessories.",
        "price": 19.99, "quantity": 15, "reorder_level": 5,
        "mod_type": "Rails & Mounting", "compatible_with": "M-LOK handguards", "installation_required": False,
    },
    # Grips & Controls
    {
        "id": "MO018", "product_type": "Modification", "category": "Modification",
        "name": "Tango Down Vickers Extended Glock Magazine Release", "brand": "Tango Down", "model": "VTMR-01",
        "description": "Extended mag release for Glock. Allows faster magazine changes.",
        "price": 19.99, "quantity": 15, "reorder_level": 5,
        "mod_type": "Grips & Controls", "compatible_with": "Glock Gen 3/4/5", "installation_required": False,
    },
    {
        "id": "MO019", "product_type": "Modification", "category": "Modification",
        "name": "Magpul MOE-K2 Pistol Grip (AR-15)", "brand": "Magpul", "model": "MOE-K2",
        "description": "Ergonomic vertical pistol grip for AR-15. Comfortable palm swell.",
        "price": 29.99, "quantity": 12, "reorder_level": 4,
        "mod_type": "Grips & Controls", "compatible_with": "AR-15/M4 (Mil-spec lower)", "installation_required": False,
    },
]

# ---------------------------------------------------------------------------
# Employees
# ---------------------------------------------------------------------------

EMPLOYEES: List[Dict[str, Any]] = [
    {
        "id": "EMP001",
        "first_name": "Carlos",
        "last_name": "Paseo",
        "role": "owner",
        "pin": "1234",
        "email": "carlos@paseo-guns.com",
        "phone": "555-100-0001",
        "hire_date": "2020-01-15",
        "active": True,
        "sales_total": 0.0,
        "transactions_count": 0,
    },
    {
        "id": "EMP002",
        "first_name": "Maria",
        "last_name": "Reyes",
        "role": "manager",
        "pin": "5678",
        "email": "maria@paseo-guns.com",
        "phone": "555-100-0002",
        "hire_date": "2021-03-10",
        "active": True,
        "sales_total": 0.0,
        "transactions_count": 0,
    },
    {
        "id": "EMP003",
        "first_name": "Diego",
        "last_name": "Vega",
        "role": "cashier",
        "pin": "4321",
        "email": "diego@paseo-guns.com",
        "phone": "555-100-0003",
        "hire_date": "2022-07-20",
        "active": True,
        "sales_total": 0.0,
        "transactions_count": 0,
    },
    {
        "id": "EMP004",
        "first_name": "Ana",
        "last_name": "Torres",
        "role": "cashier",
        "pin": "8765",
        "email": "ana@paseo-guns.com",
        "phone": "555-100-0004",
        "hire_date": "2023-02-01",
        "active": True,
        "sales_total": 0.0,
        "transactions_count": 0,
    },
]

# ---------------------------------------------------------------------------
# Demo customers
# ---------------------------------------------------------------------------

CUSTOMERS: List[Dict[str, Any]] = [
    {
        "id": "CUST001",
        "first_name": "James",
        "last_name": "Hunter",
        "email": "jhunter@email.com",
        "phone": "555-200-0001",
        "address": "123 Main St, San Antonio, TX 78201",
        "dob": "1985-04-12",
        "id_verified": True,
        "background_check_status": "approved",
        "notes": "Prefers Glock. Frequent buyer.",
        "purchase_history": [],
        "created_at": "2023-06-15",
    },
    {
        "id": "CUST002",
        "first_name": "Sandra",
        "last_name": "Wells",
        "email": "swells@email.com",
        "phone": "555-200-0002",
        "address": "456 Oak Ave, San Antonio, TX 78202",
        "dob": "1992-08-30",
        "id_verified": True,
        "background_check_status": "approved",
        "notes": "First-time buyer. Interested in CCW.",
        "purchase_history": [],
        "created_at": "2024-01-22",
    },
]

# ---------------------------------------------------------------------------
# ══════════════════════════════════════════════════════════════════════════
#  INTERDIMENSIONAL COLLECTION
#  DopeBoy's personal collection acquired across parallel dimensions.
#  Catalogued in the store computer — category: "Interdimensional"
# ══════════════════════════════════════════════════════════════════════════
# ---------------------------------------------------------------------------

# ── Firearms from other worlds ──────────────────────────────────────────────

INTERDIMENSIONAL_FIREARMS: List[Dict[str, Any]] = [

    # ---- ALPHA DIMENSION  ("The Upside-Down Market") ----
    {
        "id": "ID-FH01", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dim-2 Mirror-Forge Revolver [Dim. 2]", "brand": "Dim-2 Armory", "model": "Mirror-Forge Mk.I",
        "description": (
            "Hand-cast from inverted-market steel in the Dimension 2. "
            "The cylinder rotates counter-clockwise; rifling is left-hand spiral. "
            "Targets perceived threats before they are fired — the barrel points backward "
            "until the trigger is pulled, at which point reality flips. "
            "Includes 6 rounds of Dim-2 Hollow-Point. One-of-a-kind."
        ),
        "price": 3999.99, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Handgun", "caliber": "Dim-2 .44 Inverted Mag", "action": "DA/SA Revolver — Counter-Rotation",
        "barrel_length": "6.0\" (inverted bore)", "capacity": "6", "finish": "Mirror Chrome / Shadow Black",
    },
    {
        "id": "ID-FH02", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dim-2 Shadow AR [Dim. 2]", "brand": "Dim-2 Armory", "model": "Shadow AR-X",
        "description": (
            "Semi-automatic carbine forged in the upside-down market of the Dimension 2. "
            "Lower receiver is cast from inverted-density aluminum — lighter than air yet "
            "twice as rigid. Fires standard 5.56 but with an inverted ballistic trajectory "
            "that curves back on-target after 200 yards. M-LOK rail in mirror finish."
        ),
        "price": 4499.99, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Rifle", "caliber": "5.56 NATO (Dim-2-Trajectory)", "action": "Semi-Auto — Inverted Impingement",
        "barrel_length": "16.0\" Mirror-Bore", "capacity": "30+1", "finish": "Mirror Chrome / Matte Black",
    },
    {
        "id": "ID-FH03", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dim-2 Doppelganger 1911 [Dim. 2]", "brand": "Dim-2 Armory", "model": "Doppelganger 45",
        "description": (
            "Exact mirror-image 1911 from the Dimension 2 — ambidextrous controls are "
            "reversed: safety on the right, thumb pad on the left. "
            "Fitted with an Dim-2-steel match barrel; accuracy is identical to its Dim-1-world "
            "counterpart but the trigger breaks on the up-stroke. Rare collector piece."
        ),
        "price": 2899.99, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Handgun", "caliber": ".45 ACP (Dim-2-Cast)", "action": "Semi-Auto Single-Action — Mirrored",
        "barrel_length": "5.0\" (right-hand rifling inverted)", "capacity": "8+1", "finish": "Chrome / Void Cerakote",
    },

    # ---- QUANTUM DIMENSION  ("Probability-Wave Hustling") ----
    {
        "id": "ID-FH04", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Schrödinger's Rifle [Dim. 3]", "brand": "Dim-3 Forge", "model": "QF-1887",
        "description": (
            "Lever-action long rifle from the Dimension 3. "
            "According to Dim-3 probability mechanics, this rifle is simultaneously "
            "loaded and unloaded until the bolt is cycled — at which point the universe "
            "collapses into whichever state the operator intends. "
            "Chamber accepts both .308 Win and its quantum superposition round, Q-308. "
            "Do NOT open the action without observing the chamber first."
        ),
        "price": 6500.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Rifle", "caliber": ".308 Win / Q-308 Superposition", "action": "Lever-Action — Dim-3 Collapse",
        "barrel_length": "24.0\" Uncertainty Bore", "capacity": "∞ (probability-limited)", "finish": "Dim-3 Phase Titanium",
    },
    {
        "id": "ID-FH05", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Probability Pistol QX-9 [Dim. 3]", "brand": "Dim-3 Forge", "model": "QX-9 P-Wave",
        "description": (
            "Compact 9mm pistol engineered in the Dimension 3 using probability-wave "
            "metallurgy. The slide exists in superposition between open and closed until "
            "the shooter focuses — causing the weapon to instantly chamber or eject based "
            "on mental intent. Ships with two magazines: one loaded, one in superposition. "
            "Grip panels glow faint blue when charged."
        ),
        "price": 4200.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Handgun", "caliber": "9mm / Q-9 Wave Round", "action": "Semi-Auto Striker — P-Wave Fired",
        "barrel_length": "4.02\" Wave-Rifled", "capacity": "15+1 (observed)", "finish": "Dim-3 Blue / Matte Black",
    },
    {
        "id": "ID-FH06", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Entangled Shotgun QSG-12 [Dim. 3]", "brand": "Dim-3 Forge", "model": "QSG-12",
        "description": (
            "Pump-action 12-gauge with Dim-3-entangled barrel — linked to an identical "
            "twin weapon held somewhere in the Dimension 3. Every round fired in "
            "this dimension simultaneously fires in the entangled dimension. "
            "Accepts standard 12-gauge shells. The pump cycles both weapons at once. "
            "Folding stock, ghost ring sights with bioluminescent tritium inserts."
        ),
        "price": 5800.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Shotgun", "caliber": "12 Gauge (Entangled)", "action": "Pump-Action — Dim-3 Entangled",
        "barrel_length": "18.5\" Entangled Chrome", "capacity": "7+1 (×2 across dimensions)", "finish": "Dim-3 Phase Blue / Black",
    },

    # ---- ASTRAL DIMENSION  ("Dream-State Distribution") ----
    {
        "id": "ID-FH07", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dreamweave Sniper DS-300 [Dim. 4]", "brand": "Dim-4 Weaponworks", "model": "DS-300",
        "description": (
            "Bolt-action precision rifle from the Dimension 4, woven from solidified "
            "dream-state energy and rare Dim-4 alloy. The barrel phases through solid "
            "objects during the firing sequence, allowing the round to bypass hard cover. "
            "Chambered in .300 Win Mag with Dim-4-stabilised projectiles. "
            "Scope rail milled directly into the receiver. Ethereal cloud-pattern stock."
        ),
        "price": 7750.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Rifle", "caliber": ".300 Win Mag (Dim-4-Stabilised)", "action": "Bolt-Action — Phase-Through",
        "barrel_length": "26.0\" Phase Barrel", "capacity": "5+1", "finish": "Dim-4 Cloud White / Silver",
    },
    {
        "id": "ID-FH08", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dream-Wave Revolver DW-357 [Dim. 4]", "brand": "Dim-4 Weaponworks", "model": "DW-357",
        "description": (
            "L-Frame revolver materialised from pure dream-state energy in Dimension 4 "
            "Dimension. The cylinder is semi-transparent, revealing floating rounds held "
            "in place by Dim-4 magnetism. Fires standard .357 Mag but the muzzle flash "
            "manifests as a silent ripple of light — no report when fired in Dimension 4 "
            "Dimension. On Prime, it operates normally with standard noise."
        ),
        "price": 3200.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Handgun", "caliber": ".357 Magnum (Dim-4-Phase)", "action": "DA/SA Revolver — Dim-4 Frame",
        "barrel_length": "4.0\" Semi-Phase Steel", "capacity": "6", "finish": "Translucent Dim-4 Silver",
    },
    {
        "id": "ID-FH09", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dim-4 Combat Shotgun ACS-12 [Dim. 4]", "brand": "Dim-4 Weaponworks", "model": "ACS-12",
        "description": (
            "Semi-auto 12-gauge forged from Dim-4 dream-steel. The action cycles on "
            "intent — simply willing the next round chambers it. Compatible with standard "
            "12-gauge shells and Dim-4 Dim-5-Shot rounds (included, 5 rds). "
            "Extended tube holds 8+1. Side-folding stock phases through the shooter's "
            "shoulder for zero felt recoil when in Dim-4 mode."
        ),
        "price": 5500.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Shotgun", "caliber": "12 Gauge / Dim-4 Dim-5-Shot", "action": "Semi-Auto — Intent-Cycled",
        "barrel_length": "18.5\" Dream-Steel", "capacity": "8+1", "finish": "Dim-4 Pearl White / Ghost Grey",
    },

    # ---- VOID DIMENSION  (Between dimensions) ----
    {
        "id": "ID-FH10", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dim-5 Cannon VC-10mm [Dim. 5]", "brand": "Dim-5 Armaments", "model": "VC-10",
        "description": (
            "Full-size semi-auto pistol recovered from the inter-dimensional nexus (Dim. 5) — the "
            "space between worlds. Frame is cast from compressed dark matter, giving it "
            "a matte-black finish that absorbs all light. Fires standard 10mm Auto, but "
            "the bore is lined with Dim-5-steel for unmatched durability. "
            "The Dim-5 Cannon creates a miniature dimensional rift at the muzzle on each "
            "shot, adding unpredictable travel to every round."
        ),
        "price": 8900.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Handgun", "caliber": "10mm Auto (Dim-5-Bore)", "action": "Semi-Auto Striker — Dark Matter Frame",
        "barrel_length": "5.0\" Void-Steel Threaded", "capacity": "15+1", "finish": "Dim-5 Black — Light-Absorbing",
    },
    {
        "id": "ID-FH11", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dim-5 Rift Rifle VRR-308 [Dim. 5]", "brand": "Dim-5 Armaments", "model": "VRR-308",
        "description": (
            "Semi-auto 308 Win precision rifle from the inter-dimensional nexus (Dim. 5). "
            "The receiver is built from collapsed dark matter — it weighs only 4 lbs "
            "despite full steel internals. Each shot tears a micro-rift that adds "
            "2,000 fps to the projectile beyond the muzzle. Optics-ready with 20 MOA "
            "Picatinny rail. Night-vision compatible Void-absorb finish."
        ),
        "price": 11500.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Rifle", "caliber": ".308 Win (Dim-5-Accelerated)", "action": "Semi-Auto — Rift-Powered",
        "barrel_length": "20.0\" Dark Matter Fluted", "capacity": "10+1", "finish": "Dim-5 Black — Anti-Reflective",
    },
    {
        "id": "ID-FH12", "product_type": "Firearm", "category": "Interdimensional",
        "name": "Dim-5 Scatter Shotgun VSS-12 [Dim. 5]", "brand": "Dim-5 Armaments", "model": "VSS-12",
        "description": (
            "Bullpup 12-gauge from Dimension 5. The bolt mechanism exists partially outside "
            "this dimension — the action never jams because malfunctions are redirected "
            "into Dimension 5. Fires 12-gauge buckshot that fragments into dimensional "
            "splinters mid-flight. 12-round detachable box magazine. "
            "Integrated folding bayonet forged from Dim-5-edge alloy."
        ),
        "price": 9200.00, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Shotgun", "caliber": "12 Gauge (Dim-5-Frag)", "action": "Semi-Auto Bullpup — Dim-5-Cycled",
        "barrel_length": "14.0\" (bullpup effective 24\")", "capacity": "12", "finish": "Dim-5 Black / Dark Charcoal",
    },

    # ---- PRIME DIMENSION Exclusives (rare early DopeBoy era pieces) ----
    {
        "id": "ID-FH13", "product_type": "Firearm", "category": "Interdimensional",
        "name": "DopeBoy Prime OG 9mm [Dim. 1]", "brand": "Dim-1 Foundry", "model": "OG-9 Prime",
        "description": (
            "The original DopeBoy sidearm — the first pistol forged in Dimension 1 "
            "Dimension using early multidimensional metallurgy techniques. "
            "Full-size 9mm with hand-fitted match barrel and custom D-Boy grips in "
            "black G10. Rollmark reads 'PRIME – D-BOY EDITION'. Serial #0001. "
            "This is the benchmark all interdimensional weapons are measured against."
        ),
        "price": 14999.99, "quantity": 1, "reorder_level": 0,
        "firearm_type": "Handgun", "caliber": "9mm", "action": "Semi-Auto Striker-Fired",
        "barrel_length": "4.49\" Match-Grade", "capacity": "17+1", "finish": "Prime Black Cerakote / D-Boy G10 Grips",
    },
]

# ── Ammunition from other worlds ─────────────────────────────────────────────

INTERDIMENSIONAL_AMMO: List[Dict[str, Any]] = [
    {
        "id": "ID-AM01", "product_type": "Ammunition", "category": "Interdimensional",
        "name": "Dim-2 Inverted Hollow Point .44 (6 rds)", "brand": "Dim-2 Armory", "model": "AIHP-44",
        "description": (
            "6-round pack of Dimension 2 inverted hollow-point rounds in .44 caliber. "
            "The hollow expands inward on impact, creating an implosion effect. "
            "Stored in a mirrored steel case that reflects the shooter's intent."
        ),
        "price": 149.99, "quantity": 3, "reorder_level": 1,
        "caliber": "Dim-2 .44 Inverted Mag", "ammo_type": "Inverted HP", "grain": "250gr",
        "rounds_per_box": 6, "velocity": "1200 fps (inverted trajectory)",
    },
    {
        "id": "ID-AM02", "product_type": "Ammunition", "category": "Interdimensional",
        "name": "Dim-3 Superposition Rounds Q-308 (10 rds)", "brand": "Dim-3 Forge", "model": "Q-308",
        "description": (
            "10-round box of Dim-3 .308 rounds. Each projectile exists in two locations "
            "simultaneously until it strikes a surface — then collapses into a single "
            "impact point. Ideal for probability-based precision shooting. "
            "Glows faint blue in low light."
        ),
        "price": 299.99, "quantity": 2, "reorder_level": 1,
        "caliber": ".308 Win / Q-308 Superposition", "ammo_type": "Dim-3 HP", "grain": "175gr (observed)",
        "rounds_per_box": 10, "velocity": "2650 fps (collapsed state)",
    },
    {
        "id": "ID-AM03", "product_type": "Ammunition", "category": "Interdimensional",
        "name": "Dim-4 Dim-5-Shot 12ga (5 rds)", "brand": "Dim-4 Weaponworks", "model": "AVS-12",
        "description": (
            "5 rounds of Dim-4 Dim-5-Shot 12-gauge shells. The payload consists of "
            "solidified dream energy compressed into a slug-buckshot hybrid. "
            "Phases through the first layer of cover and detonates behind it. "
            "Non-lethal in the Dimension 4; standard lethality on Prime."
        ),
        "price": 199.99, "quantity": 2, "reorder_level": 1,
        "caliber": "12 Gauge / Dim-4 Dim-5-Shot", "ammo_type": "Phase-Slug/Buck Hybrid", "grain": "Dim-4-mass equiv. 1.5oz",
        "rounds_per_box": 5, "velocity": "1400 fps + phase boost",
    },
    {
        "id": "ID-AM04", "product_type": "Ammunition", "category": "Interdimensional",
        "name": "Void Dark-Matter 10mm (10 rds)", "brand": "Dim-5 Armaments", "model": "D5DM-10",
        "description": (
            "10 rounds of Dim-5-forged 10mm Auto. Projectiles are dark-matter jacketed — "
            "they pass through standard ballistic gelatin without slowing, then deliver "
            "full kinetic energy at the dimensional boundary of the target. "
            "Anti-reflective Void-black casing. Do not store near quantum devices."
        ),
        "price": 249.99, "quantity": 2, "reorder_level": 1,
        "caliber": "10mm Auto (Dim-5-Bore)", "ammo_type": "Dark Matter JHP", "grain": "200gr void-mass",
        "rounds_per_box": 10, "velocity": "1250 fps (Prime observation)",
    },
]

# ── Modifications from other worlds ──────────────────────────────────────────

INTERDIMENSIONAL_MODS: List[Dict[str, Any]] = [
    # Dimension 2 mods
    {
        "id": "ID-MO01", "product_type": "Modification", "category": "Interdimensional",
        "name": "Dim-2 Inverted Match Barrel — Glock 17 [Dim. 2]", "brand": "Dim-2 Armory", "model": "AIB-G17",
        "description": (
            "Match-grade Glock 17 barrel forged in the Dimension 2. Left-hand rifling "
            "provides a counter-rotational spin that compensates for Dim-1-world atmospheric "
            "interference. Tighter groupings at 25+ yards. Threaded 1/2x28. Mirror-chrome finish."
        ),
        "price": 599.99, "quantity": 2, "reorder_level": 1,
        "mod_type": "Barrels", "compatible_with": "Glock 17 Gen 3/4/5", "installation_required": False,
    },
    {
        "id": "ID-MO02", "product_type": "Modification", "category": "Interdimensional",
        "name": "Alpha Mirror Slide — Glock 19 [Dim. 2]", "brand": "Dim-2 Armory", "model": "AMS-G19",
        "description": (
            "Glock 19 replacement slide machined from Dimension 2 inverted-density steel. "
            "The optics cut is milled for Trijicon RMR/Holosun 507C. Mirror-chrome finish "
            "with Dim-2 inverted serration pattern. 40% lighter than standard."
        ),
        "price": 749.99, "quantity": 1, "reorder_level": 1,
        "mod_type": "Slides", "compatible_with": "Glock 19 Gen 3/4/5", "installation_required": False,
    },
    # Dimension 3 mods
    {
        "id": "ID-MO03", "product_type": "Modification", "category": "Interdimensional",
        "name": "Dim-3 Probability Trigger — AR-15 [Dim. 3]", "brand": "Dim-3 Forge", "model": "QPT-AR",
        "description": (
            "Drop-in AR-15 trigger group from the Dimension 3. Uses probability-wave "
            "mechanics to pre-stage the sear — the trigger break is instantaneous because "
            "the firing sequence begins at the Dim-3 level before the trigger is pulled. "
            "Effective pull weight: 2.0 lbs. Reset: imperceptible. Glows faint blue."
        ),
        "price": 899.99, "quantity": 2, "reorder_level": 1,
        "mod_type": "Triggers", "compatible_with": "AR-15/M4 (Mil-Spec lower)", "installation_required": False,
    },
    {
        "id": "ID-MO04", "product_type": "Modification", "category": "Interdimensional",
        "name": "Dim-3 Superposition Optic Mount [Dim. 3]", "brand": "Dim-3 Forge", "model": "QSOM-01",
        "description": (
            "Picatinny optic mount that maintains zero across dimensional phase shifts. "
            "Built with Dim-3-locked torque bolts — once tightened, the zero cannot "
            "change regardless of temperature, recoil, or dimensional transit. "
            "Fits any 30mm or 34mm optic. Universal Picatinny spec."
        ),
        "price": 399.99, "quantity": 3, "reorder_level": 1,
        "mod_type": "Rails & Mounting", "compatible_with": "Picatinny rail — universal (30mm/34mm)", "installation_required": False,
    },
    # Dimension 4 mods
    {
        "id": "ID-MO05", "product_type": "Modification", "category": "Interdimensional",
        "name": "Dim-4 Dream-Stock — AR-15 [Dim. 4]", "brand": "Dim-4 Weaponworks", "model": "ADS-AR",
        "description": (
            "Carbine stock woven from solidified Dim-4 dream-energy. Weighs virtually "
            "nothing yet absorbs 90% of recoil through a dimensional dampening field. "
            "Length-of-pull adjusts via mental intent. Six positions. "
            "Compatible with Mil-spec carbine buffer tubes."
        ),
        "price": 499.99, "quantity": 2, "reorder_level": 1,
        "mod_type": "Stocks & Braces", "compatible_with": "AR-15/M4 (Mil-spec buffer tube)", "installation_required": False,
    },
    {
        "id": "ID-MO06", "product_type": "Modification", "category": "Interdimensional",
        "name": "Dim-4 Phase Compensator — 9mm [Dim. 4]", "brand": "Dim-4 Weaponworks", "model": "APC-9",
        "description": (
            "Threaded compensator for 9mm pistols sourced from the Dimension 4. "
            "Ports muzzle blast into a brief Dim-4 phase pocket, eliminating muzzle "
            "flip entirely. Flash signature is a soft silver ripple rather than a fireball. "
            "1/2x28 thread. Compatible with Glock 17/19 threaded barrels."
        ),
        "price": 329.99, "quantity": 3, "reorder_level": 1,
        "mod_type": "Muzzle Devices", "compatible_with": "9mm with 1/2x28 threaded barrel", "installation_required": False,
    },
    # Void mods
    {
        "id": "ID-MO07", "product_type": "Modification", "category": "Interdimensional",
        "name": "Void-Steel Threaded Barrel — Glock 19 [Dim. 5]", "brand": "Dim-5 Armaments", "model": "VSTB-G19",
        "description": (
            "Replacement Glock 19 barrel machined from inter-dimensional Dim-5-steel. "
            "Dim-5-steel is harder than any Dim-1-world material — rated for 1,000,000+ "
            "rounds before wear. The bore absorbs residue instead of accumulating it. "
            "Threaded 1/2x28. Matte black — absorbs all light reflection."
        ),
        "price": 699.99, "quantity": 2, "reorder_level": 1,
        "mod_type": "Barrels", "compatible_with": "Glock 19 Gen 3/4/5", "installation_required": False,
    },
    {
        "id": "ID-MO08", "product_type": "Modification", "category": "Interdimensional",
        "name": "Dim-5 Rift Muzzle Brake — 5.56 [Dim. 5]", "brand": "Dim-5 Armaments", "model": "VRMB-556",
        "description": (
            "Muzzle brake machined from Dim-5-alloy. Creates a micro-dimensional rift "
            "that diverts propellant gases entirely into Dimension 5 — effectively producing "
            "zero muzzle blast or felt recoil at the shooter's position. "
            "The round still travels at full velocity to the target. 1/2x28 thread. "
            "No visible flash. Completely silent from all sides except downrange."
        ),
        "price": 849.99, "quantity": 2, "reorder_level": 1,
        "mod_type": "Muzzle Devices", "compatible_with": "5.56 AR-15 with 1/2x28 threaded barrel", "installation_required": True,
    },
    {
        "id": "ID-MO09", "product_type": "Modification", "category": "Interdimensional",
        "name": "Dim-5-Linked Dual Trigger System — AR-15 [Dim. 5]", "brand": "Dim-5 Armaments", "model": "VDTS-AR",
        "description": (
            "Two-stage AR-15 trigger group with Void-linked sear — the sear exists "
            "partially outside this dimension, making it immune to dirt, grit, or fouling. "
            "Stage 1: 1.0 lb take-up. Stage 2: 1.5 lb glass break. "
            "The trigger shoe is forged from Dim-5-edge alloy for tactile perfection."
        ),
        "price": 749.99, "quantity": 2, "reorder_level": 1,
        "mod_type": "Triggers", "compatible_with": "AR-15/M4 (Mil-Spec lower)", "installation_required": True,
    },
    # Dimension 1 collector mods
    {
        "id": "ID-MO10", "product_type": "Modification", "category": "Interdimensional",
        "name": "Dim-1 Foundry D-Boy Custom Grip Panels [Dim. 1]", "brand": "Dim-1 Foundry", "model": "DBoy-Grips",
        "description": (
            "Hand-carved G10 grip panels for 1911-pattern pistols, crafted in the "
            "Dimension 1 by DopeBoy's personal armorer. Aggressive texture on "
            "the palm swell; smooth D-Boy logo medallion inlaid at the heel. "
            "Available in Prime Black. Fit all Government/Commander 1911s."
        ),
        "price": 199.99, "quantity": 4, "reorder_level": 2,
        "mod_type": "Grips & Controls", "compatible_with": "1911 Government/Commander pattern", "installation_required": False,
    },
    {
        "id": "ID-MO11", "product_type": "Modification", "category": "Interdimensional",
        "name": "Prime Cerakote Service — Multidimensional Fade [Dim. 1]", "brand": "Dim-1 Foundry", "model": "PF-Fade",
        "description": (
            "In-house Cerakote refinishing by Dim-1 Foundry artisans. "
            "The signature Multidimensional Fade transitions from Dim-5 Black through "
            "Dim-3 Blue to Dim-4 Silver across the full length of the firearm — "
            "representing the journey through all four known dimensions. "
            "Available on any frame, slide, barrel, or complete firearm."
        ),
        "price": 449.99, "quantity": 99, "reorder_level": 99,
        "mod_type": "Grips & Controls", "compatible_with": "Any firearm — premium service item", "installation_required": True,
    },
]
