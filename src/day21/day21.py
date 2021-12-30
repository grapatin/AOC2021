"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

from numpy.lib.function_base import append

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day21/input.txt").read_text()

EXAMPLE_INPUT1 = """"""
EXAMPLE_RESULT1 = 1514


def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    player_1_pos = input_string[0] - 1
    player_2_pos = input_string[1] - 1

    dice = list(range(1,101))
    player_list = list(range(1,11))


    score_1 = 0
    score_2 = 0
    
    dice_position = 0
    dice_rolls = 0
    active_player = 'player1'

    while score_1 < 1000 and score_2 < 1000:
        if active_player == 'player1':
            player_1_pos += dice[dice_position % 100] + dice[(dice_position + 1) % 100] + dice[(dice_position + 2) % 100]
            score_1 += player_list[player_1_pos % 10]
            active_player = 'player2'
        else:
            player_2_pos += dice[dice_position % 100] + dice[(dice_position + 1) % 100] + dice[(dice_position + 2) % 100]
            score_2 += player_list[player_2_pos % 10]
            active_player = 'player1'

        dice_position += 3
        dice_rolls += 3

    min_value = min(score_1, score_2)

    solution = min_value*dice_rolls

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a([4, 8], 739785)
problem_a([5, 8], 1067724)
print("\n")

MAX_SCORE = 21

class Throws:
    def __init__(self, p1_start, p2_start):
        self.throw_number = 0
        self.active_player = 'p1'
        self.not_active_player = 'p2'
        self.throw = []
        p1 = PlayerObject('p1', p1_start)
        p2 = PlayerObject('p2', p2_start)
        self.throw.append([PlayerClass(p1, p2)])
        self.possibilities_dict = self.calculate_probability()
        self.winner_uni = {
            'p1' : 0,
            'p2' : 0,
        }

    def throw_f(self):
        player_object :PlayerObject
        not_active_player_object :PlayerObject
        player_rep :PlayerClass
        new_player_rep :PlayerClass

        #get all active player_rep for this throw
        next_throw = self.throw_number + 1
        self.throw.append([])
        
        for player_rep in self.throw[self.throw_number]:
            new_player_array = []
            #get active player object
            player_object = player_rep.player_dict[self.active_player]
            not_active_player_object = player_rep.player_dict[self.not_active_player]
            #add all new alternatives
            for move_possibility in self.possibilities_dict:
                move_d = move_possibility
                new_universes = self.possibilities_dict[move_possibility]
                new_clone = player_object.move_and_clone(move_d, new_universes)
                if new_clone.score < MAX_SCORE:
                    new_player_array.append(new_clone)
                else:
                    #store away as a victory for active player
                    self.winner_uni[self.active_player] += new_clone.no_universes
            #store all new alternatives in next throw
            for new_p_object in new_player_array:
                not_active_player_object.no_universes = new_p_object.no_universes
                if self.active_player == 'p1':
                    new_player_rep = PlayerClass(new_p_object, not_active_player_object)
                else:
                    new_player_rep = PlayerClass(not_active_player_object, new_p_object)
                self.throw[next_throw].append(new_player_rep)
        self.throw_number = next_throw
        self.active_player, self.not_active_player = self.not_active_player, self.active_player

    def calculate_probability(self):
        alternatives = [1,2,3]
        storage_dict = {}
        for dice_outcome1 in alternatives:
            for dice_outcome2 in alternatives:
                for dice_outcome3 in alternatives:
                    sum = dice_outcome1+dice_outcome2+dice_outcome3
                    if sum not in storage_dict:
                        storage_dict[sum] = 1
                    else:
                        storage_dict[sum] += 1
        return storage_dict

class PlayerClass:
    def __init__(self, p1, p2) -> None:
        self.player_dict = {
            'p1' : p1,
            'p2' : p2
        }

class PlayerObject:
    def __init__(self, player, pos, score = 0, no_universes = 1):
        self.player = player
        self.pos = pos
        self.score = score
        self.no_universes = no_universes
        self.player_score_list = list(range(1,11))

    def move_and_clone(self, move, no_universes):
        new_pos = self.pos + move
        new_score = self.score + self.player_score_list[new_pos % 10]
        new_no_universes = self.no_universes*no_universes
        new_score_keeper = PlayerObject(self.player, new_pos, new_score, new_no_universes)
        return new_score_keeper


def playerFunction(throw :Throws):

    while(True):
        throw.throw_f()
        if len(throw.throw[throw.throw_number]) == 0:
            #we are done
            return

def problem_b(input_string, expected_result):
    """Problem A solved function
    """

    throw = Throws(input_string[0],input_string[1])
    playerFunction(throw)

    print('p1:', throw.winner_uni['p1'])
    print('p2:', throw.winner_uni['p2'])


    max_uni = max(throw.winner_uni['p1'],throw.winner_uni['p2'])

    solution = max_uni

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b([4, 8], 444356092776315)
                #5136615862079541867
#problem_b([5, 8], 0)
print("\n")