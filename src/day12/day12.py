"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day12/input.txt").read_text()

EXAMPLE_INPUT1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
EXAMPLE_RESULT1 = 10

class CaveClass:
    def __init__(self, name):
        self.visited = False
        if ord('a') <= ord(name[0]) <= ord('z'):
            self.type = 'small'
        else:
            self.type = 'large'
        self.name = name
        self.next_caves = {}

    def add_next_cave(self, cave):
        if cave.name not in self.next_caves:
            self.next_caves[cave.name] = 1

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def reg_walker(current_cave, cave_storage, path_taken, cave_paths_found):
    c_i = cave_storage[current_cave]
    for next_cave in c_i.next_caves:
        next_cave_i = cave_storage[next_cave]
        if next_cave_i.type == 'small' and next_cave in path_taken:
            #abort
            pass
        else:
            if next_cave == 'end':
                cave_paths_found[path_taken] = True
            else:
                reg_walker(next_cave, cave_storage, path_taken+'-'+next_cave, cave_paths_found)
    

def reg_walker2(current_cave, cave_storage, path_taken, cave_paths_found, allowed_twice):
    c_i = cave_storage[current_cave]
    for next_cave in c_i.next_caves:
        next_cave_i = cave_storage[next_cave]
        if next_cave_i.type == 'small' and next_cave in path_taken:
            #abort
            if next_cave == allowed_twice:
                reg_walker2(next_cave, cave_storage, path_taken+'-'+next_cave, cave_paths_found, '')
        else:
            if next_cave == 'end':
                cave_paths_found[path_taken] = True
            else:
                reg_walker2(next_cave, cave_storage, path_taken+'-'+next_cave, cave_paths_found, allowed_twice)


def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    cave_storage = {}
    cave_paths_found = {}

    rows = input_string.split('\n')

    for row in rows:
        caves = row.split('-')
        if caves[0] not in cave_storage:
            cave1_class = CaveClass(caves[0])
            cave_storage[caves[0]] = cave1_class
        else:
            cave1_class = cave_storage[caves[0]]
        if caves[1] not in cave_storage:
            cave2_class = CaveClass(caves[1])
            cave_storage[caves[1]] = cave2_class
        else:
            cave2_class = cave_storage[caves[1]]

        cave1_class.add_next_cave(cave2_class)
        cave2_class.add_next_cave(cave1_class)


    reg_walker('start', cave_storage, 'start', cave_paths_found)

    solution = len(cave_paths_found)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 3856)
print("\n")


def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    cave_storage = {}
    cave_paths_found = {}
    small_caves_storage = {}

    rows = input_string.split('\n')

    for row in rows:
        caves = row.split('-')
        if caves[0] not in cave_storage:
            cave1_class = CaveClass(caves[0])
            cave_storage[caves[0]] = cave1_class
        else:
            cave1_class = cave_storage[caves[0]]
        if caves[1] not in cave_storage:
            cave2_class = CaveClass(caves[1])
            cave_storage[caves[1]] = cave2_class
        else:
            cave2_class = cave_storage[caves[1]]

        cave1_class.add_next_cave(cave2_class)
        cave2_class.add_next_cave(cave1_class)

    for cave_name in cave_storage:
        if cave_storage[cave_name].type == 'small' and cave_name not in 'start_end':
            small_caves_storage[cave_name] = 1
    for small_cave in small_caves_storage:
        reg_walker2('start', cave_storage, 'start', cave_paths_found, small_cave)

    solution = len(cave_paths_found)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 36)
problem_b(PROGBLEM_INPUT_TXT, 116692)
print("\n")
