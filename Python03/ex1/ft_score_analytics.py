import sys

print("=== Player Score Analytics ===")


def fun():
    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    my_list = sys.argv[1:]
    i = 0
    for arg in my_list:
        try:
            my_list[i] = int(arg)
            i += 1
        except ValueError:
            print(f"oops, I typed {arg} instead of 1000")
            return
    print(f"Scores processed: {my_list}")
    print(f"Total players: {len(my_list) - 1}")
    print(f"Total score: {sum(my_list)}")
    print(f"High score: {max(my_list)}")
    print(f"Low score: {min(my_list)}")
    print(f"Score range: {max(my_list) - min(my_list)}")


# my_list = {int(arg) for arg in my_list}
# print(type(my_list))
if __name__ == "__main__":
    fun()
