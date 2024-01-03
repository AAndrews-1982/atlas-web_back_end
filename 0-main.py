#!/usr/bin/env python3

# Assuming 0-add.py contains the defined add function
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
