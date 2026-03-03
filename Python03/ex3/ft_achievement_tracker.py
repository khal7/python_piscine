

def fun() -> None:

    print("=== Achievement Tracker System ===\n")

    alice_achievements = {'first_kill', 'level_10',
                          'treasure_hunter', 'speed_demon'}
    bob_achievements = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_achievements = {'level_10', 'treasure_hunter',
                            'boss_slayer', 'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    combined_sets = set.union(alice_achievements,
                              bob_achievements, charlie_achievements)
    print("\n=== Achievement Analytics ===")

    print(f"All uniqe achievements: {combined_sets}")
    print(f"Total unique achievements: {len(combined_sets)}\n")

    print(
        f"Common to all players: {alice_achievements.intersection(bob_achievements, charlie_achievements)}")

    alice = alice_achievements.difference(
        charlie_achievements, bob_achievements)
    bob = bob_achievements.difference(alice_achievements, charlie_achievements)
    charle = charlie_achievements.difference(
        alice_achievements, bob_achievements)
    print(
        f"Rare achievments (1 player): {set.union(alice, bob, charle)}")
    print(
        f"\nAlice vs Bob common: {alice_achievements.intersection(bob_achievements)}")
    print(
        f"Alice unique: {alice_achievements.difference(bob_achievements)}")
    print(f"Bon unique: {bob_achievements.difference(alice_achievements)}")


if __name__ == "__main__":
    fun()
