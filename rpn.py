#!/usr/bin/env python3
from colorama import init
from termcolor import colored
import operator
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow,
}

def calculate(arg):
    stack = []
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
    
    if len(stack) != 1:
        raise TypeError('malformed input')
        
    return stack.pop()
      


def main():
    while True:
        inputline = input("rpn calc> ")
        if inputline == "quit()":
            break;
        result = calculate(inputline)
        
        if result < 0:
            print(colored('-', 'red') + str(abs(result)))
        else:
            print(result)


if __name__ == '__main__':  # Note: that's "underscore underscore n a m e ..."
    main()
