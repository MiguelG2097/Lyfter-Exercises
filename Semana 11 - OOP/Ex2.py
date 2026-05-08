class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
        

    def add_passenger(self, person):
        if  len(self.passengers) >= self.max_passengers:
            print("The bus is full")
        else:
            self.passengers.append(person)
            print("Passenger added to the bus")

    def remove_passenger(self, person):
        self.passengers.remove(person)
        print("Passenger removed from the bus")
    
class Person:
    def __init__(self, name):
        self.name = name 

person_1 = Person("Jose")
person_2 = Person("Maria")
person_3 = Person("Pablo")
red_bus = Bus(2)
red_bus.add_passenger(person_1)
red_bus.add_passenger(person_2)
red_bus.add_passenger(person_3)
red_bus.remove_passenger(person_1)
red_bus.add_passenger(person_3)



        

