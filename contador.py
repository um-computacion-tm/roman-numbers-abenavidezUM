#Clase

import unittest

def count_words(word):
    return {word: 1}

class TestCountLetters(unittest.TestCase):
 
    def test_simple(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})
        
if __name__ == '__main__':
    unittest.main()