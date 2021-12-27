"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from os import walk
from pathlib import Path
from typing import Dict, Union

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day23/input.txt").read_text()

EXAMPLE_INPUT1 = """#############
#D.-.-.-.-.D#
###B#E#E#E###
  #D#E#E#E#
  #D#E#E#E#
  #A#E#E#E#
  #########

#############
#..-.-.-.-..#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########"""
EXAMPLE_RESULT1 = 44169

class CharacterClass:
    def __init__(self, char):
        if char == 'A':
            self.cost = 1
            self.target_collum = 3
            self.moved = False
        elif char == 'B':
            self.cost = 10
            self.target_collum = 5
            self.moved = False
        elif char == 'C':
            self.cost = 100
            self.target_collum = 7
            self.moved = False
        elif char == 'D':
            self.cost = 1000
            self.target_collum = 9
            self.moved = False

class StateClass:
    def __init__(self):
        self.a_empty = False
        self.b_empty = False
        self.c_empty = False
        self.d_empty = False

def check_if_coloumn_x_empty(x, maze):
    if x == 'A':
        if maze[5,3] in 'aE': #This marks that it is either empty or a proper char is in place
            return True
    if x == 'B':
        if maze[5,5] in 'bE': #This marks that it is either empty or a proper char is in place
            return True
    if x == 'C':
        if maze[5,7] in 'cE': #This marks that it is either empty or a proper char is in place
            return True
    if x == 'D':
        if maze[5,9] in 'dE': #This marks that it is either empty or a proper char is in place
            return True
    return False
            
def get_target_collumn_for_x(x):
    if x == 'A':
        return 3
    if x == 'B':
        return 5
    if x == 'C':
        return 7
    if x == 'D':
        return 9

def get_target_row_for_y(x, maze):
    if x == 'A':
        Xpos = 3
    if x == 'B':
        Xpos = 5
    if x == 'C':
        Xpos = 7
    if x == 'D':
        Xpos = 9
    
    for row in range(5, 1, -1):
        char = maze[row, Xpos]
        if char == 'E': #Position empty
            return row

    print('Error in get_target_row_for_y')

def move(posY,posX, pos_y_move, pos_x_move, maze :dict): #-> (dict, int):
    char_to_move :str = maze[posY, posX]
    if posY > 1:
        maze[posY, posX] = 'E'
    else:
        maze[posY, posX] = '.'
    
    if pos_y_move > 1:
        maze[pos_y_move, pos_x_move] = char_to_move.lower()
    else:
        maze[pos_y_move, pos_x_move] = char_to_move


    cost = 1
    if char_to_move == 'B':
        cost = 10
    elif char_to_move == 'C':
        cost = 100
    elif char_to_move == 'D':
        cost = 1000
    
    distance = abs(posY-pos_y_move)+abs(posX-pos_x_move)
    return maze, distance*cost

def check_if_char_can_reach_direction(current_x, target_x, maze :dict) -> bool:
    if target_x > current_x:
        direction = +1
    else:
        direction = -1
    for pos_x_move in range(current_x+direction, target_x + direction, direction):
        next_char = maze[1, pos_x_move] #we are only checking row 1
        if next_char not in '.-':
            return False
    return True

def return_list_of_possible_pos_in_row_1(currrent_x :int,  maze:dict) -> list:
    possible_destinations :list = []
    for pos_x in range(currrent_x, 12):
        next_char =  maze(2, pos_x)
        if next_char == ('.'):
            possible_destinations.append([2,pos_x])
        elif next_char == ('-'):
            pass
        else:
            break
    for pos_x in range(currrent_x, 0):
        next_char =  maze(2, pos_x)
        if next_char == ('.'):
            possible_destinations.append([2,pos_x])
        elif next_char == ('-'):
            pass
        else:
            break


def walker(dict_storage_maze):
    #Find all possible moves & store them in a list and iterate over list...
    #1st find chars and positions that maybe can move
    possible_movers = {}
    posY = 1
    moved = True
    while (moved):        
        moved = False
        for posX in range(1, 12): #check for candidates in upper row, these can only move if destination is available
            char = dict_storage_maze[posY, posX]
            if char in 'ABCD': #char that has moved already
                if check_if_coloumn_x_empty(char, dict_storage_maze):
                    #This one can maybe move home, try it
                    pos_x_target = get_target_collumn_for_x(char)

                    if check_if_char_can_reach_direction(posX, pos_x_target, dict_storage_maze):
                        pos_y_move = get_target_row_for_y(char, dict_storage_maze)
                        dict, cost = move(posY,posX, pos_y_move, pos_x_target, dict_storage_maze)
                        moved = True
    
    all_rows = [3,5,7,9]
    posY = 2
    moved = True
    while (moved):  #Now check for any collumn candidates that can move directly home, they should always do that
        moved = False
        possible_rows = all_rows
        for posX in possible_rows:
            char = dict_storage_maze[posY, posX]
            if char in 'ABCD': #Possible mover
                #can either move to row 1 or to home collumn
                if check_if_coloumn_x_empty(char, dict_storage_maze):
                    #This one can maybe move home, try it
                    pos_x_target = get_target_collumn_for_x(char)
                    if check_if_char_can_reach_direction(posX, pos_x_target, dict_storage_maze):
                        pos_y_move = get_target_row_for_y(char, dict_storage_maze)
                        dict, cost = move(posY,posX, pos_y_move, pos_x_target, dict)
                        moved = True
                else:
                    all_rows.remove(posX)
            elif '#' in char:
                #remove row from possible_rows
                all_rows.remove(posX)

def print_maze(maze :dict):
    for posY in range(0, 7):
        for posX in range(0, 13):
            if (posY, posX) in maze:
                print(maze[posY, posX], end='')
            else:
                print(' ', end='')
        print()



def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    parts = input_string.split('\n\n')

    dict_storage_maze = {}

    posY = 0
    for row in parts[0].split('\n'):
        posX = 0
        for char in row:
            if char in 'ABCD':
                #dict_storage_maze[posY, posX] = CharacterClass(char)
                dict_storage_maze[posY, posX] = char
            else:
                dict_storage_maze[posY, posX] = char
            posX += 1
        posY += 1

    dict_possible_positions = {}
    for row in parts[1].split('\n'):
        posX = 0
        for char in row:
            if char in '.':
                dict_possible_positions[posY, posX] = '.'
            posX += 1
        posY += 1

    walker(dict_storage_maze)
    print_maze(dict_storage_maze)


    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
