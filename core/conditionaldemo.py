import random

data=random.randint(1,7000)

if data<1000:
    print ("It is system port address range")
elif (data>1000)and(data<5000):
    print("It is application port range")

else:
    print("It is custom port range")