from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, _type: str) -> None:
        self._name = name
        self._type = _type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super(Flameling, self).__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super(Pyrodon, self).__init__("Pyrodon", "fire/flying")

    def attack(self) -> str:
        return f"{self._name} uses flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super(Aquabub, self).__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super(Torragon, self).__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"
