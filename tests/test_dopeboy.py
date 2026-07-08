"""
tests/test_dopeboy.py
---------------------
Unit tests for the DopeBoy class.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.dopeboy_caddy.dopeboy import DopeBoy, Dimension, Transaction, recommend_club, read_green


# ---------------------------------------------------------------------------
# recommend_club
# ---------------------------------------------------------------------------

class TestRecommendClub:
    def test_driver_range(self):
        assert recommend_club(300) == "Driver"

    def test_above_max_returns_driver_max(self):
        assert recommend_club(400) == "Driver (max power)"

    def test_putter_close_range(self):
        assert recommend_club(10) == "Putter"

    def test_seven_iron(self):
        # 7-Iron range: 140–175; 6-Iron starts at 150 and is checked first,
        # so use a value strictly below 6-Iron's lower bound (150).
        assert recommend_club(142) == "7-Iron"

    def test_pitching_wedge(self):
        # Pitching Wedge range: 100–130; 9-Iron (115–145) is checked first,
        # so use a value below 9-Iron's lower bound (115).
        assert recommend_club(105) == "Pitching Wedge"


# ---------------------------------------------------------------------------
# read_green
# ---------------------------------------------------------------------------

class TestReadGreen:
    def test_straight_putt(self):
        result = read_green("straight", 1.0)
        assert "straight" in result.lower()

    def test_left_break(self):
        result = read_green("left", 12.0)   # >= 10 → "heavy break"
        assert "left" in result.lower()
        assert "heavy break" in result.lower()

    def test_slight_right_break(self):
        result = read_green("right", 3.5)
        assert "slight break" in result.lower()

    def test_slope_clamped_at_100(self):
        # Should not blow up with extreme values
        result = read_green("left", 999)
        assert "100.0%" in result

    def test_slope_clamped_at_0(self):
        result = read_green("right", -5)
        assert "0.0%" in result


# ---------------------------------------------------------------------------
# DopeBoy — dimension management
# ---------------------------------------------------------------------------

class TestDopeBoyDimensions:
    def setup_method(self):
        self.db = DopeBoy(name="TestBoy", home_dimension="Prime")

    def test_home_dimension_created(self):
        assert "Prime" in self.db.list_dimensions()

    def test_add_dimension(self):
        self.db.add_dimension("Alpha", description="Test realm")
        assert "Alpha" in self.db.list_dimensions()

    def test_duplicate_dimension_raises(self):
        with pytest.raises(ValueError, match="already exists"):
            self.db.add_dimension("Prime")

    def test_unknown_dimension_raises(self):
        with pytest.raises(KeyError):
            self.db.get_dimension("Nonexistent")

    def test_deactivate_and_activate(self):
        self.db.deactivate_dimension("Prime")
        assert not self.db.get_dimension("Prime").active
        self.db.activate_dimension("Prime")
        assert self.db.get_dimension("Prime").active

    def test_list_dimensions_returns_all(self):
        self.db.add_dimension("Beta")
        self.db.add_dimension("Gamma")
        dims = self.db.list_dimensions()
        assert "Prime" in dims
        assert "Beta" in dims
        assert "Gamma" in dims


# ---------------------------------------------------------------------------
# DopeBoy — sales / ledger
# ---------------------------------------------------------------------------

class TestDopeBoyLedger:
    def setup_method(self):
        self.db = DopeBoy(name="TestBoy", home_dimension="Prime")
        self.db.add_dimension("Alpha")

    def test_sell_records_transaction(self):
        txn = self.db.sell("Prime", "product_x", 5, 20.0)
        assert isinstance(txn, Transaction)
        assert txn.total == 100.0

    def test_total_sales_zero_initially(self):
        fresh = DopeBoy(name="Fresh", home_dimension="Home")
        assert fresh.total_sales() == 0.0

    def test_total_sales_accumulates(self):
        self.db.sell("Prime", "prod_a", 3, 10.0)
        self.db.sell("Alpha", "prod_b", 2, 25.0)
        assert self.db.total_sales() == pytest.approx(80.0)

    def test_sales_by_dimension(self):
        self.db.sell("Prime", "x", 1, 50.0)
        self.db.sell("Alpha", "y", 2, 30.0)
        breakdown = self.db.sales_by_dimension()
        assert breakdown["Prime"] == pytest.approx(50.0)
        assert breakdown["Alpha"] == pytest.approx(60.0)

    def test_sell_inactive_dimension_raises(self):
        self.db.deactivate_dimension("Alpha")
        with pytest.raises(ValueError, match="inactive"):
            self.db.sell("Alpha", "prod", 1, 10.0)

    def test_sell_unknown_dimension_raises(self):
        with pytest.raises(KeyError):
            self.db.sell("Ghost", "prod", 1, 10.0)

    def test_ledger_returns_copy(self):
        self.db.sell("Prime", "z", 1, 5.0)
        ledger = self.db.ledger()
        ledger.clear()  # mutating the returned list should not affect internal state
        assert len(self.db.ledger()) == 1

    def test_transaction_str(self):
        txn = Transaction("Prime", "smoke", 4, 15.0)
        assert "Prime" in str(txn)
        assert "smoke" in str(txn)
        assert "$60.00" in str(txn)


# ---------------------------------------------------------------------------
# DopeBoy — caddy duties
# ---------------------------------------------------------------------------

class TestDopeBoyGolfCaddy:
    def setup_method(self):
        self.db = DopeBoy(name="Caddy", home_dimension="Golf")

    def test_caddy_club_contains_name(self):
        result = self.db.caddy_club(200)
        assert "Caddy" in result

    def test_caddy_green_read_contains_name(self):
        result = self.db.caddy_green_read("right", 4.0)
        assert "Caddy" in result

    def test_caddy_yardage_card_format(self):
        result = self.db.caddy_yardage_card(7, 380, "back")
        assert "Hole  7" in result
        assert "395 yds" in result  # 380 + 15 back offset

    def test_caddy_yardage_card_front(self):
        result = self.db.caddy_yardage_card(1, 400, "front")
        assert "385 yds" in result  # 400 - 15 front offset

    def test_caddy_yardage_card_unknown_pin(self):
        result = self.db.caddy_yardage_card(2, 300, "unknown")
        assert "300 yds" in result  # no offset for unknown pin


# ---------------------------------------------------------------------------
# Dunder methods
# ---------------------------------------------------------------------------

class TestDopeBoyDunders:
    def test_repr(self):
        db = DopeBoy("King", "Home")
        r = repr(db)
        assert "King" in r
        assert "total_sales" in r

    def test_str(self):
        db = DopeBoy("King", "Home")
        s = str(db)
        assert "King" in s
        assert "Home" in s
