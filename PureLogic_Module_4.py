                                                   # Defining Functions Lecture_1
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def greet(): # here we have defining  a functions
    print("Hi everyone")
    print("Most Welcome to everyone")


greet() # call the function



                                            # Pass arguments in function Lecture_2
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Pass arguments in function Lecture_2")
def greet(firs_name , last_name):
    print(f"Hello {firs_name} {last_name}")
    print("Welcome Aboard")


greet("Attaur" , "Rahman")

print("\n")
def greet(firs_name , last_name):
    print(f"Hello {firs_name} {last_name}")
    print("Welcome Aboard")


greet("Attaur" , "Rahman")
greet("Iqrar" , "khan")

                                            # Types of functions Lecture_3
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# two types of function
    # . perform a task only
    # . return value
print("\n")
print("Types of functions Lecture_3")

#  . perform a task function
def greet(name):
    # print("Hi" , name)
    print(f"Hi {name}")


greet("'Attaur Rahman'")

# . return value function

def get_greet(name_2):
# return (f"Hi {name_2}") # after calling this will not print the result we will use print fun to show the result in return function
    return (f"Hi {name_2}")

message = get_greet("'Iqrar khan'")
print(message)

                                            # Keyword arguments Lecture_4
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Keyword arguments Lecture_4")

# simple increment program

def increment(number , by):
    return number + by

result = increment(4 , 7)
print("The incremented number is : " , result)


# second approach of the same program
def get_increment(number_2 , by_2):
    print("the increment number of" , number_2 , "+" , by_2 , " is " , number_2 + by_2)

# keyword arguments
get_increment(number_2 = 6 , by_2 = 9) # we can also call like this any function using keyword arguments
# get_increment(8 , 10)

                                            # Default arguments Lecture_5
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Default arguments Lecture_5")

def get_increment_2(number_3 , number_4 , by = 6): # Here the by perameter has bydefault 6 value if we have not assign value during call this fun
    # key note the default perameter will alway last perameter:
    return number_3 + number_4 + by

result = get_increment_2(4 , 7 )
print("The incremented number is :" , result)

                                            # **arguments multiple number orguments Lecture_6
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("**arguments multiple number orguments Lecture_6")

def save_user(** user):
    print(user)
    print(user.values()) # this will print only the value of the dictionary
    # print(user["name"]) # this will print only the name of the user from dictionary
save_user(id = 1 , name = "Attaurrahma" , address = "Mardan" , mobile_number = int("01234567892"))

                                            # scope of the varibles Lecture_7
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("scope of the varibles Lecture_7")
message_var = 10 # this is global variable
print("Gloabl variable outside from function :" , message_var)
def scope_varible():
    #message_var = "Hello" # this is local variable
    global message_var # we can create global variable inside a function
    # this is bad practice
    message_var = 100 # this is also global variable inside a function
scope_varible()
print("Gloabl variable outside from function :" , message_var)
print("global variable inside of a function :" , message_var)

                                            # debugins Lecture_ 9
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("debugins Lecture_ 9")

                                            # Excercise Lecture_12
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Excercise solution Lecture_12")

def fizz_buz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return ("fiz_buz divisble by 5 and 3")
    if input % 3 == 0:
        return ("divisible by 3")
    elif input % 5 == 0:
        return ("divisible by 5")
    else:
        return(input)
print(fizz_buz(15))