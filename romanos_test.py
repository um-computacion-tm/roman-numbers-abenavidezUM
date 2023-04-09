import unittest
from romanos1 import to_roman
from romanos1 import to_decimal
        
class TestDecimanalToRoman(unittest.TestCase):
    def test_1(self):
        resultado = to_roman(1)
        self.assertEqual(resultado, "I")
    def test_2(self):
        resultado = to_roman(2)
        self.assertEqual(resultado, "II")
    def test_3(self):
        resultado = to_roman(3)
        self.assertEqual(resultado, "III")
    def test_4(self):
        resultado = to_roman(4)
        self.assertEqual(resultado, "IV")
    def test_5(self):
        resultado = to_roman(5)
        self.assertEqual(resultado, "V")
    def test_6(self):
        resultado = to_roman(6)
        self.assertEqual(resultado, "VI")
    def test_7(self):
        resultado = to_roman(7)
        self.assertEqual(resultado, "VII")
    def test_8(self):
        resultado = to_roman(8)
        self.assertEqual(resultado, "VIII")
    def test_9(self):
        resultado = to_roman(9)
        self.assertEqual(resultado, "IX")
    def test_10(self):
        resultado = to_roman(10)
        self.assertEqual(resultado, "X")
    def test_11(self):
        resultado = to_roman(50)
        self.assertEqual(resultado, "L")
    def test_12(self):
        resultado = to_roman(100)
        self.assertEqual(resultado, "C")
    def test_13(self):
        resultado = to_roman(500)
        self.assertEqual(resultado, "D")
    def test_14(self):
        resultado = to_roman(1000)
        self.assertEqual(resultado, "M")
    def test_15(self):
        resultado = to_roman(1101)
        self.assertEqual(resultado, "MCI")
    def test_16(self):
        resultado = to_roman(75)
        self.assertEqual(resultado, "LXXV")
    

class TestRomantodecimal(unittest.TestCase):
    def test_1(self):
        resultado =to_decimal('I')
        self.assertEqual(resultado, 1)
    def test_2(self):
        resultado = to_decimal('II')
        self.assertEqual(resultado, 2)
    def test_3(self):
        resultado = to_decimal('III')
        self.assertEqual(resultado, 3)
    def test_4(self):
        resultado = to_decimal('IV')
        self.assertEqual(resultado, 4)
    def test_5(self):
        resultado = to_decimal('V')
        self.assertEqual(resultado, 5)
    def test_6(self):
        resultado = to_decimal('VI')
        self.assertEqual(resultado, 6)
    def test_7(self):
        resultado = to_decimal('VII')
        self.assertEqual(resultado, 7)
    def test_8(self):
        resultado = to_decimal('VIII')
        self.assertEqual(resultado, 8)
    def test_9(self):
        resultado = to_decimal('IX')
        self.assertEqual(resultado, 9)
    def test_10(self):
        resultado = to_decimal('X')
        self.assertEqual(resultado, 10)
    def test_11(self):
        resultado = to_decimal('L')
        self.assertEqual(resultado, 50)
    def test_12(self):
        resultado = to_decimal('C')
        self.assertEqual(resultado, 100)
    def test_13(self):
        resultado = to_decimal('D')
        self.assertEqual(resultado, 500)
    def test_14(self):
        resultado = to_decimal('M')
        self.assertEqual(resultado, 1000)
    def test_15(self):
        resultado = to_decimal('MCI')
        self.assertEqual(resultado, 1101)
    def test_16(self):
        resultado = to_decimal('LXXV')
        self.assertEqual(resultado, 75)

        
    if __name__ == '__main__':
     unittest.main()