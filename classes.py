class Point:            #Definimos a new class of things called points
    def __init__(self, x, y):    # __init__ when i create a new point, what information do i need?
                    #(self, x, y) SELF is the variable that going to be a variable that represents the Point itself (the object)
        self.x = x
        self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)
