#!/usr/bin/env python3

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
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
        result = calculate(input("rpn calc> "))
        print(result)


if __name__ == '__main__':  # Note: that's "underscore underscore n a m e ..."
    main()