"""Unit tests for assembler phase 1"""

import unittest
import context
from asm.assembler_phase1 import *


class TestResolve(unittest.TestCase):

    def test_sample_resolve(self):
        lines = """
        # comment line at address 0

        # Blank line above is also address 0
        start:   # and start should also be address 0
        next:    ADD/P   r0,r1,r2[15]  # Still address 0
                 SUB     r1,r2,r3      # Address 1
        after:   MUL     r1,r2,r3[15]  # Address 2
        finally:  # Address 3
        fini:    DIV     r1,r2,r3      # Address 3
        """.split("\n")
        labels = resolve(lines)
        self.assertEqual(labels["start"], 0)
        self.assertEqual(labels["next"], 0)
        self.assertEqual(labels["after"], 2)
        self.assertEqual(labels["finally"], 3)
        self.assertEqual(labels["fini"], 3)


if __name__ == "__main__":
    unittest.main()