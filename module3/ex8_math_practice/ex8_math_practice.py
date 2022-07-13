import random

MIN = -40
MAX = 40
NR_LINES = 100
WIDTH = max(len(str(MIN)), len(str(MAX))) + 1


def create_math_problems(tmp_path):
    my_file = open(tmp_path, 'w')
    index = 0
    for one_line in range(NR_LINES):
        index += 1
        nr_1 = random.randint(MIN, MAX)
        nr_2 = random.randint(-40, 40)
        nr_3 = random.randint(-40, 40)
        nr_4 = random.randint(-40, 40)
        line = f"[{index:{3}}] {nr_1:{WIDTH}}" \
               f" {random.choice(['+', '-'])} ({nr_2:{WIDTH}})" \
               f" {random.choice(['+', '-'])} ({nr_3:{WIDTH}})" \
               f" {random.choice(['+', '-'])} ({nr_4:{WIDTH}}) = ______\n"
        my_file.write(line)


def solve_math_problems(tmp_path):
    with open(tmp_path, 'r') as my_file:
        for exercice in my_file:
            result = eval(exercice.split(']', 1)[1].split('=', 1)[0])
            print(f"{exercice.split('=', 1)[0]}= {result}")


if __name__ == "__main__":
    create_math_problems('exercises.txt')
    solve_math_problems('exercises.txt')
