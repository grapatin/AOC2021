"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

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
    snail_fish_base :SnailFishNumber 
    snail_fish_base = SnailFishNumber(rows.pop(0))
    
    solution = snail_fish_base.calc_magnitude()

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

#problem_a('[[1,2],3]', EXAMPLE_RESULT1)
#problem_a('[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]', EXAMPLE_RESULT1)

problem_a("""[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]""", 445)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
