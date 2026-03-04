

def list_comprehension() -> None:
    print("=== List Comprehension Examples ===")
    players = ['alice', 'bob', 'charlie', 'diana']
    scores = [2300, 1800, 2150, 2050]
    status = [True, True, True, False]

    high_score = []
    active_players = []
    averge = 0
    i = 0
    for _ in players:
        if scores[i] > 2000:
            high_score.append(players[i])
        if status[i] == True:
            active_players.append(players[i])
        averge += scores[i]
        scores[i] *= 2
        i += 1
    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {scores}")
    print(f"Active players: {active_players}")
    return i, averge / len(scores)


def dict_comprehension() -> int:
    players = {'alice': 2300, 'bob': 1300, 'charlie': 2150}

    player1 = {
        'scores': players['alice'],
        'alice_ach': {'hunter', 'killer', 'sniper', 'level_up', 'attendee'}
    }
    player2 = {'scores': players['bob'], 'bob_ach': {
        'killer', 'attendee', 'zombie_killer'}}
    player3 = {'scores': players['charlie'], 'charlie_ach': {'hunter', 'killer',
                                                             'sniper', 'level_up', 'attendee', 'attendee', 'zombie_killer', 'alumni'}}
    # len(player['alice_ach'])

    score_categ = {'high': 3, 'medium': 2, 'low': 1}
    i = 0

    for player in players:
        if players[player] >= 2300:
            score_categ['high'] = 3
        elif players[player] <= 1330:
            score_categ['low'] = 1
        else:
            score_categ['medium'] = 2

    achievement_count = {'alice': len(
        player1['alice_ach']), 'bob': len(player2['bob_ach']), 'charlie': len(player3['charlie_ach'])}
    print(f"Player scores: {players}")
    print(f"Score categories: {score_categ}")
    print(f"Achievement counts: {achievement_count}")
    best_player = max(players, key=players.get)
    best_score = max(players.values())
    achievement = len(player1['alice_ach'])
    return best_player, best_score, achievement


def set_comprehension() -> int:
    players = {'alice', 'bob', 'charlie', 'diana', 'alice'}
    print(players)
    achivements = {'first_kill', 'level_10',
                   'boss_slayer', 'first_kill', 'level_10', 'attendee', 'level_20'}
    print(achivements)
    regions = {'north', 'east', 'central', 'north', 'east'}
    print(regions)
    return (len(achivements))


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    total_players, average_score = list_comprehension()
    print("\n=== Dict Comprehension Examples ===")
    best_player, best_score, achievements = dict_comprehension()
    print("\n=== Set Comprehension Examples ===")
    unique_achiv = set_comprehension()

    print("\n=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {unique_achiv}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {best_player} ({best_score} points, {achievements} achievements)")
