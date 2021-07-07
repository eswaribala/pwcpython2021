#create customer list
import datetime
customer=[2462,'Parameswari','Bala',datetime.date(1970,12,2),True]
print(customer[2:])



#read the list
for _ in customer:
   if type(_) == str:
       print (_)

#dynamic list
customers=[]
import random
def getKey(data):
    # return element position to sort
    return data[1]

for _ in range(50):
    customer=[random.randint(1,5000),'customer'+str(_)]
    customers.append(customer)

#print(customers)
customers.sort(reverse=False,key=getKey)
for _ in customers:
    print(_)
    '''
    for __ in _:
        if(type(__)==str):
            print(__)
    '''

projectList=['p1','p2','p3','p4']
companyList=['c1','c2','c3','c4']

for (x,y) in zip(projectList,companyList):
    print(x,'=>',y)


