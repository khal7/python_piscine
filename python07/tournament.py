from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def single_battle(opponents: list[tuple]) -> None:
    #print(opponents)
    display = ", ".join(f"({factory.name}+{strategy.name})" for factory, strategy in opponents) 
    print(f"[ {display} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")


    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            factory, strategy = opponents[i]
            factory1, strategy1 = opponents[j]
            
            rival = factory.create_base()
            rival1 = factory1.create_base()
    

            print(rival.describe())
            print(" vs.")
            print(rival1.describe())
            print(" now fight!")
            try:
                strategy.act(rival)
                strategy1.act(rival1)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return




if __name__ == "__main__":

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    transform_factory = TransformCreatureFactory()
    healing_factory = HealingCreatureFactory()

    normal_strategy = NormalStrategy()
    defensive_strategy = DefensiveStrategy()
    aggressive_strategy = AggressiveStrategy()

    oppenetent1 = (flame_factory, normal_strategy)
    oppenetent2 = (healing_factory, defensive_strategy)
    battle_list = [oppenetent1, oppenetent2]
    print("Tournament 0 (basic)")
    single_battle(battle_list)
    print("\nTournament 1 (error)")

    oppenetent1 = (flame_factory, aggressive_strategy)
    oppenetent2 = (healing_factory, defensive_strategy)
    battle_list = [oppenetent1, oppenetent2]
    single_battle(battle_list)
    print("\nTournament 2 (multiple)")

    oppenetent1 = [aqua_factory, normal_strategy]
    oppenetent2 = [healing_factory, defensive_strategy]
    oppenetent3 = [transform_factory, aggressive_strategy]

    single_battle([oppenetent1, oppenetent2, oppenetent3])


    #print(battle_list)

