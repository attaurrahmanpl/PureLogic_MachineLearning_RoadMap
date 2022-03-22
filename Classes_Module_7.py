

#                                                # Creating Custom Classes Lecture_2
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Creating Custom Classes Lecture_1")
class Point:
    def draw(self):
        print("draw")


# Calling the class
point = Point()
print(type(point))
print(isinstance(point , Point))


#                                                # Python Constructor  Lecture_3
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Python Constructor  Lecture_3")

class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age  = 28

c1 = Computer()
print(c1.name)
print(c1.age)
# access the name and age of the function using class objec


#                                                # Class vs Instance Attributes Lecture_4
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Class vs Instance Attributes Lecture_4")

class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def draw(self):
        print (f"Point : [{self.x} , {self.y}] ")
point  = Point (1, 2)
point.draw()