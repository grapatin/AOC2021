import itertools
from typing import DefaultDict


def create_24_variants(input_row_array):
    row = 0
    result_dict = {}
    for input_array in input_row_array.split('\n'):
        input_array = [int(number) for number in input_array.split(',')]
        x,y,z = input_array
        output_array = input_array      #1
        output_array.append([-1*y,x,z]) #2
        output_array.append([-1*x,-1*y,z])
        output_array.append([y,-1*x,z])

        output_array.append([-1*x,y,-1*z])         
        output_array.append([-1*y,-1*x,-1*z]) 
        output_array.append([x,-1*y,-1*z])
        output_array.append([y,x,-1*z])

        output_array.append([x,z,-1*y])
        output_array.append([-1*z,x,-1*y]) 
        output_array.append([-1*x,-1*z,-1*y])
        output_array.append([z,-1*x,-1*y])

        output_array.append([x,-1*z,y])
        output_array.append([z,x,y]) 
        output_array.append([-1*x,z,y])
        output_array.append([-1*z,-1*x,y])

        output_array.append([-1*z,y,x])
        output_array.append([-1*y,-1*z,x]) 
        output_array.append([z,-1*y,x])
        output_array.append([y,z,x])

        output_array.append([z,y,-1*x])
        output_array.append([-1*y,z,-1*x]) 
        output_array.append([-1*z,-1*y,-1*x])
        output_array.append([y,-1*z,-1*x])
        result_dict[row] = output_array
        row += 1
        
    return result_dict

input = """-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7"""

result_dict = create_24_variants(input)

for i in range(24):
    for row in result_dict:
        print(result_dict[row][i])
    print()
