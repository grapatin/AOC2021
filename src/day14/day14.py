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
    
    steps = 10
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
        #print('1:', template)

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
problem_a(PROGBLEM_INPUT_TXT, 3213)
print("\n")

def worker_improve_rule(w_string, rules_dict_ex, count_dict_ext, rules_dict, turns):
    rule_string = w_string
    for l in range(turns):
        work_me = ''
        for pos in range(len(w_string)-1):
            search_str = w_string[pos]+w_string[pos+1]
            if search_str in rules_dict:
                work_me += w_string[pos] + rules_dict[search_str]
            else:
                work_me += w_string[pos]
        work_me += w_string[-1]
        w_string = work_me

    rules_dict_ex[rule_string] = w_string[:-1]

    count_dict = {}
    for char in w_string[:-1]:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    count_dict_ext[rule_string] = count_dict

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    template, rules_string = input_string.split('\n\n')
    rules_dict = {}
    rules_string = rules_string.split('\n')

    for row in rules_string:
        find_me, insert_me = row.split(' -> ')
        rules_dict[find_me] = insert_me

    #teach algo 20 steps
    rules_dict_ext = {}
    count_dict_ext = {}
    for key in rules_dict:
        worker_improve_rule(key, rules_dict_ext, count_dict_ext, rules_dict, 20)

    template = worker2(template, rules_dict_ext)    
    #dummy = worker2(template, rules_dict_ext)    
    #print('2:', dummy)

    answer_dict = {}
    for rule in rules_dict_ext:
        count = occurrences(template, rule)
        if count > 0:    
            for key in count_dict_ext[rule]:
                if key in answer_dict:
                    answer_dict[key] += count_dict_ext[rule][key]*count
                    #answer_dict[key] += 1
                else:
                    answer_dict[key] = count_dict_ext[rule][key]*count

    #also add the very last character
    answer_dict[template[-1]] += 1

    v=list(answer_dict.values())
    k=list(answer_dict.keys())
    solution = max(v) - min(v)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def worker2(template, rules_dict_ext):
    work_me = ''
    for pos in range(len(template)-1):
        search_str = template[pos]+template[pos+1]
        if search_str in rules_dict_ext:
            work_me += rules_dict_ext[search_str]
        else:
            work_me += template[pos]
    work_me += template[-1]
    template = work_me
    return template

problem_b(EXAMPLE_INPUT1, 2188189693529)
problem_b(PROGBLEM_INPUT_TXT, 3711743744429) #3710268282222 too low
print("\n")


