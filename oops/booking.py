from abc import ABC,abstractmethod

class Booking(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

    def load(self):
        print("Ready with abstarct class")


class FlightBooking(Booking):
    #static variable
    serviceProvider='Indigo'
    def __init__(self):
        self.__amount=0
    def pay(self,amount):
        self.__amount=amount

flightBooking=FlightBooking()
flightBooking.pay(12000)
print(FlightBooking.serviceProvider)