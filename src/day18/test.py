import json

start_string = """[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]"""

start_string_2 = """[1,[[9,[5,8]],[[2,0],0]]]
[[[6,4],6],[[1,[7,3]],[[0,1],[4,9]]]]
[[[7,3],[8,6]],[[4,[1,2]],7]]
[[[2,[4,5]],[[7,1],2]],1]
[[[[4,4],[4,6]],9],[[4,2],6]]
[[[9,8],[[4,0],0]],[[2,[5,1]],[[9,6],[9,2]]]]
[[[6,[9,0]],0],[6,[[5,8],3]]]
[[[[7,3],[5,4]],0],[3,[[0,6],3]]]
[5,[[0,0],[[4,8],[8,6]]]]
[[[3,[9,2]],9],[5,[0,6]]]
[[[[6,3],[3,2]],[5,9]],2]
[[[0,4],7],[8,[8,[4,2]]]]
[[[8,[8,0]],9],[[1,[6,3]],[4,2]]]
[[[[5,4],[1,5]],[1,3]],[[[9,0],[7,4]],9]]
[[[5,[4,2]],[[9,2],3]],[[[6,2],[6,8]],[[2,4],[9,4]]]]
[[9,6],[0,[[1,1],9]]]
[[[8,[5,9]],[2,9]],[0,[[7,6],[7,6]]]]
[[[5,[4,8]],[[7,7],[2,2]]],[[[2,6],[5,7]],[0,[6,2]]]]
[[[[9,3],5],3],[[[1,5],2],[3,3]]]
[[[2,[1,1]],[[5,8],[7,1]]],[[9,7],5]]
[[9,9],3]
[[[5,[6,1]],9],[1,[9,3]]]
[[[[1,2],7],[[6,8],[4,1]]],[[2,3],[6,3]]]
[[[[9,3],[7,9]],2],[[9,[3,4]],[[2,6],[7,0]]]]
[[8,[4,9]],[[2,[5,6]],6]]
[3,[[[9,7],7],[[2,6],4]]]
[[[[3,4],[0,8]],[[6,4],[2,6]]],[[[1,4],[5,4]],8]]
[8,[[0,[5,5]],[[1,2],1]]]
[[[5,[8,1]],[[1,8],[4,0]]],[8,8]]
[[[9,5],3],[[7,9],[1,6]]]
[[[[1,1],1],[[2,0],[2,5]]],5]
[[3,[[5,4],[7,4]]],[[4,4],[1,9]]]
[[0,[[7,4],[7,2]]],[[8,0],[5,9]]]
[0,[[[1,2],4],[[1,0],[6,4]]]]
[[[[6,6],[9,8]],3],[[[5,5],[1,6]],[8,[5,3]]]]
[[7,[[5,6],0]],[5,[[9,2],4]]]
[[[4,[4,5]],[7,[4,5]]],[[[9,8],8],[[8,2],[3,0]]]]
[[[8,[0,5]],[[0,4],[8,9]]],[8,[4,6]]]
[[[4,[9,7]],[[7,4],[7,1]]],[[[8,4],0],[[6,9],[9,0]]]]
[[3,6],[[3,[4,6]],[[6,0],0]]]
[3,[1,[[4,0],1]]]
[[[9,9],[0,[6,3]]],[3,2]]
[7,4]
[2,6]
[[[3,[7,8]],7],[[0,[2,5]],[1,1]]]
[0,5]
[8,[8,[[2,4],5]]]
[[[[8,2],1],[9,0]],[[[0,8],[3,0]],9]]
[[[[7,0],1],[[0,1],[6,7]]],[[[3,1],[8,3]],7]]
[8,0]
[[[7,[1,3]],[7,[7,2]]],[[9,0],4]]
[[[[0,3],5],[[1,0],8]],[[0,2],9]]
[[5,[[7,6],[7,2]]],5]
[[[[2,8],[5,4]],[1,6]],[[8,8],[[5,2],4]]]
[[[[1,5],[1,8]],1],[[6,[2,4]],5]]
[[[[9,7],[6,3]],2],[[3,[4,4]],[3,4]]]
[[[9,2],[2,9]],[[[0,7],[0,8]],[[0,2],[6,7]]]]
[[[[1,1],3],[[1,4],[8,9]]],[[8,[8,6]],[7,7]]]
[5,[[1,[8,8]],[6,3]]]
[[[1,4],3],7]
[[[[0,1],[2,0]],2],[[8,8],7]]
[[[[2,8],[4,4]],[[5,6],8]],[[[5,3],1],7]]
[[9,[0,[8,3]]],[5,6]]
[[[0,[8,9]],[6,[8,1]]],[[[2,3],8],[[4,0],8]]]
[[2,[5,4]],[[7,4],[[5,0],3]]]
[[[[1,1],2],[[3,0],[7,7]]],[[1,[3,8]],2]]
[[[1,4],[6,[2,4]]],[[5,5],0]]
[[[[4,4],8],[[4,3],[3,5]]],[[7,1],2]]
[[[4,[0,8]],9],[[[6,9],2],8]]
[[[[0,0],1],[1,1]],[2,[[0,0],[7,7]]]]
[[2,[5,5]],9]
[[[[5,8],[7,7]],[[9,8],5]],[[3,5],[8,8]]]
[[5,[3,[3,9]]],[3,[9,8]]]
[[8,[4,6]],[[5,0],[9,2]]]
[[[3,[1,8]],[4,5]],[[0,[5,9]],6]]
[9,[[1,1],0]]
[[[[6,1],[9,2]],4],[5,3]]
[[[[3,0],[0,5]],[1,[5,2]]],[[[2,0],[0,2]],[[6,4],4]]]
[[[[1,1],[4,6]],[[3,8],[3,2]]],[[[4,3],7],[2,[7,8]]]]
[4,[[1,5],5]]
[8,[[1,1],0]]
[[[[8,4],[9,9]],[3,[6,6]]],[[[7,9],[9,7]],7]]
[[2,5],[8,[3,8]]]
[[[6,1],[7,[3,5]]],9]
[[1,[[3,6],[1,0]]],[[[2,8],8],[4,[2,7]]]]
[[[3,[6,9]],[[9,6],[0,8]]],[[5,[6,4]],[[3,4],1]]]
[[[[7,7],1],[5,[2,5]]],[[3,7],[[4,7],3]]]
[[4,[3,[7,2]]],[[[8,8],[5,8]],8]]
[[3,[[9,9],6]],6]
[[6,7],[2,9]]
[[[9,7],[1,[4,0]]],[[[3,4],0],[1,2]]]
[9,[[8,[8,4]],3]]
[[[4,[4,1]],[[4,7],[2,3]]],[8,[5,[1,5]]]]
[7,[2,[4,1]]]
[[[[1,5],7],[5,9]],8]
[[[[1,5],[0,4]],8],[[[7,0],6],[8,3]]]
[[[7,[3,5]],0],[8,[9,[5,6]]]]
[[1,[[5,1],5]],[[5,1],[9,[3,0]]]]
[3,[[[8,5],[7,5]],[9,4]]]
[[[3,3],[2,[5,9]]],7]"""

