import sys
sys.path.append("F:\pwcpythonbatch2\oops\product.py")
from product import Product

class SeasonalProduct(Product):
    def __init__(self,productId,name,dop,cost,season):
        Product.__init__(self,productId,name,dop,cost)
        self.__season=season

    def getSeason(self):
        return self.__season

import datetime
seasonalProduct=SeasonalProduct(294697,'WinterJacket',datetime.date(2020,11,10),3500,'Winter')
print(seasonalProduct.getSeason())
