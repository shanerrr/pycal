import sys

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


class Calculator:

    def compute(self, input):
        left_bound = 0
        for index in range(len(input)):
            if input[index] in open_list:
                left_bound = index
            elif input[index] in close_list:
                solution = self.evaluate(input[left_bound + 1:index])
                if left_bound == 0:
                    return solution

    def evaluate(self, expression):

        # split the expression to three args
        # ex: (add 2+3) -> add, 2, 3
        args = expression.split()

        match args[0]:
            case 'add':
                answer = self.add(args[1], args[2])
            case 'multiply':
                answer = self.multiply(args[1], args[2])

        return answer

    def add(self, x, y):
        return int(x)+int(y)

    def multiply(self, x, y):
        return int(x)*int(y)


def main():
    print(Calculator().compute(sys.argv[1]))


if __name__ == '__main__':
    main()
