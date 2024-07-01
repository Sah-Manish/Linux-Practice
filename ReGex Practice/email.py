#! /usr/bin/python
import re
import sys

email=sys.argv[1]
if (re.search("@", email)):
    print("Valid")
else:
    print("Invalid")

