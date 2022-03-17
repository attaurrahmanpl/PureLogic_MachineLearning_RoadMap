#                                                # Builtin data structure
#                                                # Lis data structure
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Lis data structure")
# list of latter
latter = ["a" , "b" , "c" , "d"]
print(latter)


# list between a list
print("\n")
matrix = [ [2 , 3] , [ 4 , 5 ] , [6 , 7]]
print(matrix)


# to print multiple time single element of the lis
print("\n")
stars = ["*"] * 10
print(stars)

# concatenate of the two or more list
print("\n")
combined = stars + matrix
print(combined)

# To create list of the number define range
print("\n")
numbers = list(range(23))
print(numbers)
print(numbers[5:])

# use list function to create string list
print("\n")
character = list("Hello World Python")
print(character)
print("length of the character is:" , len(character))


#                                                # Accessing  item in list Lecture_2
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Accessing  item in list Lecture_2")


# access list item using index number
print("\n")
list_latter = ["ab" , "c" , "d" , "g" , "atta"]
print("List item 0 is : " , list_latter[0])
print("List item -1 is : " , list_latter[-1])


# modify item in list
print("\n")
print("original List item no#1 is:" , list_latter[1])
list_latter[1] = "cd"
print("List item no#1 new updated value is:" , list_latter[1])


# using two index to slice string from list
print("\n")
print("liste items of index 1 to 3 is :" , list_latter[0:3])
print("every second latter : " , list_latter[::2]) # this access every second latter in list

# using range method
print("\n")
numbers_range = list(range(20))
print("original list numbers_range the numbers between 0 to 20 is:" , numbers_range)
print("numbers_range every second number is:",numbers_range[::2])
print("list of number in reverse order:",numbers_range[::-1])
print("list of ever second number in reverse order:",numbers_range[::-2])


#                                                # list unpacking Lecture_3
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("list unpacking Lecture_3")

# list
unpacking_numbers = [1 , 3 , 6 , 7 , 10]
first_two = unpacking_numbers[0:2]
second_ = unpacking_numbers[2 :]
single_number = unpacking_numbers[-1]
print("single number is:" , single_number)
print("first numbers is:" , first_two)
print("second numbers is:" , second_)
first , second , *other = unpacking_numbers
print("first number of the list is:" , first)
print("Second number of the list is:" , second)
print("all other number of the list is:" , other)
first , *other , last = unpacking_numbers
print("first number of the list is:" , first)
print("all other number of the list is:" , other)
print("last number of the list is: " , last)
print("First and last number of the list is:" , first , last)


#                                                # looping over list Lecture_4
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("looping over list Lecture_4")

# loop
print("\nsimple for loop")
latter_loop = ["a" , "b" , "c"]
for latter_loop in latter_loop:
    print(latter_loop)

# enumerate method
# the enumerate function will also print the index of the list as wel values
print("\nFor Loop with enumerate method To print index of the list as well vaues in tupple")
latter_loop = ["a" , "b" , "c"]
for latter_loop in enumerate(latter_loop):
    print(latter_loop)

print("\nFor Loop with enumerate method To print index of the list as well vaues in tupple")
latter_loop = ["a" , "b" , "c"]
for latter_loop in enumerate(latter_loop):
    print(latter_loop[0] , latter_loop[1])

print("\nUnpacking tuuple")
latter_loop = ["a" , "b" , "c"]
for index , latter in enumerate(latter_loop):
    print(index , latter)


#                                                # Adding Removing items from list Lecture_5
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Adding Removing items from list Lecture_5")


latter = ["a" , 3 ,"b" , 5 ,"r" , "st"]
# adding item at the end in a list
print("\nadd item at the end in a list")
print("original list is:" , latter)
latter.append("atta")
print("The updated list is:" , latter)
# insert new value on specific index
print("\ninsert new value on specific index")
latter.insert(0 , 23)
print("after adding new values in list:" , latter)
print("\n Removing items from list")
# to remove the last value from the list
print(" .to remove the last value from the list ")
print("original list is:" , latter)
print("pop method")
#latter.pop()
latter.pop(0) # this will remove first value from the list
print("Remove value from list using index value" , latter)
# remove method will only remove specific value it's not using indx
# while pop remove only one value at a time using index
# print("Remove method")
# latter.remove(23)
# print("After removing specific value from list:" , latter)
