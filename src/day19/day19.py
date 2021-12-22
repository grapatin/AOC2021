"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day19/input.txt").read_text()

EXAMPLE_INPUT1 = """"""
EXAMPLE_RESULT1 = 1514


def create_24_variants(input_array):
    x,y,z = input_array
    result_dict = {}
    result_dict[tuple(input_array)] = 1

    result_dict[tuple([-1*y,x,z])] = 2
    result_dict[tuple([-1*x,-1*y,z])] = 3
    result_dict[tuple([y,-1*x,z])] = 4

    result_dict[tuple([-1*x,y,-1*z])] = 5
    result_dict[tuple([-1*y,-1*x,-1*z])] = 6
    result_dict[tuple([x,-1*y,-1*z])] = 7
    result_dict[tuple([y,x,-1*z])] = 8

    result_dict[tuple([x,z,-1*y])] = 9
    result_dict[tuple([-1*z,x,-1*y])] = 10
    result_dict[tuple([-1*x,-1*z,-1*y])] = 11
    result_dict[tuple([z,-1*x,-1*y])] = 12

    result_dict[tuple([x,-1*z,y])] = 13
    result_dict[tuple([z,x,y])] = 14
    result_dict[tuple([-1*x,z,y])] = 15
    result_dict[tuple([-1*z,-1*x,y])] = 16

    result_dict[tuple([-1*z,y,x])] = 17
    result_dict[tuple([-1*y,-1*z,x])] = 18 #17
    result_dict[tuple([z,-1*y,x])] = 19
    result_dict[tuple([y,z,x])] = 20

    result_dict[tuple([z,y,-1*x])] = 21
    result_dict[tuple([-1*y,z,-1*x])] = 22 #21
    result_dict[tuple([-1*z,-1*y,-1*x])] = 23
    result_dict[tuple([y,-1*z,-1*x])] = 24
        
    return result_dict

class CommonBeacons:
    def __init__(self, scanner_id, beacon_row_row):
        self.beacon_dict = {}
        self.scanner_dict = {}
        self.beacon_dict[beacon_row_row] = 1
        self.scanner_dict[scanner_id] = 1

    def add(self, scanner_id, beacon_row_row):
        self.beacon_dict[beacon_row_row] = 1
        self.scanner_dict[scanner_id] = 1

class BeaconClass:
    def __init__(self, parent_scanner, x,y,z):
        self.parent_scanner = parent_scanner
        self.x = x
        self.y = y
        self.z = z
        self.beacon_relations = {}
        self.name = '(' + str(x) + ',' +str(y) + ',' + str(z)+')'

    def store_distance(self, other_beacon):
        if self != other_beacon:
            x_d = other_beacon.x - self.x
            y_d = other_beacon.y - self.y
            z_d = other_beacon.z - self.z
            self.beacon_relations[other_beacon] = [x_d, y_d, z_d]

    def get_rotated_cord(self):
        rotation_index = self.parent_scanner.rotation_index
        x,y,z = self.x, self.y, self.z

        if rotation_index == 1:
            return [self.x, self.y, self.z]
        elif rotation_index == 2:
            return [-1*y,x,z]        
        elif rotation_index == 3:
            return [-1*x,-1*y,z]
        elif rotation_index == 4:
            return [y,-1*x,z]

        elif rotation_index == 5:
            return [-1*x,y,-1*z]
        elif rotation_index == 6:
            return [-1*y,-1*x,-1*z]
        elif rotation_index == 7:
            return [x,-1*y,-1*z]
        elif rotation_index == 8:
            return [y,x,-1*z]

        elif rotation_index == 9:
            return [x,z,-1*y]
        elif rotation_index == 10:
            return [-1*z,x,-1*y]
        elif rotation_index == 11:
            return [-1*x,-1*z,-1*y]
        elif rotation_index == 12:
            return [z,-1*x,-1*y]

        elif rotation_index == 13:
            return [x,-1*z,y]
        elif rotation_index == 14:
            return [z,x,y]
        elif rotation_index == 15:
            return [-1*x,z,y]
        elif rotation_index == 16:
            return [-1*z,-1*x,y]

        elif rotation_index == 17:
            return [-1*z,y,x]
        elif rotation_index == 18:
            return [-1*y,-1*z,x]
        elif rotation_index == 19:
            return [z,-1*y,x]
        elif rotation_index == 20:
            return [y,z,x]

        elif rotation_index == 21:
            return [z,y,-1*x]
        elif rotation_index == 22:
            return [-1*y,z,-1*x]
        elif rotation_index == 23:
            return [-1*z,-1*y,-1*x]
        elif rotation_index == 24:
            return [y,-1*z,-1*x]
            
