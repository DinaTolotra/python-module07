from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory


if __name__ == "__main__":
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    transfo_factory: TransformCreatureFactory = TransformCreatureFactory()
    heal_base_creature = healing_factory.create_base()
    heal_evolved_creature = healing_factory.create_evolved()
    transfo_base_creature = transfo_factory.create_base()
    transfo_evolved_creature = transfo_factory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    print(heal_base_creature.describe())
    print(heal_base_creature.attack())
    print(heal_base_creature.heal())
    print(" evolved:")
    print(heal_evolved_creature.describe())
    print(heal_evolved_creature.attack())
    print(heal_evolved_creature.heal())
    print("")

    print("Testing Creature with transform capability")
    print(" base:")
    print(transfo_base_creature.describe())
    print(transfo_base_creature.attack())
    print(transfo_base_creature.transform())
    print(transfo_base_creature.attack())
    print(transfo_base_creature.revert())
    print(" evolved:")
    print(transfo_evolved_creature.describe())
    print(transfo_evolved_creature.attack())
    print(transfo_evolved_creature.transform())
    print(transfo_evolved_creature.attack())
    print(transfo_evolved_creature.revert())
