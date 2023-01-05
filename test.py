import unittest

from calc import Calculator


class CalculatorTest(unittest.TestCase):

    calculator = Calculator()

    def testNumber(self):

        # expression given in assignment with answer
        self.assertEqual(self.calculator.compute('123'), 123)
        self.assertEqual(self.calculator.compute('0'), 0)

        # testing with more numbers
        for i in range(0, 100):
            self.assertEqual(self.calculator.compute(str(i)), i)

    def testAdd(self):

        # expression given in assignment with answer
        self.assertEqual(self.calculator.compute('(add 12 12)'), 24)
        self.assertEqual(self.calculator.compute('(add 1 1)'), 2)
        self.assertEqual(self.calculator.compute('(add 0 (add 3 4))'), 7)
        self.assertEqual(self.calculator.compute(
            '(add 3 (add (add 3 3) 3))'), 12)

        # testing with more numbers
        for i in range(0, 50):
            self.assertEqual(self.calculator.compute(
                '(add ' + str(i) + ' ' + str(i+1) + ')'), i + i+1)

    def testMultiply(self):

        # expression given in assignment with answer
        self.assertEqual(self.calculator.compute('(multiply 1 1)'), 1)
        self.assertEqual(self.calculator.compute(
            '(multiply 0 (multiply 3 4))'), 0)
        self.assertEqual(self.calculator.compute(
            '(multiply 2 (multiply 3 4))'), 24)
        self.assertEqual(self.calculator.compute(
            '(multiply 3 (multiply (multiply 3 3) 3))'), 81)

        # testing with more numbers
        for i in range(0, 50):
            self.assertEqual(self.calculator.compute(
                '(multiply ' + str(i) + ' ' + str(i+1) + ')'), i * (i+1))

    def testMixExpressions(self):

        # expression given in assignment with answer
        self.assertEqual(self.calculator.compute('(add 1 (multiply 2 3))'), 7)
        self.assertEqual(self.calculator.compute(
            '(multiply 2 (add (multiply 2 3) 8))'), 28)

        # testing with more numbers
        self.assertEqual(self.calculator.compute('(add 5 (multiply 2 3))'), 11)
        self.assertEqual(self.calculator.compute(
            '(multiply 2 (add (multiply 2 9) 8))'), 52)
        self.assertEqual(self.calculator.compute(
            '(multiply (multiply 5 5) (add 3 5))'), 200)
        self.assertEqual(self.calculator.compute(
            '(multiply (add (multiply 1 3) 5) (add 1 5))'), 48)


if __name__ == '__main__':
    unittest.main()
