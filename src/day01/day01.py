"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day01/input.txt").read_text()

EXAMPLE_INPUT1 = """1"""
EXAMPLE_RESULT1 = 0

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')

    current = -1
    count = 0

    for row in rows:
        temp = int(row)
        if current > 0 and temp > current:
            count += 1
        current = temp

    solution = count

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')

    current = -1
    count = 0

    for pos in range(2, len(rows)):
        temp = int(rows[pos-2]) + int(rows[pos]) + int(rows[pos-1])
        if current > 0 and temp > current:
            count += 1
        current = temp

    solution = count

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 1665)
print("\n")

problem_b(PROGBLEM_INPUT_TXT, 1702)