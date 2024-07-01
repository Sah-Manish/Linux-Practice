#! /usr/bin/python
import re
import sys

email=sys.argv[1]
if (re.search(r"^\w+@\w+\.(com|gov|in|net|edu)$", email, re.IGNORECASE)):
    # or i could use r"\w+@\w+\.(com|gov|in|net|edu)$", email.lower()
    print("Valid")
else:
    print("Invalid")

