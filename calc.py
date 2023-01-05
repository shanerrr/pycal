import sys

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


class Calculator:

    # very simple implmentation of a stack
    stack = []

    def compute(self, input):
        for index in range(len(input)):
            if input[index] in open_list:
                self.stack.append(index)
            elif input[index] in close_list:
                solution = self._evaluate(input[self.stack.pop()+1:index])
                if not self.stack:
                    return solution

    def _evaluate(self, expression):

        # split the expression to three args
        # ex: (add 2+3) -> add, 2, 3
        args = expression.split()

        match args[0]:
            case 'add':
                answer = self._add(args[1], args[2])
            case 'multiply':
                answer = self._multiply(args[1], args[2])

        return answer

    def _add(self, x, y):
        return int(x)+int(y)

    def _multiply(self, x, y):
        return int(x)*int(y)


def main():
    print(Calculator().compute(sys.argv[1]))


if __name__ == '__main__':
    main()
