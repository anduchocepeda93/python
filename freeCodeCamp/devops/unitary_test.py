import math

def area_circulo(radio):
    return math.pi * radio**2

# Test con unittest
import unittest

class TestArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area_circulo(1), math.pi)

if __name__ == "__main__":
    unittest.main()
