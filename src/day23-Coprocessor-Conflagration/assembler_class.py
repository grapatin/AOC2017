"""
Assembler class
"""

class AssemblyProcessor:
    """Class for Advent Of Code assembly language processing
    """
    def __init__(self, code_array):
        self.registry_dict = { 'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0
        }
        self.program_counter = 0
        self._code_array = code_array
        self._length = len(code_array)
        self._sound = 0


    def _snd(self, code_string):
        """snd X
        plays a sound equal to X
        """
        parts = code_string.split()
        x_part = parts[1]
        if x_part in self.registry_dict:
            x_part = self.registry_dict[x_part]
        self._sound = int(x_part)
        self.program_counter += 1

    def _set(self, code_string):
        """set X Y
        sets register X to the value of Y
        """
        parts = code_string.split()
        x_part = parts[1]
        y_part = parts[2]
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        self.registry_dict[x_part] = int(y_part)
        self.program_counter += 1

    def _add(self, code_string):
        """add X Y
        increases register X by the value of Y.
        """
        parts = code_string.split()
        x_part = parts[1]
        y_part = parts[2]
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        self.registry_dict[x_part] += int(y_part)
        self.program_counter += 1

    def _sub(self, code_string):
        """sub X Y
        decreases register X by the value of Y.
        """
        parts = code_string.split()
        x_part = parts[1]
        y_part = parts[2]
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        self.registry_dict[x_part] -= int(y_part)
        self.program_counter += 1


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
        self.program_counter += 1

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
        self.program_counter += 1

    def _rcv(self, code_string):
        """_rcv X
        Recovers the frequency of the last sound played, but only when
        the value of X is not zero. (If it is zero, the command does nothing.)
        """
        parts = code_string.split()
        x_part = parts[1]
        if x_part in self.registry_dict:
            x_part = self.registry_dict[x_part]
        if int(x_part) != 0:
            print('Recovery run with value', self._sound)
            raise ValueError(self._sound)
        self.program_counter += 1

    def _jnz(self, code_string):
        """jnz X Y
        jumps with an offset of the value of Y, but only if the value of X is not
        zero. (An offset of 2 skips the next instruction, an offset of -1 jumps
        to the previous instruction, and so on.)
        """
        parts = code_string.split()
        x_part = parts[1]
        y_part = parts[2]
        if x_part in self.registry_dict:
            x_part = self.registry_dict[x_part]
        if y_part in self.registry_dict:
            y_part = self.registry_dict[y_part]
        if int(x_part) != 0:
            self.program_counter += int(y_part)
        else:
            self.program_counter += 1

    def execute(self):
        """Executor of next command in code_string
        """
        code_string = self._code_array[self.program_counter]
        if 'snd' in code_string:
            self._snd(code_string)
        elif 'set' in code_string:
            self._set(code_string)
        elif 'add' in code_string:
            self._add(code_string)
        elif 'mul' in code_string:
            self._mul(code_string)
        elif 'mod' in code_string:
            self._mod(code_string)
        elif 'rcv' in code_string:
            self._rcv(code_string)
        elif 'jnz' in code_string:
            self._jnz(code_string)
        elif 'sub' in code_string:
            self._sub(code_string)
        else:
            assert False
