# pycal

A calculator that evaluates s-expressions from the command line using Python 3.10.x

#### Examples:

```
$ ./calc.py 123
123

$ ./calc.py "(add 12 12)"
24

$ ./calc.py "(add 1 1)"
2

$ ./calc.py "(add 0 (add 3 4))"
7

$ ./calc.py "(add 3 (add (add 3 3) 3))"
12

$ ./calc.py "(multiply 1 1)"
1

$ ./calc.py "(multiply 0 (multiply 3 4))"
0

$ ./calc.py "(multiply 2 (multiply 3 4))"
24

$ ./calc.py "(multiply 3 (multiply (multiply 3 3) 3))"
81
```