rows = start_string_2.split('\n')

first_row = rows.pop(0)
base = json.loads(first_row)

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

def explode_do_and_check(base):
    explode_v = [0, 0]
    explode = True
    while (explode == True):
        explode = False
        for array_d1 in base:
            if isinstance(array_d1, list):
                for array_d2 in array_d1:
                    if isinstance(array_d2, list):
                        for array_d3 in array_d2:
                            if isinstance(array_d3, list):
                                for index4, array_d4 in enumerate(array_d3):
                                    if isinstance(array_d4, list):
                                        print('Explode these 2 values', array_d4)
                                        explode_v = array_d4
                                        array_d3[index4] = 'x'
                                        explode = True
                                        break
                            if explode:
                                break
                    if explode:
                        break
            if explode:
                break
        y = json.dumps(base)                        
        print('Json', y)

        if explode == True:
            x_index = y.find('"x"')
            #find previous number and do the math
            y = add_to_previous_number(y, x_index, explode_v[0])
            #find next number and do the math      
            y = add_to_next_number(y, x_index, explode_v[1])
            y = y.replace('"x"', '0')
            base = json.loads(y)
            print('Array:', base)
    return base

def add_to_previous_number(w_string, index, add_me):
    #find previous number and do the math
    for pos in range(index, 1, -1):
        if w_string[pos] in '0123456789':
            if w_string[pos -1] in '0123456789':
                t_number = int(w_string[pos-1:pos+1])
                t_number += add_me
                t_string = str(t_number)
                w_string = w_string[:pos-1] + t_string + w_string[pos+1:]
            else:
                t_number = int(w_string[pos]) + add_me
                t_string = str(t_number)
                w_string = w_string[:pos] + t_string + w_string[pos+1:]
            break
    return w_string

def add_to_next_number(w_string, index, add_me):
    #find previous number and do the math
    for pos in range(index, len(w_string) - 1):
        if w_string[pos] in '0123456789':
            if w_string[pos+1] in '0123456789':
                t_number = int(w_string[pos:pos+2])
                t_number += add_me
                t_string = str(t_number)
                w_string = w_string[:pos] + t_string + w_string[pos+2:]
            else:
                t_number = int(w_string[pos]) + add_me
                t_string = str(t_number)
                w_string = w_string[:pos] + t_string + w_string[pos+1:]
            break
    return w_string

def split(base):
    y = json.dumps(base)
    for index in range(len(y) -1):
        if y[index] in '0123456789' and y[index+1] in '0123456789':
            #split this number
            numb = int(y[index:index+2])
            left = int(numb/2)
            rigth = int(numb/2)
            if numb % 2 != 0:
                rigth += 1
            y = y[:index] + '[' + str(left) + ',' + str(rigth) + ']' + y[index+2:]
            break
    base = json.loads(y)
    return base

for row in rows:
    row = json.loads(row)
    base = [base] + [row]
    json_copy = ''
    while json_copy != json.dumps(base): 
        json_copy = json.dumps(base)
        base = explode_do_and_check(base)
        print('After explode:', base)
        base = split(base)
        print('After split:', base)

print('This is the string to calculate Magnitude on:\n',base)
print('This is the string to calculate Magnitude on:\n',json.dumps(base,separators=(',', ':')))

snail_fist_number = SnailFishNumber(json.dumps(base,separators=(',', ':')))
print('Got Magnitude:',snail_fist_number.calc_magnitude())