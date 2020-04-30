"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    calculation = input("What would you like to calculate?")
    toke_calculation = calculation.split(' ')
    print(toke_calculation)
    if toke_calculation[0] == "q":
        break
    result = None
    if toke_calculation[0] == "+":

        result = add(int(toke_calculation[1]), int(toke_calculation[2]))
    elif toke_calculation[0] == "-":
        result = subtract(int(toke_calculation[1]), int(toke_calculation[2]))
    elif toke_calculation[0] == "*":
        result = multiply(int(toke_calculation[1]), int(toke_calculation[2]))
    elif toke_calculation[0] == "/":
        result = divide(int(toke_calculation[1]), int(toke_calculation[2]))
    print(result)