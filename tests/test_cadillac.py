"""
tests/test_cadillac.py
-----------------------
Unit tests for the Cadillac, SoundSystem, and HeadUnit classes.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.dopeboy_caddy.cadillac import Cadillac, SoundSystem, HeadUnit


# ---------------------------------------------------------------------------
# SoundSystem
# ---------------------------------------------------------------------------

class TestSoundSystem:
    def setup_method(self):
        self.ss = SoundSystem()

    def test_play_sets_track(self):
        self.ss.play("Empire State of Mind")
        assert self.ss.current_track == "Empire State of Mind"

    def test_play_message_contains_track(self):
        msg = self.ss.play("C.R.E.A.M.")
        assert "C.R.E.A.M." in msg

    def test_stop_clears_track(self):
        self.ss.play("Shook Ones")
        self.ss.stop()
        assert self.ss.current_track is None

    def test_set_volume_clamps_high(self):
        self.ss.set_volume(200)
        assert self.ss._volume == 100

    def test_set_volume_clamps_low(self):
        self.ss.set_volume(-10)
        assert self.ss._volume == 0

    def test_set_volume_normal(self):
        self.ss.set_volume(75)
        assert self.ss._volume == 75

    def test_str_idle(self):
        assert "idle" in str(self.ss)

    def test_str_playing(self):
        self.ss.play("Illmatic")
        assert "Illmatic" in str(self.ss)


# ---------------------------------------------------------------------------
# HeadUnit
# ---------------------------------------------------------------------------

class TestHeadUnit:
    CORRECT = "0000"

    def setup_method(self):
        self.hu = HeadUnit()

    def test_compartment_locked_by_default(self):
        assert self.hu.is_locked is True

    def test_wrong_code_stays_locked(self):
        self.hu.unlock_compartment("9999", self.CORRECT)
        assert self.hu.is_locked is True

    def test_correct_code_unlocks(self):
        self.hu.unlock_compartment(self.CORRECT, self.CORRECT)
        assert self.hu.is_locked is False

    def test_lock_after_unlock(self):
        self.hu.unlock_compartment(self.CORRECT, self.CORRECT)
        self.hu.lock_compartment()
        assert self.hu.is_locked is True

    def test_store_item_when_unlocked(self):
        self.hu.unlock_compartment(self.CORRECT, self.CORRECT)
        msg = self.hu.store_item("Roscoe", self.CORRECT, self.CORRECT)
        assert "stored" in msg.lower()
        assert "Roscoe" in self.hu.contents

    def test_store_item_when_locked_fails(self):
        msg = self.hu.store_item("Roscoe", self.CORRECT, self.CORRECT)
        assert "locked" in msg.lower()

    def test_retrieve_item(self):
        self.hu.unlock_compartment(self.CORRECT, self.CORRECT)
        self.hu.store_item("Roscoe", self.CORRECT, self.CORRECT)
        msg = self.hu.retrieve_item("Roscoe", self.CORRECT, self.CORRECT)
        assert "retrieved" in msg.lower()
        assert "Roscoe" not in self.hu.contents

    def test_retrieve_missing_item(self):
        self.hu.unlock_compartment(self.CORRECT, self.CORRECT)
        msg = self.hu.retrieve_item("Phantom", self.CORRECT, self.CORRECT)
        assert "not found" in msg.lower()

    def test_contents_hidden_when_locked(self):
        self.hu.unlock_compartment(self.CORRECT, self.CORRECT)
        self.hu.store_item("Roscoe", self.CORRECT, self.CORRECT)
        self.hu.lock_compartment()
        assert self.hu.contents == []

    def test_contents_returns_copy(self):
        self.hu.unlock_compartment(self.CORRECT, self.CORRECT)
        self.hu.store_item("Roscoe", self.CORRECT, self.CORRECT)
        contents = self.hu.contents
        contents.clear()
        assert len(self.hu.contents) == 1  # internal state unchanged

    def test_str_contains_brand(self):
        assert "Alpine" in str(self.hu)

    def test_str_shows_lock_status(self):
        assert "locked" in str(self.hu)
        self.hu.unlock_compartment(self.CORRECT, self.CORRECT)
        assert "unlocked" in str(self.hu)


# ---------------------------------------------------------------------------
# Cadillac
# ---------------------------------------------------------------------------

class TestCadillac:
    def setup_method(self):
        self.car = Cadillac(year=1972, model="Eldorado")

    def test_default_specs(self):
        assert self.car.ROOF_COLOR == "gloss white"
        assert "gold spoke" in self.car.RIM_STYLE
        assert self.car.SEAT_MATERIAL == "white leather"
        assert self.car.RIM_COUNT == 4
        assert self.car.TIRE_STYLE == "whitewall"

    def test_play_delegates_to_sound_system(self):
        msg = self.car.play("Represent")
        assert "Represent" in msg

    def test_set_volume(self):
        msg = self.car.set_volume(90)
        assert "90" in msg

    def test_stop_music(self):
        self.car.play("Illmatic")
        msg = self.car.stop_music()
        assert "Illmatic" in msg

    def test_unlock_correct_code(self):
        msg = self.car.unlock_compartment("0000")
        assert "unlocked" in msg.lower()

    def test_unlock_wrong_code(self):
        msg = self.car.unlock_compartment("9999")
        assert "wrong" in msg.lower()

    def test_store_and_retrieve(self):
        self.car.unlock_compartment("0000")
        self.car.store_in_compartment("Roscoe", "0000")
        msg = self.car.retrieve_from_compartment("Roscoe", "0000")
        assert "retrieved" in msg.lower()

    def test_lock_compartment(self):
        self.car.unlock_compartment("0000")
        self.car.lock_compartment()
        assert self.car.head_unit.is_locked is True

    def test_specs_contains_key_details(self):
        specs = self.car.specs()
        assert "gloss white" in specs
        assert "gold spoke" in specs
        assert "whitewall" in specs
        assert "white leather" in specs
        assert "1972" in specs
        assert "Eldorado" in specs

    def test_repr(self):
        r = repr(self.car)
        assert "Cadillac" in r
        assert "gloss white" in r

    def test_str(self):
        s = str(self.car)
        assert "white roof" in s
        assert "gold spokes" in s
        assert "whitewall" in s
        assert "white leather" in s
