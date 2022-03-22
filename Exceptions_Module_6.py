

#                                                # Handle Exceptions Lecture_1
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Handle Exceptions Lecture_1")
# age = int(input("age : "))

print("i we are entering string or other type than integer the return error")
print("1st")
try:
    age = int(input("age :"))
except ValueError:
    print("you did not enter valid age")
print("Execution continue")


#                                                # Handling different Exceptions Lecture_2
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Handling different Exceptions Lecture_2")
print("2nd")
try:
    age = int(input("age :"))
    xfactor = 10 / age
    print(xfactor)
except (ValueError):
    print("you did not enter valid age")
except ZeroDivisionError:
    print("age cannot be zero ")
print("Execution continue")

print("multiple exception in single line")
try:
    age = int(input("age :"))
    xfactor = 10 / age
    print(xfactor)
except (ValueError , ZeroDivisionError):
    print("you did not enter valid age")
else:
    print("no exception were thrown")


#                                                # the with statement  Lecture_2
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Handling different Exceptions Lecture_2")


#                                                # Raising exception Lecture_6
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Raising exception Lecture_6")
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less ")
    return 10 / age
try:
    result = calculate_xfactor(8)
    print(result)
except ValueError as error:
    print(error)