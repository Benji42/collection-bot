import math
from enum import Enum, auto


class Upgrades(Enum):
    ROLL_REGEN = auto()
    """Increases the regeration speed of rolls."""
    ROLL_MAX = auto()
    DAILY_BONUS = auto()
    FRAGMENT_BONUS = auto()
    WISHLIST_SIZE = auto()
    WISHLIST_RATE_BONUS = auto()
    UPGRADE_6 = auto()
    UPGRADE_7 = auto()
    UPGRADE_8 = auto()
    UPGRADE_9 = auto()


class RollGenerationRate:
    def modifier(self, level) -> int:
        return 900 - level * 60

    def formatted_modifier(self, level) -> str:
        minutes = int((self.modifier(level) / 60) % 60)
        return f"{minutes} minutes"


class RollMaximum:
    def modifier(self, level) -> int:
        return 20 + level * 3

    def formatted_modifier(self, level) -> str:
        return f"{self.modifier(level)} rolls"


class DailyBonus:
    def modifier(self, level) -> int:
        return 5 + level

    def formatted_modifier(self, level) -> str:
        return f"{self.modifier(level)}"


class FragmentBonus:
    def modifier(self, level) -> float:
        return 1 + level * 0.2

    def formatted_modifier(self, level) -> str:
        return f"{self.modifier(level)}x"


class WishlistSize:
    def modifier(self, level) -> int:
        return 7 + level

    def formatted_modifier(self, level) -> str:
        return f"{self.modifier(level)} slots"


class WishlistRateBonus:

    def modifier_as_int(self, level) -> int:
        return int((math.log(level+1, 1.62) / 3408) * 10000 + 0.5)

    def modifier(self, level) -> float:
        return self.modifier_as_int(level) / 10000

    def formatted_modifier(self, level) -> str:
        if level != 0:
            # return f"{self.modifier_as_int(level) / 100}".ljust(5, "0") + "%"
            return f"1 in {int(10000 / self.modifier_as_int(level))} rolls"
        return "1 in 20000 rolls"


class UpgradeEffects:
    upgrades: dict[Upgrades, RollGenerationRate | RollMaximum | DailyBonus | FragmentBonus | WishlistSize | WishlistRateBonus] = {
        Upgrades.ROLL_REGEN: RollGenerationRate(),
        Upgrades.ROLL_MAX: RollMaximum(),
        Upgrades.DAILY_BONUS: DailyBonus(),
        Upgrades.FRAGMENT_BONUS: FragmentBonus(),
        Upgrades.WISHLIST_SIZE: WishlistSize(),
        Upgrades.WISHLIST_RATE_BONUS: WishlistRateBonus(),
    }
