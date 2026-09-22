#Importing the abstractmethod module
from abc import ABC, abstractmethod


#This is the Abstract Class Payment
class Payment(ABC):

    def __init__(self,amount):
        self.amount =amount

   
    #This is the abstract method
    @abstractmethod
    def calculate_amount(self):
        pass

#Tuition Payment subclass
class TuitionPayment(Payment):

    def calculate_amount(self):
        return (self.amount) + (self.amount * 5 / 100)


#Accomodation Payment subclass
class AccomodationPayment(Payment):
    def calculate_amount(self):
        return (self.amount)+ (self.amount * 10 / 100)
    
#Library subclass
class LibraryFine(Payment):
     def calculate_amount(self):
         return (self.amount) + (self.amount  * 2 / 100)


#Creating the class objects
tuition =TuitionPayment(25000)

accomodation =AccomodationPayment(3000)
library_fee =LibraryFine(3000)

payments =[tuition,accomodation,library_fee]

#Demostrating polymorphism
for payment in payments:
    total_amount =payment.calculate_amount()

#Displaying the results
print("Payment Type :",payment.__class__.__name__)
print("Original Amount UGX :",payment.amount)
print("Total amount UGX :",total_amount)


#The __class__.__name__   Displays the name of the subclass chosen dynamically