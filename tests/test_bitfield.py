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


class Test_Insert(unittest.TestCase):
    def test_insert_low(self):
        """Inserting a few bits in the lowest part of the word. """
        low_bits = BitField(0, 3)
        self.assertEqual(low_bits.insert(15, 0), 15)  # All the bits to 1
        # Slip it in without disturbing higher bits
        self.assertEqual(low_bits.insert(0b1010, 0b1111_0000), 0b1111_1010)