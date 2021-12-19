"""
Template code
"""
from pathlib import Path
import json
import test


PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day18/input.txt").read_text()

EXAMPLE_INPUT1 = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
EXAMPLE_RESULT1 = 3488

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

class SnailFishNumber:
    def __init__(self, init_string):
            para_count = 0
            init_string = init_string[1:-1] #Remove first and last []
            #find comma
            for index in range(len(init_string)):
                char = init_string[index]
                if char == '[':
                    para_count += 1
                elif char == ']':
                    para_count -= 1
                elif char == ',' and para_count == 0:
                    #this is the comma
                    parts = [init_string[:index],init_string[index + 1:]]
                    if '[' in parts[0]:
                        #new pair
                        self.left_part = SnailFishNumber(parts[0])
                    else:
                        self.left_number = int(parts[0])
                        self.left_part = None
                    if '[' in parts[1]:
                        #new pair
                        self.right_part = SnailFishNumber(parts[1])
                    else:
                        self.right_number = int(parts[1])
                        self.right_part = None
                
    def calc_magnitude(self):
        sum = 0
        if self.left_part is None:
            sum += self.left_number*3
        else:
            sum += self.left_part.calc_magnitude()*3

        if self.right_part is None:
            sum += self.right_number*2
        else:
            sum += self.right_part.calc_magnitude()*2

        return sum

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')
    first_row = rows.pop(0)
    base = json.loads(first_row)
    
    for row in rows:
        row = json.loads(row)
        base = [base] + [row]
        json_copy = ''
        while json_copy != json.dumps(base): 
            json_copy = json.dumps(base)
            base = test.explode_do_and_check(base)
            #print('After explode:', base)
            base = test.split(base)
            #print('After split:', base)    

    snail_fish_number = SnailFishNumber(json.dumps(base,separators=(',', ':')))
    solution = snail_fish_number.calc_magnitude()

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a("""[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""", 4140)
print('\n')
problem_a(PROGBLEM_INPUT_TXT, 3763)
print("\n")