class ScannerClass:
    def __init__(self, scanner_input):
        rows = scanner_input.split('\n')
        self.scanner_id = rows.pop(0)
        self.beacons = {}
        self.rotation_index = 1 
        self.x = 0
        self.y = 0
        self.z = 0
        for index, row in enumerate(rows):
            x,y,z = [int(number) for number in row.split(',')]
            self.beacons[index] = BeaconClass(self, x,y,z)

        #calculate relative position between beacon and all other beacon
        for beacon in self.beacons.values():
            for other_beacon in self.beacons.values():
                beacon.store_distance(other_beacon)

    def return_number_of_beacons(self):
        return len(self.beacons)
        
    def get_rotated_cord(self, xyz_a):
        rotation_index = self.rotation_index
        x,y,z = xyz_a[0], xyz_a[1], xyz_a[2]

        if rotation_index == 1:
            return xyz_a
        elif rotation_index == 2:
            return [-1*y,x,z]        
        elif rotation_index == 3:
            return [-1*x,-1*y,z]
        elif rotation_index == 4:
            return [y,-1*x,z]

        elif rotation_index == 5:
            return [-1*x,y,-1*z]
        elif rotation_index == 6:
            return [-1*y,-1*x,-1*z]
        elif rotation_index == 7:
            return [x,-1*y,-1*z]
        elif rotation_index == 8:
            return [y,x,-1*z]

        elif rotation_index == 9:
            return [x,z,-1*y]
        elif rotation_index == 10:
            return [-1*z,x,-1*y]
        elif rotation_index == 11:
            return [-1*x,-1*z,-1*y]
        elif rotation_index == 12:
            return [z,-1*x,-1*y]

        elif rotation_index == 13:
            return [x,-1*z,y]
        elif rotation_index == 14:
            return [z,x,y]
        elif rotation_index == 15:
            return [-1*x,z,y]
        elif rotation_index == 16:
            return [-1*z,-1*x,y]

        elif rotation_index == 17:
            return [-1*z,y,x]
        elif rotation_index == 18:
            return [-1*y,-1*z,x]
        elif rotation_index == 19:
            return [z,-1*y,x]
        elif rotation_index == 20:
            return [y,z,x]

        elif rotation_index == 21:
            return [z,y,-1*x]
        elif rotation_index == 22:
            return [-1*y,z,-1*x]
        elif rotation_index == 23:
            return [-1*z,-1*y,-1*x]
        elif rotation_index == 24:
            return [y,-1*z,-1*x]

    def find_common_beacon(self, other_scanner):
        for base_beacon_1 in self.beacons.values():
            hits_found = 0
            for base_beacon_2 in other_scanner.beacons.values():
                for other_beacon_cord in base_beacon_1.beacon_relations.values():
                    other_beacon_cord = self.get_rotated_cord(other_beacon_cord)
                    for other_beacon_cord_2 in base_beacon_2.beacon_relations.values():
                        all_variants_dict = create_24_variants(other_beacon_cord_2)
                        if tuple(other_beacon_cord) in all_variants_dict:
                            hits_found += 1
                            if hits_found == 11:
                                print('Hit #', hits_found, 'for beacon:', base_beacon_1.name)
                                #TODO calculate what this means for cord for scanner!
                                #figure out rotation of scanner relative scanner 0
                                other_scanner.rotation_index = all_variants_dict[tuple(other_beacon_cord)]
                                beacon_2_scanner_0_rotation = base_beacon_2.get_rotated_cord()

                                scanner_location_x = base_beacon_1.x - beacon_2_scanner_0_rotation[0] - self.x
                                scanner_location_y = base_beacon_1.y - beacon_2_scanner_0_rotation[1] - self.y
                                scanner_location_z = base_beacon_1.z - beacon_2_scanner_0_rotation[2] - self.z

                                other_scanner.x = scanner_location_x
                                other_scanner.y = scanner_location_y
                                other_scanner.z = scanner_location_z
                                print(other_scanner.scanner_id, 'is at:', [other_scanner.x, other_scanner.y, other_scanner.z])
                                return True
                        else:
                            pass
                            #print('No hit')
        return False
                    



def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    scanners = input_string.split('\n\n')
    scanner_list :ScannerClass = []
    for scanner_input in scanners:
        scanner_list.append(ScannerClass(scanner_input))

    all_beacons_from_scanner_0 = {}

    for beacon in scanner_list[0].beacons.values():
        all_beacons_from_scanner_0[tuple(beacon.get_rotated_cord())] = 1

    
    identified_scanners = {}
    not_identified_scanners = {}
    identified_scanners[scanner_list[0]] = True
    for scan_i in range(1,len(scanner_list)):
        identified_scanners[scanner_list[scan_i]] = False

    all_identified = False

    base_scanner = scanner_list[0]
    searched_scanners = {}
    while (all_identified == False):
        all_identified = True
        for other_scanner in identified_scanners:
            if identified_scanners[other_scanner] == False:
                all_identified = False
                if base_scanner.find_common_beacon(other_scanner):
                    identified_scanners[other_scanner] = True
        searched_scanners[base_scanner] = True
        for new_base in identified_scanners:
            if new_base not in searched_scanners and identified_scanners[new_base] == True:
                base_scanner = new_base
                break

    all_beacons = 0
    for scan in scanner_list:
        all_beacons += scan.return_number_of_beacons()

    solution =  all_beacons

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a("""--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14""", 79)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
