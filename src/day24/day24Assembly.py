"""
Template code
"""
import sys
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day24/input.txt").read_text()

EXAMPLE_INPUT1 = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""
EXAMPLE_RESULT1 = 4

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps


class AssemblyProcessor:
    """Class for Advent Of Code assembly language processing
    """
    def __init__(self, code_array, input_number):
        self.registry_dict = {
            'w' : 0,
            'x' : 0,
            'y' : 0,
            'z' : 0
        }
        self._program_counter = 0
        self._code_array = code_array
        self._length = len(code_array)
        input_array = []
        for char in str(input_number):
            input_array.append(char)
        self.input_array = input_array

    def printer(self):
        print ('w:', self.registry_dict['w'], 'x:', self.registry_dict['x'], 'y:', self.registry_dict['y'], 'z:', self.registry_dict['z'],end='')

    def _inp(self, code_string):
        """snd X
        plays a sound equal to X
        """
        parts = code_string.split()
        var_part = parts[1]
        self.registry_dict[var_part]  = int(self.input_array.pop(0))
        self._program_counter += 1
        print('** INPUT **')

    def _add(self, code_string):
        """add X Y
        increases register X by the value of Y.
        """
        parts = code_string.split()
        x_part = parts[1]
        y_part = parts[2]
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        if x_part not in self.registry_dict:
            self.registry_dict[x_part] = 0
        self.registry_dict[x_part] += int(y_part)
        self._program_counter += 1

    def _mul(self, code_string):
        """mul X Y
        sets register X to the result of multiplying the value contained in
        register X by the value of Y.
        """
        parts = code_string.split()
        x_part = parts[1]
        y_part = parts[2]
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        if x_part not in self.registry_dict:
            self.registry_dict[x_part] = 0
        self.registry_dict[x_part] *= int(y_part)
        self._program_counter += 1

    def _mod(self, code_string):
        """mod X Y
        sets register X to the remainder of dividing the value contained in
        register X by the value of Y (that is, it sets X to the result of X modulo Y).
        """
        parts = code_string.split()
        x_part = parts[1]
        y_part = parts[2]
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        if x_part not in self.registry_dict:
            self.registry_dict[x_part] = 0
        self.registry_dict[x_part] %= int(y_part)
        self._program_counter += 1

    def _div(self, code_string):
        """mod X Y
        sets register X to the remainder of dividing the value contained in
        register X by the value of Y (that is, it sets X to the result of X modulo Y).
        """
        parts = code_string.split()
        x_part = parts[1]
        y_part = parts[2]
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        if x_part not in self.registry_dict:
            self.registry_dict[x_part] = 0
        self.registry_dict[x_part] = int(self.registry_dict[x_part] / int(y_part))
        self._program_counter += 1

    def _eql(self, code_string):
        """eql X Y
        If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a
        """
        parts = code_string.split()
        x_part_i = parts[1]
        y_part = parts[2]
        if x_part_i in self.registry_dict:
            x_part = self.registry_dict[x_part_i]
        else:
            x_part = int(x_part_i)
            
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        else:
            y_part = int(y_part)

        if x_part == y_part:
            self.registry_dict[x_part_i] = 1
        else:
            self.registry_dict[x_part_i] = 0
    
        self._program_counter += 1

    def execute(self):
        """Executor of next command in code_string
        """
        code_string = self._code_array[self._program_counter]
        self.printer()
        print(' PC:', self._program_counter, code_string)
        if 'inp' in code_string:
            self._inp(code_string)
        elif 'add' in code_string:
            self._add(code_string)
        elif 'mul' in code_string:
            self._mul(code_string)
        elif 'mod' in code_string:
            self._mod(code_string)
        elif 'div' in code_string:
            self._div(code_string)
        elif 'eql' in code_string:
            self._eql(code_string)
        else:
            assert False

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    code_strings = string_worker(input_string)
    start_value = 97919997299495
    #             12345678901234
    #             979196 7529 6495
    #             979199 7529 9495
    #             979199 9729 9495
    result = 1

    while (result != 0):
        runner_instance: AssemblyProcessor = AssemblyProcessor(code_strings, start_value)
        try:
            while True:
                runner_instance.execute()
        except:
            result = runner_instance.registry_dict['z']
            if result == 0:
                solution = start_value
            else:
                start_value += 31111111111111

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

#problem_a(EXAMPLE_INPUT1, 0)
problem_a(PROGBLEM_INPUT_TXT, 2951)  #92919675296445 to low
print("\n")
