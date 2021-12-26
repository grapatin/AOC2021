"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

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
problem_a([5, 8], 0)
print("\n")


def problem_b(input_string, expected_result):
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

    while score_1 < 21 and score_2 < 21:
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


problem_b([4, 8], 444356092776315)
problem_b([5, 8], 0)
print("\n")