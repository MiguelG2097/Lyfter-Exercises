
#La herencia múltiple se usa cuando una clase necesita combinar comportamientos de 
# varias clases padre. Es común cuando se quiere agregar “capacidades” reutilizables 
# sin crear una clase gigante.



class Walk:
    def walk(self):
        print("I am walking")


class Fly:
    def fly(self):
        print("I am flying")


class Swim:
    def swim(self):
        print("I am swimming")


class Duck(Walk, Fly, Swim):
    pass

duck = Duck()
duck.walk()
duck.fly()
duck.swim()