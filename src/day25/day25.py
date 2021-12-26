
"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day25/input.txt").read_text()

EXAMPLE_INPUT1 = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
EXAMPLE_RESULT1 = 58


def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    dict_storage = {}
    posY = 0

    for row in input_string.split('\n'):
        posX = 0
        for char in list(row):
            dict_storage[(posX, posY)] = char
            posX += 1
        posY += 1
    
    maxY, maxX = posY, posY #assume a square

    moves = 0
    moved = 1
    while moved > 0:
        moved = 0
        #First move '>'
        storage_copy = dict_storage.copy()
        for k, v in storage_copy.items():
            if v == '>':
                posX, posY = k[0], k[1]
                previousX = posX
                posX += 1
                if (posX, posY) not in storage_copy:
                    posX = 0
                next_char = storage_copy[(posX, posY)]
                if next_char == '.':
                    #we can move
                    dict_storage[(posX, posY)] = '>'
                    dict_storage[(previousX, posY)] = '.'
                    moved += 1
        storage_copy = dict_storage.copy()
        for key, v in storage_copy.items():
            if v == 'v':
                posX, posY = key[0], key[1]
                previousY = posY
                posY += 1
                if (posX, posY) not in storage_copy:
                    posY = 0
                next_char = storage_copy[(posX, posY)]
                if next_char == '.':
                    #we can move
                    dict_storage[(posX, posY)] = 'v'
                    dict_storage[(posX, previousY)] = '.'
                    moved += 1
        moves += 1
        # print()
        # print('After', moves)
        # for k, v in dict_storage.items():
        #     print(v, end='')
        #     if k[0] == maxX:
        #         print()

    solution = moves
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
