


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get('power'), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get('power') >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map((lambda x: "* " + x + " *"), spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m.get("power"))
    min_power = min(mages, key=lambda m: m.get("power"))
    sum_power = sum(map(lambda m: m.get("power"), mages))

    len_mages = len(mages)
    my_dict = {'max_power': max_power.get('power'), 'min_power': min_power.get(
        'power'), 'avg_power': round(sum_power / len_mages, 2)}
    return my_dict


if __name__ == "__main__":
    my_dict1 = {'name': 'name1', 'power': 4, 'type': 'skinny'}
    my_dict2 = {'name': 'name2', 'power': 1, 'type': 'skinny'}
    my_dict3 = {'name': 'name3', 'power': 3, 'type': 'skinny'}
    my_list = [my_dict1, my_dict2, my_dict3]

    artifact = artifact_sorter(my_list)
    print(artifact)

    p_filter = power_filter(my_list, 3)    
    print(p_filter)

    transorm = spell_transformer(["hello", "how", "are", "you"])
    print(transorm)

    stats = mage_stats(my_list)
    print(stats)
