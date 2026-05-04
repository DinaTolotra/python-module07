from ex0 import Creature, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import StrategyError
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy


def battle(
    participant_1: tuple[Creature, BattleStrategy],
    participant_2: tuple[Creature, BattleStrategy]
) -> bool:
    print("\n* Battle *")
    print(participant_1[0].describe())
    print(" vs")
    print(participant_2[0].describe())
    print(" now fight!")
    try:
        participant_1[1].act(participant_1[0])
        participant_2[1].act(participant_2[0])
    except StrategyError as error:
        print("Battle error, aborting tournament:", error)
        return False
    return True


def arrange_battle(
    creature_set: list[tuple[Creature, BattleStrategy]]
) -> None:
    participant_1: tuple[Creature, BattleStrategy]
    participant_2: tuple[Creature, BattleStrategy]

    print("*** Tournament ***")
    print(len(creature_set), " opponents involved")
    for i in range(len(creature_set)):
        participant_1 = creature_set[i]
        for j in range(i + 1, len(creature_set)):
            participant_2 = creature_set[j]
            if not battle(participant_1, participant_2):
                return


def print_creature_set(
    creature_set: list[tuple[Creature, BattleStrategy]]
) -> None:
    participant: tuple[Creature, BattleStrategy]
    print(" [ ", end="")
    for i in range(len(creature_set)):
        participant = creature_set[i]
        print(
            f"({participant[0].get_name()}+",
            f"{participant[1].get_name()})",
            sep="",
            end=""
        )
        if i < len(creature_set) - 1:
            print(", ", end="")
    print(" ]")


if __name__ == "__main__":
    flame_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()

    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    transfo_factory: TransformCreatureFactory = TransformCreatureFactory()

    normal_strategy: NormalStrategy = NormalStrategy()
    aggressive_strategy: AggressiveStrategy = AggressiveStrategy()
    defensive_strategy: DefensiveStrategy = DefensiveStrategy()

    creature_set_0: list[tuple[Creature, BattleStrategy]] = list()
    creature_set_1: list[tuple[Creature, BattleStrategy]] = list()
    creature_set_2: list[tuple[Creature, BattleStrategy]] = list()

    creature_set_0.append((flame_factory.create_base(), normal_strategy))
    creature_set_0.append((healing_factory.create_base(), defensive_strategy))

    creature_set_1.append((flame_factory.create_base(), aggressive_strategy))
    creature_set_1.append((healing_factory.create_base(), defensive_strategy))

    creature_set_2.append((aqua_factory.create_base(), normal_strategy))
    creature_set_2.append((healing_factory.create_base(), defensive_strategy))
    creature_set_2.append((transfo_factory.create_base(), aggressive_strategy))

    print("Tournament 0 (basic)")
    print_creature_set(creature_set_0)
    arrange_battle(creature_set_0)
    print("")

    print("Tournament 1 (error)")
    print_creature_set(creature_set_1)
    arrange_battle(creature_set_1)
    print("")

    print("Tournament 2 (multiple)")
    print_creature_set(creature_set_2)
    arrange_battle(creature_set_2)
