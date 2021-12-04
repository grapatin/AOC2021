"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day04/input.txt").read_text()

EXAMPLE_INPUT1 = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
EXAMPLE_RESULT1 = 4512

class bingo_numer:
    def __init__(self, row, pos):
        self.row = row
        self.pos = pos
        self.found = False

class bingo_card:
    def __init__(self, rows_with_numbers):
        rows = rows_with_numbers.split('\n')
        row_n = 0
        pos_in_row = 0
        self.storage_dict = {}
        self.numbers_found_in_row = [0] * 5
        self.numbers_found_in_col = [0] * 5
        self.bingo_found = False
        for row in rows:
            numbers = row.split()
            pos_in_row = 0
            for number in numbers:
                self.storage_dict[number] = bingo_numer(row_n, pos_in_row)
                pos_in_row += 1
            row_n += 1

    def check_for_number(self, number):
        if number in self.storage_dict:
            b_n = self.storage_dict[number]
            b_n.found = True
            self.numbers_found_in_row[b_n.row] += 1
            self.numbers_found_in_col[b_n.pos] += 1

    def check_for_bingo(self):
        for row_check in self.numbers_found_in_row:
            if row_check == 5:
                self.bingo_found = True
                return True
        for col_check in self.numbers_found_in_col:
            if col_check == 5:
                self.bingo_found = True
                return True
        return False

    def calculate_score(self, last_number):
        sum_unmarked = 0
        for number in self.storage_dict:
            if self.storage_dict[number].found == False:
                sum_unmarked += int(number)
        return sum_unmarked*int(last_number)

class player_class:
    def __init__(self, input):
        parts = input.split('\n\n')
        self.numbers_to_draw = parts[0].split(',')
        self.bingo_cards = {}
        self.number_of_boards = len(parts)

        for bing_n in range(1, len(parts)):
            self.bingo_cards[bing_n] = bingo_card(parts[bing_n])
    
    def play(self):
        for drawn_number in self.numbers_to_draw:
            for bingo_card_n in self.bingo_cards:
                bingo_card = self.bingo_cards[bingo_card_n]
                bingo_card.check_for_number(drawn_number)
                if bingo_card.check_for_bingo() == True:
                    return bingo_card.calculate_score(drawn_number)
    
    def play_part2(self):
        boards_with_bingo = 0
        for drawn_number in self.numbers_to_draw:
            for bingo_card_n in self.bingo_cards:
                bingo_card = self.bingo_cards[bingo_card_n]
                if bingo_card.bingo_found == False:
                    bingo_card.check_for_number(drawn_number)
                    if bingo_card.check_for_bingo() == True:
                        boards_with_bingo += 1
                        if boards_with_bingo == self.number_of_boards - 1:
                            return bingo_card.calculate_score(drawn_number)

def problem_a(input_string, expected_result):
    """Problem A solved function
    """

    player = player_class(input_string)

    solution = player.play()

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result) #35056

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 4662)
print("\n")


def problem_b(input_string, expected_result):
    """Problem A solved function
    """

    player = player_class(input_string)

    solution = player.play_part2()

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result) #35056


problem_b(EXAMPLE_INPUT1, 1924)
problem_b(PROGBLEM_INPUT_TXT, 12080)
print("\n")