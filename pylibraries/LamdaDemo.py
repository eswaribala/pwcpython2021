f = lambda x: x*x
p = f(5)
print(p)

weekdays = ['sun', 'mon', 'tues', 'wed', 'thurs' 'fri']
days = filter(lambda day: day if len(day)==3 else '', weekdays)
for d in days:
   print(d)

numbers = [ 74, 85, 14, 23, 56, 31,44 ]

remainders = map(lambda num: num%5, numbers)
for i in remainders:
   print(i)

colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]

def normalize_case(string):
    return string.casefold()

normalized_colors = map(normalize_case, colors)

for i in normalized_colors:
   print(i)

from functools import reduce

dataList=[89,35,78,90,45,27,78,22]

import math
odd_list = list(map(lambda x: math.log2(x), dataList))
print(odd_list)

orders=[["34587", "Learning Python, Mark Lutz",
         4, 40.95],
        ["34545", "Mastering Python, Mark Lutz",
         3, 90.95]
        ]
min_order=100
invoice_total=list(map(lambda x:x if x[2] >= min_order
                       else (x[2], x[3] + 10),orders))
print(invoice_total)