"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day13/input.txt").read_text()

EXAMPLE_INPUT1 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
EXAMPLE_RESULT1 = 17

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    
    part1, part2 = input_string.split('\n\n')

    cord_storage = {}
    for row in part1.split('\n'):
        x_, y_ = row.split(',')
        typle = (int(x_), int(y_))
        cord_storage[typle] = 1

    fold_no = 0
    fold_rows = part2.split('\n')

    for row in fold_rows:
        fold_line = int(fold_rows[fold_no].split('=')[1])
        new_storage = {}
        if 'x' in fold_rows[fold_no]:
            #fold collumn
            for value in cord_storage:
                x, y = value
                if x > fold_line:
                    x = abs(x - fold_line*2)
                    new_storage[(x,y)] = 1
                else:
                    new_storage[value] = 1
        else:
            #fold row
            for value in cord_storage:
                x, y = value
                if int(y) > fold_line:
                    y = abs(y - fold_line*2)
                    new_storage[(x,y)] = 1
                else:
                    new_storage[value] = 1
        cord_storage = new_storage
        fold_no += 1

    print()
    for y in range(0, 6):
        for x in range(0,40):
            if (x,y) in cord_storage:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()

    solution = len(new_storage)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
