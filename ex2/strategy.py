from abc import ABC, abstractmethod
from typing import Any
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    def __init__(self, name: str) -> None:
        self._name: str = name

    @abstractmethod
    def act(self, creature: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass

    def get_name(self) -> str:
        return self._name


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super(NormalStrategy, self).__init__("Normal")

    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
        else:
            raise StrategyError(
                f"Invalid Creature '{creature._name}' " +
                "for this normal strategy"
            )

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super(AggressiveStrategy, self).__init__("Aggressive")

    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise StrategyError(
                f"Invalid Creature '{creature._name}' " +
                "for this aggressive strategy"
            )

    def is_valid(self, creature: Any) -> bool:
        return (
            isinstance(creature, TransformCapability)
            and isinstance(creature, Creature)
        )


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super(DefensiveStrategy, self).__init__("Defensive")

    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise StrategyError(
                f"Invalid Creature '{creature._name}' " +
                "for this defensive strategy"
            )

    def is_valid(self, creature: Any) -> bool:
        return (
            isinstance(creature, HealCapability)
            and isinstance(creature, Creature)
        )
