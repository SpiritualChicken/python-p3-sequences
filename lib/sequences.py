#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        my_fibonacci = []
        print(my_fibonacci)
    elif length == 1:
        my_fibonacci = [0]
        print(my_fibonacci) 
    else:
        my_fibonacci = [0, 1]
        while len(my_fibonacci) < length:
            num = my_fibonacci[-1] + my_fibonacci[-2]
            my_fibonacci.append(num)
        print(my_fibonacci)


print_fibonacci(1)