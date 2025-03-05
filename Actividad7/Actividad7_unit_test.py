#Unit testing
import unittest
import Actividad7_1_numeros

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

class TestRacionales(unittest.TestCase):
    def test_print_hello(self):
        r = 0
        racional = Actividad7_1_numeros.Racionales(r)
        self.assertEqual(racional.print_hello(), "Hello Edgar")

if __name__ == '__main__':
    unittest.main()