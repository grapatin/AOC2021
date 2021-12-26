"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"dayXX/input.txt").read_text()

EXAMPLE_INPUT1 = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""
EXAMPLE_RESULT1 = 12521



def problem_a(input_string, expected_result):
    """Problem A solved function
    """

    


    solution = 0

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
