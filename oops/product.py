class Product:
    def __init__(self,productId,name,dop,cost):
        self.__productId=productId
        self.__name=name
        self.__dop=dop
        self.__cost=cost

    def setProductId(self,productId):
        self.__productId=productId

    def getProductId(self):
        return self.__productId

    def setName(self, name):
        self.__name= name

    def getName(self):
        return self.__name

    def setDop(self, dop):
        self.__dop = dop

    def getDop(self):
        return self.__dop

    def setCost(self, cost):
        self.__cost = cost

    def getCost(self):
        return self.__cost
'''
import datetime
product=Product(3248723,'Laptop',datetime.date(2021,5,21),34568)

print(product.getProductId(),product.getName(),product.getDop(),product.getCost())

#update

product.setName("MobilePhone")


print(product.getProductId(),product.getName(),product.getDop(),product.getCost())

'''