import unittest
from Complex.py import Complex

class Complex:

    def test_add(self, other):
        number_1 = Complex(3, 3)
        number_2 = Complex(4, 8)
        expected = Complex(7, 11)

        self.assertEqual(str(expected), str(actual))


    def test_sub(self, other):
        number_1 = Complex(3, 3)
        number_2 = Complex(4, 8)
        expected = Complex(7, 11)

        self.assertEqual(str(expected), str(actual))

    def test_mul(self, other):
        number_1 = Complex(3, 4)
        number_2 = Complex(4, 8)
        expected = Complex(12, 48)

        self.assertEqual(str(expected), str(actual))
    
if __name__ == "__main__":
    TestComplex()


