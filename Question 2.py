#Importing abstractmethod module from abc
from abc import ABC, abstractmethod


#Creating an abstract Class Transport
class Transport(ABC):
    

   #Abstract method "Calculate_fare" 
    @abstractmethod
    def calculate_fare(self,distance):
        pass
        
#Creating Taxi subclass
class Taxi(Transport):
    def calculate_fare(self,distance):
        return (5000 + 2000 * distance)
#Creating Bus subclass
class Bus(Transport):
    def calculate_fare(self,distance):
        return (1000 * distance)
        
#Creating Motorcycle subclass
class Motorcycle(Transport):
    def calculate_fare(self,distance):
        return (2000 + 1500 * distance)


#Creating the objects for the three transport methods
taxi =Taxi()
motorcycle = Motorcycle()
bus =Bus()

#Distance is 10
distance = 10


#Objects being created
transports =[taxi,bus,motorcycle]

# Demonstrating polymorphism            
for transport in transports:
    fare =transport.calculate_fare(distance)


#Displaying the results of transport type,distance and fare
#The __class__.__name__ Displays the name of the transport classes
print("Transport Type :",transport.__class__.__name__)
print("Distance :",distance,'km')
print("Fare : UGX :",fare)



#EXPLANATION BETWEEN DYNAMIC BINDING AND STATIC BINDING

#Dynamic Binding means that the method that will execute is determined during execution time while Static
# Binding means the method to be executed is passed before program runs earlier during compile time
