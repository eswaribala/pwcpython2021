# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:02:13 2021

@author: Balasubramaniam
"""

firstName="Parameswari"
#slice the string
print(firstName[5:-2])
print(firstName.capitalize())
print(firstName.upper())
print(firstName.center(len(firstName)+40,"*"))
print(firstName.ljust(len(firstName)+40,"*"))
print(firstName.rjust(len(firstName)+40,"*"))

#base64 encoding
import base64
import random
seqNo=random.randint(1,1000)
encodedstring=base64.b64encode(str(seqNo).encode(encoding='utf-8',
                       errors='strict'))
print(encodedstring)

#print encoded data using loop
for _ in encodedstring[0:]:
    print(chr(int(_)),end="")





