"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day22/input.txt").read_text()

EXAMPLE_INPUT1 = """on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15"""


EXAMPLE_RESULT1 = 590784

class AllCubes:
    def __init__(self):
        self.storage = {}
        self.first = True

    def add_cube(self, row):
        cube_from_storage :CubeClass
        rows = ''
        for cube_from_storage in self.storage:
            rows = cube_from_storage.create_new_rows_from_this_row(row)
            if (rows != row): #We have a split, stop and continue
                break
        if len(rows) > 0:
                for new_row in rows.split('\n'):
                    if new_row == row: #we have found a cube that actually does not need any further changes
                        new_cube = CubeClass(new_row)
                        self.storage[new_cube] = new_cube
                    else: #we need to check so this does not conflict with something else
                        self.add_cube(new_row)
        if self.first:
            self.first = False
            new_cube = CubeClass(row)
            self.storage[new_cube] = new_cube

    def off_cube(self, row):
        cube_from_storage :CubeClass
        #run all existings cubes against this new cube
        cube_off = CubeClass(row)
        new_storage = {}
        for cube_from_storage in self.storage:
            rows = cube_off.create_new_rows_from_this_row(cube_from_storage.row)
            #print('off rows:', rows)
            if (len(rows) > 0):
                for new_row in rows.split('\n'):
                    new_cube = CubeClass(new_row)
                    new_storage[new_cube] = new_cube
        self.storage = new_storage
            
        
    def calc_size(self):
        cube :CubeClass
        count = 0
        for cube in self.storage:
            count += cube.size_of_cube

        return count

class CubeClass:
    def __init__(self, row):
        self.row = row
        parts = row.split('=')
        self.x1 = int(parts[1])
        self.x2 = int(parts[2])
        self.y1 = int(parts[4])
        self.y2 = int(parts[5])
        self.z1 = int(parts[7])
        self.z2 = int(parts[8])
        self.size_of_cube = ((self.x2-self.x1+1)*(self.y2-self.y1+1)*(self.z2-self.z1+1))   

    def create_new_rows_from_this_row(self, row):
        cord = ['x', 'y', 'z']
        cord_array = []
        rows = ''
        if row != self.row:
            new_parts = row.split('=')
            existing_parts = self.row.split('=')
            for i in range(0,9,3):
                new_low = int(new_parts[i+1])
                new_high = int(new_parts[i+2])
                existing_low = int(existing_parts[i+1])
                existing_high = int(existing_parts[i+2])
                overlapp, overlapp_low, overlapp_high = self.find_over_lapp_cords(new_low, new_high, existing_low, existing_high)
                if overlapp:
                    #print('Overlapp found', cord[int(i / 3)], ':', new_low, new_high, existing_low, existing_high, overlapp_low, overlapp_high)
                    cord_array.append(new_low)
                    cord_array.append(overlapp_low)
                    cord_array.append(overlapp_high)
                    cord_array.append(new_high)
                else:
                    #print('No overlapp found', cord[int(i / 3)], ':', new_low, new_high, existing_low, existing_high)
                    #since one of the cord didn't overlapp there is no way they can overlapp
                    return row 
            x_new_low = cord_array[0]
            x_overlapp_low = cord_array[1]
            x_overlapp_high = cord_array[2]
            x_new_high = cord_array[3]

            y_new_low = cord_array[4]
            y_overlapp_low = cord_array[5]
            y_overlapp_high = cord_array[6]
            y_new_high = cord_array[7]
            
            z_new_low = cord_array[8]
            z_overlapp_low = cord_array[9]
            z_overlapp_high = cord_array[10]
            z_new_high = cord_array[11]
            
            #create new string, 3 scenarious for each x,y,z, part low outside before overlapp, overlapp, part after overlapp
            if x_new_low != x_overlapp_low: 
                str_temp = "on x="+str(x_new_low)+'='+str(x_overlapp_low-1)+'=y='+str(y_new_low)+'='+str(y_new_high)+'=z='+str(z_new_low)+'='+str(z_new_high)
                rows += str_temp + '\n'
                #print('Row x before overlapp: ' + str_temp)
            if x_new_high != x_overlapp_high:
                str_temp = "on x="+str(x_overlapp_high+1)+'='+str(x_new_high)+'=y='+str(y_new_low)+'='+str(y_new_high)+'=z='+str(z_new_low)+'='+str(z_new_high)
                rows += str_temp + '\n'
                #print('Row x after overlapp: ' + str_temp)
           
            if y_new_low != y_overlapp_low:
                str_temp = "on x="+str(x_overlapp_low)+'='+str(x_overlapp_high)+'=y='+str(y_new_low)+'='+str(y_overlapp_low - 1)+'=z='+str(z_new_low)+'='+str(z_new_high)
                rows += str_temp + '\n'
                #print('Row y before overlapp: ' + str_temp)

            if y_new_high != y_overlapp_high:
                str_temp = 'on x='+str(x_overlapp_low)+'='+str(x_overlapp_high)+'=y='+str(y_overlapp_high+1)+'='+str(y_new_high)+'=z='+str(z_new_low)+'='+str(z_new_high)
                rows += str_temp + '\n'
                #print('Row y after overlapp: ' + str_temp)
            
            if z_new_low != z_overlapp_low:
                str_temp = 'on x='+str(x_overlapp_low)+'='+str(x_overlapp_high)+'=y='+str(y_overlapp_low)+'='+str(y_overlapp_high)+'=z='+str(z_new_low)+'='+str(z_overlapp_low-1)
                rows += str_temp + '\n'
                #print('Row z before overlapp: ' + str_temp)
            
            if z_new_high != z_overlapp_high:
                str_temp = 'on x='+str(x_overlapp_low)+'='+str(x_overlapp_high)+'=y='+str(y_overlapp_low)+'='+str(y_overlapp_high) +'=z='+str(z_overlapp_high+1)+'='+str(z_new_high)
                rows += str_temp + '\n'
                #print('Row z after overlapp: ' + str_temp)
        return rows[:-1]

    def find_over_lapp_cords(self2, new_low, new_high, current_low, current_high):
        #find X overlapp
        if new_low > current_high or new_high < current_low:
            #no overlapp
            return False, 0, 0
        else:
            #we have a overlapp
            if new_low >= current_low:
                overlapp_low = new_low
            else:
                overlapp_low = current_low
            if new_high <= current_high:
                overlapp_high = new_high
            else:
                overlapp_high = current_high
            return True, overlapp_low, overlapp_high
        

class StorageClass_partI:
    def __init__(self):
        self.storage_dict = {}

    def set(self, cord, pos_on):
        self.storage_dict[tuple(cord)] = pos_on    


def problem_a(input_string, expected_result):
    global EXAMPLE_RESULT1
    """Problem A solved function
    """
    input_string = input_string.replace('..', '=')
    input_string = input_string.replace(',','=')
    rows = input_string.split('\n')
    storage_class = StorageClass_partI()
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

    EXAMPLE_RESULT1 = solution
    if solution == expected_result:
        print("Correct solution found:", solution)

    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
#problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    input_string = input_string.replace('..', '=')
    input_string = input_string.replace(',','=')
    rows = input_string.split('\n')
    all_cubes :AllCubes = AllCubes()
    for row in rows:
        if 'on' in row:
            all_cubes.add_cube(row)
        else:
            all_cubes.off_cube(row)

    solution = all_cubes.calc_size()

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_b(PROGBLEM_INPUT_TXT, 1218645427221987)
print("\n")