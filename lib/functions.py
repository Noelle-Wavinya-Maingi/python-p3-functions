#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")


def greet(name):
    pass
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")

def add(num1, num2):
    pass
    return num1 + num2

def halve(number):
    pass
    if(type(number) != int and type(number) != float):
        return None
    else:
        return number/2


greet_programmer()
greet("programmer")
greet_with_default()
add(num1=1, num2=2)
halve(1309)