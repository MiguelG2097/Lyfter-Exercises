class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius
        

my_circle = Circle(100)
area = my_circle.get_area()
print(f"The radius of the circle is {area}")
