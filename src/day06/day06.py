"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day06/input.txt").read_text()

EXAMPLE_INPUT1 = """3,4,3,1,2"""
EXAMPLE_RESULT1 = 5934

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    numbers = [int(number) for number in input_string.split(',')]

    num_copy = numbers.copy()
    times = 80

    for t in range(times):
        numbers_to_append = 0
        for pos in range(len(numbers)):
            num_copy[pos] -= 1
            if num_copy[pos] < 0:
                numbers_to_append += 1
                num_copy[pos] = 6
            
        for count in range(numbers_to_append):
            num_copy.append(8)
        numbers = num_copy.copy()
        numbers_to_append = 0

    solution = len(numbers)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)


def problem_b(input_string, expected_result):
    """Problem B solved function
    """
    numbers = [int(number) for number in input_string.split(',')]
    times = 256
    storage_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for i in range(len(numbers)):
        storage_dict[numbers[i]] += 1
    for t in range(times):
        storage_copy = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
        for entry in storage_dict:
            if entry == 0:
                storage_copy[6] += storage_dict[0]
                storage_copy[8] = storage_dict[0]
            else:
                storage_copy[entry-1] += storage_dict[entry]
        storage_dict = storage_copy.copy()

    solution = 0
    for entry in storage_dict:
        solution += storage_dict[entry]
    
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, 5934)
problem_a(PROGBLEM_INPUT_TXT, 376194)
print('\n')
problem_b(EXAMPLE_INPUT1, 26984457539)
problem_b(PROGBLEM_INPUT_TXT, 1693022481538)
print("\n")