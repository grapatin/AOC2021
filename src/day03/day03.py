"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day03/input.txt").read_text()

EXAMPLE_INPUT1 = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
EXAMPLE_RESULT1 = 198

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')
    count_b1 = [0] * len(rows[0])
    count_b0 = [0] * len(rows[0])
    for row in rows:
        for char_pos in range(len(row)):
            if row[char_pos] == '1':
                count_b1[char_pos] += 1
            else:
                count_b0[char_pos] += 1

    binary_gamma = ''
    binary_epsilon = ''
    for l in range(len(count_b0)):
        if count_b0[l] > count_b1[l]:
            binary_gamma = binary_gamma + '0'
            binary_epsilon = binary_epsilon + '1'
        else:
            binary_gamma = binary_gamma + '1'
            binary_epsilon = binary_epsilon + '0'

    
    b_int_gamma = int(binary_gamma, 2)
    b_int_epsilon = int(binary_epsilon, 2)
    


    solution = b_int_gamma*b_int_epsilon

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 3985686)
print("\n")


def check_if_1_is_most_common(dict, char_pos):
    count_1 = 0
    count_0 = 0
    for entry in dict:
            if dict[entry][char_pos] == '1':
                count_1 += 1
            else:
                count_0 += 1

    if (count_1 >= count_0):
        return True
    else:
        return False
  

def remove_entries(dict, pos, char):
    copy_dict = dict.copy()

    for dict_key in dict:
        if dict[dict_key][pos] != char:
            del copy_dict[dict_key]

    return copy_dict

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')
    storage_dict = {}
    for row_c in range(len(rows)):
        storage_dict[row_c] = rows[row_c]

    storage_oxy = storage_dict.copy()
    storage_co2 = storage_dict.copy()

    length = len(rows[0])

    pos = 0
    while (len(storage_oxy) > 1):
        if (check_if_1_is_most_common(storage_oxy, pos % length)):
            storage_oxy = remove_entries(storage_oxy, pos, '1')
        else:
            storage_oxy = remove_entries(storage_oxy, pos, '0')
        pos += 1

            
    pos = 0
    while (len(storage_co2) > 1):
        if (check_if_1_is_most_common(storage_co2, pos % length)):
            storage_co2 = remove_entries(storage_co2, pos, '0')
        else:
            storage_co2 = remove_entries(storage_co2, pos, '1')
        pos += 1
    

    key_oxy = list(storage_oxy)[0]
    key_co2 = list(storage_co2)[0]

    
    b_int_oxy = int(storage_oxy[key_oxy], 2)
    b_int_co2 = int(storage_co2[key_co2], 2)
    
    solution = b_int_oxy*b_int_co2

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 230)
problem_b(PROGBLEM_INPUT_TXT, 2555739)
print("\n")