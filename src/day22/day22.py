"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day22/input.txt").read_text()

EXAMPLE_INPUT1 = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11"""
EXAMPLE_RESULT1 = 590784

class AllCubes:
    def __init__(self):
        self.storage = {}

    def add_cube(self, cube):
        self.storage[cube] = 1

    def find_overlapp(self, new_cube):
        cube :CubeClass
        overlapp = 0
        for cube in self.storage:
            overlapp += cube.size_of_overlapp(new_cube)

        return overlapp
        
class CubeClass:
    def __init__(self, row):

        parts = row.split('=')
        self.x1 = int(parts[1])
        self.x2 = int(parts[2])
        self.y1 = int(parts[4])
        self.y2 = int(parts[5])
        self.z1 = int(parts[7])
        self.z2 = int(parts[8])
        self.size_of_cube = ((self.x2-self.x1+1)*(self.y2-self.y1+1)*(self.z2-self.z1+1))   

    def inside_cube(self, x_t, y_t, z_t):
        if self.x1 <= x_t <= self.x2:
            if self.y1 <= y_t <= self.y2:
                if self.z1 <= z_t <= self.z2:
                    return True
        return False

    def size_of_overlapp(self, newCube):
        overlapp_b = False
        overlapp = 0
        inside_x1 = self.x1
        inside_x2 = self.x2
        inside_y1 = self.y1
        inside_y2 = self.y2
        inside_z1 = self.z1
        inside_z2 = self.z2
        if self.inside_cube(newCube.x1, newCube.y1, newCube.z1):
            overlapp_b = True
            inside_x1 = newCube.x1
            inside_y1 = newCube.y1
            inside_z1 = newCube.z1
        if self.inside_cube(newCube.x2, newCube.y2, newCube.z2):
            overlapp_b = True
            inside_x2 = newCube.x2
            inside_y2 = newCube.y2
            inside_z2 = newCube.z2

        if overlapp_b:
            overlapp = (inside_x2 - inside_x1 + 1)*(inside_y2 - inside_y1 + 1)*(inside_z2-inside_z1 + 1)
        return overlapp

class StorageClass:
    def __init__(self):
        self.storage_dict = {}

    def set(self, cord, pos_on):
        self.storage_dict[tuple(cord)] = pos_on    


def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    input_string = input_string.replace('..', '=')
    input_string = input_string.replace(',','=')
    rows = input_string.split('\n')
    storage_class = StorageClass()
    for row in rows:
        parts = row.split('=')
        pos_on = True
        x1 = int(parts[1])
        x2 = int(parts[2])
        y1 = int(parts[4])
        y2 = int(parts[5])
        z1 = int(parts[7])
        z2 = int(parts[8])
        if 'on' in row:
            pos_on = True
        else:
            pos_on = False
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    storage_class.set([x,y,z], pos_on)

    solution = 0
    for value in storage_class.storage_dict.values():
        if value:
            solution += 1

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
#problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

#TODO solve that we can have multiple overlapps


def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    input_string = input_string.replace('..', '=')
    input_string = input_string.replace(',','=')
    rows = input_string.split('\n')
    all_cubes :AllCubes = AllCubes()
    solution = 0
    for row in rows:
        new_cube = CubeClass(row)
        if 'on' in row:
            solution += new_cube.size_of_cube
            solution -= all_cubes.find_overlapp(new_cube)
            all_cubes.add_cube(new_cube)
        else:
            solution -= all_cubes.find_overlapp(new_cube)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)



problem_b(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
#problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")