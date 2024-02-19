"""Unit tests for bitfield.py"""
import unittest
from instruction_set.bitfield import BitField

class Test_Extract(unittest.TestCase):

    def test_extract_low(self):
        """Extract low 3 bits"""
        low_bits = BitField(0,3)
        self.assertEqual(low_bits.extract(0b10101010101), 0b101)

    def test_middle_bits(self):
        """Extract 5 bits from the middle of a word"""
        middle_bits = BitField(5,9)
        self.assertEqual(middle_bits.extract(0b1010101101101011), 0b11011)