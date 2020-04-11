class AssemblyInterpreter:

    def __init__(self):
        self.registers = {}
        self.program_counter = 0
        self.instructions = {
            'mov': self._move,
            'inc': self._increment,
            'dec': self._decrement,
            'jnz': self._jump_not_zero
        }

    def resolve(self, operand):
        return self.registers[operand] if operand in self.registers else int(operand)

    def execute(self, program):

        while self.program_counter < len(program):
            parsed = program[self.program_counter].split()
            current_instruction = parsed[0]
            args = parsed[1:]
            self.program_counter += 1
            self.instructions[current_instruction](*args)

        return self.registers

    def _move(self, x, y):
        self.registers[x] = self.resolve(y)

    def _increment(self, x):
        self.registers[x] += 1
        pass

    def _decrement(self, x):
        self.registers[x] -= 1
        pass

    def _jump_not_zero(self, x, y):
        if(self.resolve(x) != 0):
            self.program_counter += self.resolve(y) - 1
        pass

def simple_assembler(program):
	return AssemblyInterpreter().execute(program)