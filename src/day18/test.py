import json


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
                                        #print('Explode these 2 values', array_d4)
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
        #print('Json', y)

        if explode == True:
            x_index = y.find('"x"')
            #find previous number and do the math
            y = add_to_previous_number(y, x_index, explode_v[0])
            #find next number and do the math      
            y = add_to_next_number(y, x_index, explode_v[1])
            y = y.replace('"x"', '0')
            base = json.loads(y)
            #print('Array:', base)
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
