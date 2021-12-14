"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day14/input.txt").read_text()

EXAMPLE_INPUT1 = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
EXAMPLE_RESULT1 = 1514

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    template, rules_string = input_string.split('\n\n')
    rules_dict = {}
    rules_string = rules_string.split('\n')

    for row in rules_string:
        find_me, insert_me = row.split(' -> ')
        rules_dict[find_me] = insert_me
    
    steps = 40
    for l in range(steps):
        work_me = ''
        for pos in range(len(template)-1):
            search_str = template[pos]+template[pos+1]
            if search_str in rules_dict:
                work_me += template[pos] + rules_dict[search_str]
            else:
                work_me += template[pos]
        work_me += template[-1]
        template = work_me

    count_dict = {}
    for char in template:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    
    v=list(count_dict.values())
    k=list(count_dict.keys())
    solution = max(v) - min(v)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, 1588)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
