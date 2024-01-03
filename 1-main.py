#!/usr/bin/env python3
from typing import Any

# Assuming 1-concat.py contains the defined concat function
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
