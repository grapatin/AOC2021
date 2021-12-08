"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day08/input.txt").read_text()

EXAMPLE_INPUT1 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
EXAMPLE_RESULT1 = 26

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')

    solution = 0
    for row in rows:
        part = row.split(' | ')
        segments = part[1].split()
        for segment in segments:
            if len(segment) in [2, 7, 4, 3]:
                solution += 1

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 539)
print("\n")


def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')

    solution = 0
    for row in rows:
        part = row.split(' | ')
        segments_p1 = part[0].split()
        storage_dict = {}
        identify_chars(segments_p1, storage_dict)
    
        segments_p2 = part[1].split()
        number_string = ''
        for segment in segments_p2:
            if sorted(segment) == sorted(storage_dict[0]):
                number_string += '0'
            if sorted(segment) == sorted(storage_dict[1]):
                number_string += '1'
            if sorted(segment) == sorted(storage_dict[2]):
                number_string += '2'
            if sorted(segment) == sorted(storage_dict[3]):
                number_string += '3'
            if sorted(segment) == sorted(storage_dict[4]):
                number_string += '4'
            if sorted(segment) == sorted(storage_dict[5]):
                number_string += '5'
            if sorted(segment) == sorted(storage_dict[6]):
                number_string += '6'
            if sorted(segment) == sorted(storage_dict[7]):
                number_string += '7'
            if sorted(segment) == sorted(storage_dict[8]):
                number_string += '8'
            if sorted(segment) == sorted(storage_dict[9]):
                number_string += '9'
        solution += int(number_string)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def identify_chars(segments, storage_dict):
    for segment in segments:
        if len(segment) == 2: #This is number 1
            storage_dict[1] = segment                
        elif len(segment) == 3: #This is number 7
            storage_dict[7] = segment
        elif len(segment) == 4: #This is number 4
            storage_dict[4] = segment
        elif len(segment) == 7: #This is number 8
            storage_dict[8] = segment
        
    for segment in segments:
        if len(segment) == 6: #This is 0, 6 or 9
            is_it_9 = True
            for char in storage_dict[4]:
                if char not in segment:
                    is_it_9 = False
            if is_it_9 == True:
                storage_dict[9] = segment
            else:
                is_it_0 = True
                for char in storage_dict[1]:
                    if char not in segment:
                        is_it_0 = False
                if is_it_0 == True:
                    storage_dict[0] = segment
                else:
                    storage_dict[6] = segment

    for segment in segments:
        if len(segment) == 5: #This is 2,3 or 5
            is_it_3 = True
            for char in storage_dict[1]:
                if char not in segment:
                    is_it_3 = False
            if is_it_3 == True:
                storage_dict[3] = segment
            else:
                is_it_5 = True
                for char in segment:
                    if char not in storage_dict[6]:
                        is_it_5 = False
                if is_it_5 == True:
                    storage_dict[5] = segment
                else:
                    storage_dict[2] = segment

problem_b('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf', 5353)
problem_b(PROGBLEM_INPUT_TXT, 1084606)
print("\n")