"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import numpy

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day16/input.txt").read_text()

EXAMPLE_INPUT1 = """8A004A801A8002F478"""
EXAMPLE_RESULT1 = 16

def problem_a(input_string, expected_result):
    """Problem A solved function
    """

    bin_string = fix_string(input_string)

    _, solution, _ = worker2(bin_string)
    

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def fix_string(string_input):
    replacement_dict = { '0':'0000',
        '1': '0001', 
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111' }

    new_string = ''
    for char in string_input:
        new_string += replacement_dict[char]

    return new_string

def worker2(bin_string, no_subpackets = 9999999, mode = 0):
    sum_version_numer = 0
    bin_eaten = 0
    values_list = []

    while bin_string != '' and int(bin_string, 2) > 0 and no_subpackets > 0:
        packet_version_b = bin_string[:3]
        packet_version = int(packet_version_b, 2)
        sum_version_numer += packet_version

        bin_string = bin_string[3:]
        bin_eaten += 3
        packet_type = int(bin_string[:3], 2)
        bin_string = bin_string[3:]
        bin_eaten += 3

        if packet_type == 4: #literal value
            done = False
            value_s = ''
            while not done:
                first_bit = bin_string[0]
                bin_string = bin_string[1:]
                bin_eaten += 1
                if first_bit == '0':
                    done = True
                value_s += bin_string[0:4]
                bin_string = bin_string[4:]
                bin_eaten += 4
            value = int(value_s, 2)
            values_list.append(value)
        else:   #Operator id
            length_type_id = bin_string[0]
            bin_string = bin_string[1:]
            bin_eaten += 1
            if length_type_id == '0': #next 15 bits length of sub packet
                length = int(bin_string[:15], 2)
                bin_string = bin_string[15:]
                bin_eaten += 15
                new_pos, sum_from_func, result = worker2(bin_string[:length], 99999999, packet_type)
                values_list.append(result)
                if new_pos != length:
                    print('Error')
                sum_version_numer += sum_from_func
                bin_string = bin_string[length:]
                bin_eaten += length

            else: #next 11 bits are the number of subpackets immediately contained by this packet
                no_subpackets_temp = int(bin_string[:11], 2)
                bin_string = bin_string[11:]
                bin_eaten += 11
                new_pos, sum_from_func, result = worker2(bin_string, no_subpackets_temp, packet_type)
                values_list.append(result)
                sum_version_numer += sum_from_func
                bin_string = bin_string[new_pos:]
                bin_eaten += new_pos
        no_subpackets -= 1
    result = 0
    if mode == 0:
        result = sum(values_list)
    elif mode == 1:
        result = numpy.prod(values_list)
    elif mode == 2:
        result = min(values_list)
    elif mode == 3:
        result = max(values_list)
    elif mode == 5:
        if values_list[0] > values_list[1]:
            result = 1
        else:
            result = 0
    elif mode == 6:
        if values_list[0] < values_list[1]:
            result = 1
        else:
            result = 0
    elif mode == 7:
        if values_list[0] == values_list[1]:
            result = 1
        else:
            result = 0
    return bin_eaten, sum_version_numer, result

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    bin_string = fix_string(input_string)
    _, sum_version_numer, solution = worker2(bin_string)
    
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

sum_version_numer = 0
problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
sum_version_numer = 0
problem_a('620080001611562C8802118E34', 12)
sum_version_numer = 0
problem_a('C0015000016115A2E0802F182340', 23)
sum_version_numer = 0
problem_a(PROGBLEM_INPUT_TXT, 1014)
print("\n")


print('Part B')
problem_b('C200B40A82', 3)
problem_b('04005AC33890', 54)
problem_b('880086C3E88112', 7)
problem_b('CE00C43D881120', 9)
problem_b('D8005AC2A8F0', 1)
problem_b('F600BC2D8F', 0)
problem_b('9C005AC2F8F0', 0)
problem_b('9C0141080250320F1802104A08', 1)
problem_b(PROGBLEM_INPUT_TXT, 1014) #23212829832 Too low
print("\n")
