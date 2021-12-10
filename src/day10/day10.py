"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day10/input.txt").read_text()

EXAMPLE_INPUT1 = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
EXAMPLE_RESULT1 = 26397

def string_worker(input_string): 
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def checkLine(expect, string, pos):
    if expect == '(':
        expect = ')'
    elif expect == '[':
        expect = ']'
    elif expect == '{':
        expect = '}'
    else:
        expect = '>'
    score = 0
    while pos != len(string) and score == 0: 
        if (string[pos] in '([{<'):
            score, pos = checkLine(string[pos], string, pos+1)
        else:
            if (string[pos] == expect):
                return score, pos+1
            else:
                #Error
                if string[pos] == ')':
                    return 3, pos
                elif string[pos] == ']':
                    return 57, pos
                elif string[pos] == '}':
                    return 1197, pos
                elif string[pos] == '>':
                    return 25137, pos
                else:
                    return 'Unxpected'
    return score, pos


def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    rows = input_string.split('\n')
    for row in rows:
        score, pos = checkLine(row[0], row, 1)
        solution += score

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

def checkLine2(expect, string, pos):
    if expect == '(':
        expect = ')'
        newscore = -1
    elif expect == '[':
        expect = ']'
        newscore = -2
    elif expect == '{':
        expect = '}'
        newscore = -3
    else:
        expect = '>'
        newscore = -4

    score = 0
    while pos != len(string) and score == 0: 
        if (string[pos] in '([{<'):
            score, pos = checkLine2(string[pos], string, pos+1)
        else:
            if (string[pos] == expect):
                return score, pos+1
            else:
                #Error
                if string[pos] == ')':
                    return 3, pos
                elif string[pos] == ']':
                    return 57, pos
                elif string[pos] == '}':
                    return 1197, pos
                elif string[pos] == '>':
                    return 25137, pos
                else:
                    return 'Unxpected'
    if score > 0: #corrupt line 
        return score, pos
    else:
        #incomplete line repair it but only add score
        score = score*5 + newscore
        return score, pos+1
        

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solutions = []
    rows = input_string.split('\n')
    for row in rows:
        score, pos = checkLine2(row[0], row, 1)
        if score < 0:
            solutions.append(score*-1)

    length = len(solutions)
    solutions = sorted(solutions)

    solution = solutions[int(length/2)]

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)


problem_b(EXAMPLE_INPUT1, 288957)
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")

