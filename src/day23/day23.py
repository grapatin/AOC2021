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
#..-.-.-.-..#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
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
        if maze[5,3] in 'aAE' and maze[4,3] in 'aAE' and maze[3,3] in 'aAE' and maze[2,3] in 'aAE':
             #This marks that it is either empty or a proper char is in place
            return True
    if x == 'B':
        if maze[5,5] in 'bBE' and maze[4,5] in 'bBE' and maze[3,5] in 'bBE' and maze[2,5] in 'bBE': #This marks that it is either empty or a proper char is in place
            return True
    if x == 'C':
        if maze[5,7] in 'cCE' and maze[4,7] in 'cCE' and maze[3,7] in 'cCE' and maze[2,7] in 'cCE': #This marks that it is either empty or a proper char is in place
            return True
    if x == 'D':
        if maze[5,9] in 'dDE' and maze[4,9] in 'dDE' and maze[3,9] in 'dDE' and maze[2,9] in 'dDE': #This marks that it is either empty or a proper char is in place
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

def move(posY,posX, pos_y_move, pos_x_move, maze :dict, move_string, char) -> int:
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
    if posY == 1 or pos_y_move == 1:
        distance = abs(posY-pos_y_move)+abs(posX-pos_x_move)
    else:
        if posX != pos_x_move:
            distance = posY-1+abs(posX-pos_x_move)+pos_y_move-1
        else:
            distance = 0
    move_string = 'moved:'+char+'from:y'+str(posY)+'x:'+str(posX)+'to:y'+str(pos_y_move)+'x:'+str(pos_x_move)+'cost:'+str(distance*cost)+'\n'
    #print_maze(maze)
    return distance*cost, move_string

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

def check_if_done(maze):
    if maze[2,3] == 'a' and maze[2,5] == 'b' and maze[2,7] == 'c' and maze[2,9] == 'd':
        return True
    else:
        return False

def walker(dict_storage_maze, cost_sofar, walk_string):
    global min_cost
    #Find all possible moves & store them in a list and iterate over list...
    #1st find chars and positions that maybe can move    
    #First move given movers
    if cost_sofar > min_cost:
        return 
    for _ in range(10):
        cost_row_move, walk_row = move_row_1(dict_storage_maze)
        cost_move_into_collumn, walk_collumn = move_into_collumns(dict_storage_maze)
        cost_sofar += cost_row_move + cost_move_into_collumn
        walk_string += walk_row + walk_collumn
    blocked_rows = []
    for posY in range(2,6):  #Now check for any collumn candidates that can move 
        possible_rows = [9,7,5,3]
        possible_row1_pos = [1,2,4,6,8,10,11]
        for posX in possible_rows:
            if posX not in blocked_rows:
                char = dict_storage_maze[posY, posX]
                if char in 'ABCD': #Possible mover
                    #can move to row 1
                    for pos_x_target in possible_row1_pos:
                        if check_if_char_can_reach_direction(posX, pos_x_target, dict_storage_maze):
                            can_it_move = True
                            #This is a candidate! Recursive jump!
                            maze_copy = dict_storage_maze.copy()
                            cost, move_string = move(posY,posX, 1, pos_x_target, maze_copy, '', char)
                            walker(maze_copy, cost_sofar+cost, walk_string+move_string)
                    blocked_rows.append(posX)
                elif char != 'E':
                    blocked_rows.append(posX)
    if check_if_done(dict_storage_maze):
        if cost_sofar < min_cost:
            print('new best found:', cost_sofar)
            print_maze(dict_storage_maze, walk_string)
            min_cost = cost_sofar

def move_row_1(dict_storage_maze):
    move_string = ''
    cost = 0
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
                        cost1, move_string2 = move(posY,posX, pos_y_move, pos_x_target, dict_storage_maze,move_string, char)
                        move_string += move_string2
                        cost += cost1
                        moved = True
    return cost, move_string

def move_into_collumns(dict_storage_maze) -> int:
    move_string = ''
    posY = 2
    blocked_rows = []
    cost = 0
    for _ in range(10):  #Now check for any collumn candidates that can move directly home, they should always do that
        possible_rows = [3,5,7,9]
        for posX in possible_rows:
            if posX not in blocked_rows:
                char = dict_storage_maze[posY, posX]
                if char in 'ABCD': #Possible mover
                    #can either move to row 1 or to home collumn
                    if check_if_coloumn_x_empty(char, dict_storage_maze):
                        #This one can maybe move home, try it
                        pos_x_target = get_target_collumn_for_x(char)
                        if check_if_char_can_reach_direction(posX, pos_x_target, dict_storage_maze):
                            if pos_x_target == posX: #Its already on correct position
                                cost2, move_string2 = move(posY,posX, posY, posX, dict_storage_maze, move_string, char)
                                cost += cost2
                                move_string += move_string2
                            else:
                                pos_y_move = get_target_row_for_y(char, dict_storage_maze)
                                cost2, move_string2 = move(posY,posX, pos_y_move, pos_x_target, dict_storage_maze, move_string, char)
                                cost += cost2
                                move_string += move_string2
                    else:
                        blocked_rows.append(posX)
        posY += 1
        if posY == 6:
            blocked_rows = []
            posY = 2
    return cost, move_string

def print_maze(maze :dict, move_string):
    for posY in range(0, 7):
        for posX in range(0, 13):
            if (posY, posX) in maze:
                print(maze[posY, posX], end='')
            else:
                print(' ', end='')
        print()
    print(move_string)

min_cost = 500000
def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    global min_cost
    solution = 0    
    dict_storage_maze = {}
    posY = 0
    for row in input_string.split('\n'):
        posX = 0
        for char in row:
            if char in 'ABCD':
                #dict_storage_maze[posY, posX] = CharacterClass(char)
                dict_storage_maze[posY, posX] = char
            else:
                dict_storage_maze[posY, posX] = char
            posX += 1
        posY += 1
    print('Start State:')
    print_maze(dict_storage_maze, '')
    min_cost = 500000
    walker(dict_storage_maze, 0, '')

    solution = min_cost

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 48541)
print("\n")
