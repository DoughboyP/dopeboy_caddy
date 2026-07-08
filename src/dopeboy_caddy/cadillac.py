"""
cadillac.py
-----------
Models the DopeBoy's custom Cadillac:
  - White roof
  - Gold spoke rims
  - New white leather seats
  - Premium sound system
  - Head unit with a hidden locked compartment
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


# ---------------------------------------------------------------------------
# Sub-components
# ---------------------------------------------------------------------------

@dataclass
class SoundSystem:
    """
    Premium in-car audio setup.

    Attributes:
        speakers:    number of speakers in the cabin.
        subwoofers:  number of subwoofers in the trunk.
        amplifier_watts: total amplifier output in watts.
        current_track:   title of the currently playing track.
    """
    speakers: int = 12
    subwoofers: int = 2
    amplifier_watts: int = 2000
    current_track: Optional[str] = None
    _volume: int = field(default=50, init=False, repr=False)

    def play(self, track: str) -> str:
        self.current_track = track
        return f"♪ Now playing: '{track}' at volume {self._volume} — {self.amplifier_watts}W pumping through {self.speakers} speakers + {self.subwoofers} subs."

    def set_volume(self, level: int) -> str:
        self._volume = max(0, min(level, 100))
        return f"Volume set to {self._volume}."

    def stop(self) -> str:
        track = self.current_track or "nothing"
        self.current_track = None
        return f"Stopped playing '{track}'."

    def __str__(self) -> str:
        playing = f"'{self.current_track}'" if self.current_track else "idle"
        return (
            f"SoundSystem({self.speakers} speakers, {self.subwoofers} subs, "
            f"{self.amplifier_watts}W amp) — {playing}"
        )


@dataclass
class HeadUnit:
    """
    In-dash head unit with a touch screen and a hidden locked compartment
    concealed behind the display panel.
    """
    brand: str = "Alpine"
    screen_size_inches: float = 9.0
    _compartment_locked: bool = field(default=True, init=False, repr=False)
    _compartment_contents: List[str] = field(default_factory=list, init=False, repr=False)

    # ------------------------------------------------------------------
    # Compartment access
    # ------------------------------------------------------------------

    def unlock_compartment(self, code: str, correct_code: str = "0000") -> str:
        """Unlock the hidden compartment behind the display panel."""
        if code == correct_code:
            self._compartment_locked = False
            return "🔓 Compartment unlocked."
        return "❌ Wrong code. Compartment remains locked."

    def lock_compartment(self) -> str:
        """Lock the compartment."""
        self._compartment_locked = True
        return "🔒 Compartment locked."

    def store_item(self, item: str, code: str, correct_code: str = "0000") -> str:
        """Store an item in the compartment (must be unlocked first)."""
        if self._compartment_locked:
            return "❌ Cannot store item — compartment is locked."
        if code != correct_code:
            return "❌ Wrong code."
        if item not in self._compartment_contents:
            self._compartment_contents.append(item)
        return f"'{item}' stored in compartment."

    def retrieve_item(self, item: str, code: str, correct_code: str = "0000") -> str:
        """Retrieve an item from the compartment."""
        if self._compartment_locked:
            return "❌ Compartment is locked."
        if code != correct_code:
            return "❌ Wrong code."
        if item in self._compartment_contents:
            self._compartment_contents.remove(item)
            return f"'{item}' retrieved from compartment."
        return f"'{item}' not found in compartment."

    @property
    def is_locked(self) -> bool:
        return self._compartment_locked

    @property
    def contents(self) -> List[str]:
        """Read-only list of stored items (only visible when unlocked)."""
        if self._compartment_locked:
            return []
        return list(self._compartment_contents)

    def __str__(self) -> str:
        status = "locked" if self._compartment_locked else "unlocked"
        return (
            f"{self.brand} {self.screen_size_inches}\" head unit "
            f"| hidden compartment [{status}]"
        )


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------

class Cadillac:
    """
    The DopeBoy's fully customised 1972 Cadillac Eldorado.

    Specs
    -----
    Exterior:
        - Body color : Brown
        - Roof       : Gloss white
        - Rims       : 24" gold spoke (set of 4)
        - Tires      : Whitewall
    Interior:
        - Seats      : New white leather (full cabin)
        - Audio      : Premium {SoundSystem}
        - Head unit  : {HeadUnit} with hidden locked compartment
    """

    BODY_COLOR    = "brown"
    ROOF_COLOR    = "gloss white"
    RIM_STYLE     = "24-inch gold spoke"
    RIM_COUNT     = 4
    SEAT_MATERIAL = "white leather"
    TIRE_STYLE    = "whitewall"

    def __init__(
        self,
        make: str = "Cadillac",
        model: str = "Eldorado",
        year: int = 1972,
        sound_system: Optional[SoundSystem] = None,
        head_unit: Optional[HeadUnit] = None,
    ) -> None:
        self.make  = make
        self.model = model
        self.year  = year
        self.sound_system = sound_system or SoundSystem()
        self.head_unit    = head_unit    or HeadUnit()

    # ------------------------------------------------------------------
    # Convenience pass-throughs
    # ------------------------------------------------------------------

    def play(self, track: str) -> str:
        return self.sound_system.play(track)

    def set_volume(self, level: int) -> str:
        return self.sound_system.set_volume(level)

    def stop_music(self) -> str:
        return self.sound_system.stop()

    def unlock_compartment(self, code: str, correct_code: str = "0000") -> str:
        return self.head_unit.unlock_compartment(code, correct_code)

    def lock_compartment(self) -> str:
        return self.head_unit.lock_compartment()

    def store_in_compartment(self, item: str, code: str, correct_code: str = "0000") -> str:
        return self.head_unit.store_item(item, code, correct_code)

    def retrieve_from_compartment(self, item: str, code: str, correct_code: str = "0000") -> str:
        return self.head_unit.retrieve_item(item, code, correct_code)

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def specs(self) -> str:
        """Return a formatted spec sheet for the vehicle."""
        lines = [
            f"{'='*52}",
            f"  {self.year} {self.make} {self.model}",
            f"{'='*52}",
            f"  Body color    : {self.BODY_COLOR}",
            f"  Roof          : {self.ROOF_COLOR}",
            f"  Rims          : {self.RIM_STYLE} (×{self.RIM_COUNT})",
            f"  Tires         : {self.TIRE_STYLE}",
            f"  Seats         : New {self.SEAT_MATERIAL}",
            f"  Audio         : {self.sound_system}",
            f"  Head unit     : {self.head_unit}",
            f"{'='*52}",
        ]
        return "\n".join(lines)

    def __repr__(self) -> str:
        return (
            f"Cadillac(year={self.year}, model={self.model!r}, "
            f"roof='{self.ROOF_COLOR}', rims='{self.RIM_STYLE}')"
        )

    def __str__(self) -> str:
        return f"🚗 {self.year} {self.make} {self.model} — {self.BODY_COLOR}, white roof, gold spokes, whitewall tires, white leather"
