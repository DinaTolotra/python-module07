from ex0 import Creature, CreatureFactory, FlameFactory, AquaFactory


def test_factory_creature_creation(factory: CreatureFactory) -> None:
    base_creature: Creature = factory.create_base()
    evolved_creature: Creature = factory.create_evolved()
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def test_base_creature_battle(factory_1: CreatureFactory,
                              factory_2: CreatureFactory) -> None:
    creature_1: Creature = factory_1.create_base()
    creature_2: Creature = factory_2.create_base()
    print(creature_1.describe())
    print(" vs")
    print(creature_2.describe())
    print(creature_1.attack())
    print(creature_2.attack())


if __name__ == "__main__":
    flame_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()

    print("Testing factory")
    test_factory_creature_creation(flame_factory)

    print("\nTesting factory")
    test_factory_creature_creation(aqua_factory)

    print("\nTesting battle")
    test_base_creature_battle(flame_factory, aqua_factory)
