"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day16/input.txt").read_text()

EXAMPLE_INPUT1 = """8A004A801A8002F478"""
EXAMPLE_RESULT1 = 16

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    global sum_version_numer

    bin_string = fix_string(input_string)

    worker(bin_string)
    
    solution = sum_version_numer

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def worker(bin_string):
    global sum_version_numer

    while bin_string != '' and int(bin_string, 2) > 0:
        bits_so_far = 0
        packet_version_b = bin_string[:3]
        packet_version = int(packet_version_b, 2)
        sum_version_numer += packet_version

        bin_string = bin_string[3:]
        bits_so_far += 3
        packet_type = int(bin_string[:3], 2)
        bin_string = bin_string[3:]
        bits_so_far += 3

        #sum_version_numer += packet_type
        if packet_type == 4: #literal value
            done = False
            value = ''
            while not done:
                first_bit = bin_string[0]
                bin_string = bin_string[1:]
                if first_bit == '0':
                    done = True
                value += bin_string[0:4]
                bin_string = bin_string[4:]
        else:   #Operator id
            length_type_id = bin_string[0]
            bin_string = bin_string[1:]
            bits_so_far += 1
            if length_type_id == '0': #next 15 bits length of sub packet
                length = int(bin_string[:15], 2)
                bin_string = bin_string[15:]
                bits_so_far += 15
                #worker(bin_string[:length])
                #bin_string = bin_string[length:]

            else: #next 11 bits are the number of subpackets immediately contained by this packet
                no_sub_packets = int(bin_string[:11], 2)
                bin_string = bin_string[11:]
                #worker(bin_string)

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
sum_version_numer = 0
problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
sum_version_numer = 0
problem_a('620080001611562C8802118E34', 12)
sum_version_numer = 0
problem_a('C0015000016115A2E0802F182340', 23)
sum_version_numer = 0
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
