"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day07/input.txt").read_text()

EXAMPLE_INPUT1 = """16,1,2,0,4,2,7,1,2,14"""
EXAMPLE_RESULT1 = 37


def problem_a(input_string, expected_result):
    """Problem A solved function
    """

    positions = [int(number) for number in input_string.split(',')]

    minP = min(positions)
    maxP = max(positions)
    cheapest = 1000000

    for tryP in range(minP, maxP):
        fuelCost = 0
        for index in range(len(positions)):
            fuelCost += abs(tryP - positions[index])
        if fuelCost < cheapest:
            cheapest = fuelCost


    solution = cheapest
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """

    positions = [int(number) for number in input_string.split(',')]

    minP = min(positions)
    maxP = max(positions)
    cheapest = 10000000000
    storage_dict = {}

    for tryP in range(minP, maxP):
        fuelCost = 0
        storage_dict = {}
        for index in range(len(positions)):
            steps = abs(tryP - positions[index])
            stepCost = 0
            if steps in storage_dict:
                stepCost = storage_dict[steps]
            else:
                for d in range(0, steps):
                    stepCost += d+1
                    if (d+1) not in storage_dict:
                        storage_dict[d+1] = stepCost
            fuelCost += stepCost
            storage_dict[steps] = stepCost
        if fuelCost < cheapest:
            cheapest = fuelCost
    solution = cheapest
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)
problem_b(EXAMPLE_INPUT1, 168)
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")
