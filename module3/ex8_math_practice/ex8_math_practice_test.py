import re
from ex8_math_practice import create_math_problems, solve_math_problems


def test_create_math_problems(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    f = d / 'test-problems.txt'
    create_math_problems(f)


def test_solve_problems_from_file(capsys, tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    f = d / 'test-problems.txt'
    create_math_problems(f)
    solve_math_problems(f)
    captured_out, captured_err = capsys.readouterr()
    assert len(captured_out.split('\n')) == 101


def test_correct_solved_problems(capsys, tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    with open(d / 'test-problems.txt', 'w') as file:
        file.write(
            '[  1]   19 - (   1) - (   4) + (  28) = ______\n'
            '[  2]  -18 + (   8) - (  16) - (   2) = ______\n'
            '[  3]   -8 + (  17) - (  15) + ( -29) = ______\n'
            '[  4]  -31 - ( -12) - (  -5) + ( -26) = ______\n'
            '[  5]  -15 - (  12) - (  14) - (  31) = ______\n'
        )

    answer = '[  1]   19 - (   1) - (   4) + (  28) = 42\n' \
             '[  2]  -18 + (   8) - (  16) - (   2) = -28\n' \
             '[  3]   -8 + (  17) - (  15) + ( -29) = -35\n' \
             '[  4]  -31 - ( -12) - (  -5) + ( -26) = -40\n' \
             '[  5]  -15 - (  12) - (  14) - (  31) = -72\n'

    solve_math_problems(d / 'test-problems.txt')
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == answer


def check_pattern(lines, regex_string):
    pattern = re.compile(regex_string)
    for line in lines:
        assert pattern.match(line) is not None


def test_perfect_format(capsys, tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()
    f = d / 'test-problems.txt'
    create_math_problems(f)
    solve_math_problems(f)
    captured_out, captured_err = capsys.readouterr()

    with open(d / 'test-problems.txt', 'r') as file:
        check_pattern(file, r'^\[[ \d]{3}\][- \d]{6}(?:[+-] \([- \d]{4}\) ){3}= ______$')

    check_pattern(captured_out.split('\n')[:-1], r'^\[[ \d]{3}\][- \d]{6}(?:[+-] \([- \d]{4}\) ){3}= -?\d+$')
