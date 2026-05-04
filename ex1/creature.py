from ex0 import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super(Sproutling, self).__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super(Bloomelle, self).__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super(Shiftling, self).__init__("Shiftling", "Normal")
        self._is_transformed: bool = False

    def attack(self) -> str:
        if self._is_transformed:
            return f"{self._name} performs a boosted strike!"
        return f"{self._name} attacks normally."

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

    def transform(self) -> str:
        if not self._is_transformed:
            self._is_transformed = True
            return f"{self._name} shifts into a sharper form!"
        return ""

    def revert(self) -> str:
        if self._is_transformed:
            self._is_transformed = False
            return f"{self._name} returns to normal."
        return ""


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super(Morphagon, self).__init__("Morphagon", "Normal/Dragon")
        self._is_transformed: bool = False

    def attack(self) -> str:
        if self._is_transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        return f"{self._name} attacks normally."

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

    def transform(self) -> str:
        if not self._is_transformed:
            self._is_transformed = True
            return f"{self._name} morphs into a dragonic battle form!"
        return ""

    def revert(self) -> str:
        if self._is_transformed:
            self._is_transformed = False
            return f"{self._name} stabilizes its form."
        return ""
