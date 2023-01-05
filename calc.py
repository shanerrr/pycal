import sys
import math


class Calculator:

    def compute(self, input):
        # if there is an opening bracket, we know its an expression
        while '(' in input:
            # getting the starting and ending bracket of deepest nested expression
            rb = input.find(')')
            lb = input[:rb].rfind('(')

            # call our evaluate method with the most nested expression
            solution = self._evaluate(
                input[lb + 1:rb])

            # when the left bracket idx is 0, we know we are at the root expression
            if lb == 0:
                return solution

            # otherwise, update the calculated expression in string with the calculated value
            else:
                input = input[:lb] + str(solution) + input[rb+1:]

        # if not brackets, we can assume its just an interger
        return int(input)

    def _evaluate(self, expression):

        # split the expression to three args
        # ex: (add 2+3) -> [add, 2, 3]
        args = expression.split()

        match args[0]:
            case 'add':
                answer = self._add(args[1:])
            case 'multiply':
                answer = self._multiply(args[1:])

        return answer

    def _add(self, values):
        # turn to a list of ints and add them all up
        return sum(list(map(int, values)))

    def _multiply(self, values):
        # turn to a list of ints and multiplys them all up using math module
        return math.prod(list(map(int, values)))


def main():
    print(Calculator().compute(sys.argv[1]))


if __name__ == '__main__':
    main()
