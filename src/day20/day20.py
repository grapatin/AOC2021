"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day20/input.txt").read_text()

EXAMPLE_INPUT1 = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""
EXAMPLE_RESULT1 = 35

def grow(storage_dict, translator_string, turn):
    new_storage_dict = storage_dict.copy()

    minRow = minChar = min(storage_dict)[0] - 3 - 1
    maxRow = maxChar = max(storage_dict)[0] + 3 + 1

    for row in range(minRow, maxRow):
        for ch in range(minChar, maxChar):
            posRow = row
            powChar = ch
            bin_string = ''
            for posRow_d in range(-1,2):
                for posChar_d in range (-1, 2):
                    check_pos_tuple =  (posRow + posRow_d, powChar + posChar_d)
                    if check_pos_tuple in storage_dict:
                        next_char = storage_dict[check_pos_tuple]
                    else:
                        if turn % 2 != 0:
                            if translator_string[0] == '#':
                                next_char = '.'
                            else:
                                next_char = '#'
                        else:
                            if translator_string[0] == '.':
                                next_char = '.'
                            else:
                                next_char = '#'                    
                    bin_string += next_char
            bin_string = bin_string.replace('#', '1').replace('.', '0')
            number = int(bin_string, 2)
            new_char = translator_string[number]
            new_storage_dict[(posRow, powChar)] = new_char
    storage_dict = new_storage_dict

    return storage_dict

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    translator_string = input_string.split('\n\n')[0]
    image = input_string.split('\n\n')[1]

    dict_storage = {}
    row_number = 0
    for row in image.split('\n'):
        char_number = 0
        for char in row:
            dict_storage[(row_number,char_number)] = char
            char_number += 1
        row_number += 1

    for loop in range(25):
        dict_storage = grow(dict_storage, translator_string, 1)
        dict_storage = grow(dict_storage, translator_string, 2)

    solution = 0

    for entry in dict_storage.values():
        if entry == '#':
            solution += 1

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1) 
problem_a(PROGBLEM_INPUT_TXT, 20395)  #Part 2 too low 15937
print("\n")
