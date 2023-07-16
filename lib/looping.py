#!/usr/bin/env python3

def happy_new_year():
    c = 10
    while c >= 0:
        if c == 0:
            return print("Happy New Year!")
        else:
            print(c)
            c -= 1
    pass

def square_integers(int_list):
    squared_ints = [val * val for val in int_list]
    return squared_ints
    pass

def fizzbuzz():
    n = 1
    while n <= 100:
        if n%3 == 0 and n%5 == 0:
            print("FizzBuzz")
            n += 1
        elif n%3 == 0:
            print("Fizz")
            n += 1
        elif n%5 == 0:
            print("Buzz")
            n += 1
        else:
            print(n)
            n += 1
    pass
