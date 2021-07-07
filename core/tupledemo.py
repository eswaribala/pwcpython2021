import datetime
customer=(2462,'Parameswari','Bala',datetime.date(1970,12,2),True)
print(customer[2:])

#append the data
#cannot append data to tuple
#read the list
for _ in customer:
   if type(_) == str:
       print (_)

import random
#list of tuples
students=[]
for _ in range(50):
    marks=(random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100))
    students.append(marks)

for _ in students:
    print(_)
