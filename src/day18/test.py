import json

start_string = """[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]"""

start_string_2 = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""

rows = start_string_2.split('\n')

first_row = rows.pop(0)
base = json.loads(first_row)

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

print(base)

