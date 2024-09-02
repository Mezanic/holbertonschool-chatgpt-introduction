#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Check if an argument is provided
if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except ValueError:
        print("Please provide an integer as the argument.")
else:
    print("Please provide an argument.")
