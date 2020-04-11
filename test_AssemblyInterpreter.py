from unittest import TestCase

from AssemblyInterpreter import simple_assembler


class Test(TestCase):
    def test_simple_assembler(self):
        code = '''\
        mov a 5
        inc a
        dec a
        dec a
        jnz a -1
        inc a'''
        self.assertEqual(simple_assembler(code.splitlines()), {'a': 1})
