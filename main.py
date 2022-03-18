

#                                                # Adding Removing items from list Lecture_5
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Adding Removing items from list Lecture_5")

latter = ["a" , "b" , "c" , "c" , "d" , "f"]
print("original list is:" , latter)

# To add values at the end in list
print("To add more item in list using append function")
latter.append(23)
print("after applying append function list:" , latter)

# to add value in list using indexing at any index
print("the insert function will add value at index point")
print("original list is:" , latter)
latter.insert(0,3)
print("After inserting values in list:" , latter)


# Remove values from index

print("To remove end value of index or by any index using pop function:")
print("original list is:" , latter)
latter.pop()
print("after applying pop function list is:" , latter)

# To remove specific value by its value
print("original list is:" , latter)
latter.remove(3)
print("after applying remove function on a list:" , latter)

# to remove element from list by range
print("original list is:" , latter)
del latter[0:2]
print("after applying del function by range list is:" , latter)

# to remove all value from list
# print("original list is:" , latter)
# latter.clear()
# print("after applying clear function list is : " , latter)


#                                                # Finding items in a list Lecture_6
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Finding items in a list Lecture_6")
latter = [3, 'a', 'b', 'c', 'c', 'd', 'f', 23]
print("original list is:" , latter)
# to find the index of f in list
print("to find the index of f in list")
print("The index of f is:" , latter.index("f"))

# now if the value does not exist in the list and we search the program will give error
#print(latter.index("g"))
# print("to remove the above error we we use condition")
# input_latter = input("enter the latter that you want in list")
# if input_latter in latter:
#     print(latter.index(input_latter))
# else:
#     print(input_latter , "does not exist in list")


#                                                # sorting items in a list Lecture_7
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("sorting items in a list Lecture_7")

numbers = [12 , 34 , 54 , 65 , 78 , 36 , 5 , 43 , 13]
print("Original list of the numbers :" , numbers)
numbers.sort()
print("sorted list of the numbers is:" , numbers)

# sort a list in reverse order
print("sort list in reverse order")
numbers.sort(reverse=True)
print("list in reverse order is:" , numbers)

# now use sorted function
print("Original list of the numbers :" , numbers)

# sorted function will only create temporary list that will not effect original list
print("after applying sorted function" , sorted(numbers))
print("after applying sorted revrse function :" , sorted(numbers , reverse = True))
print("Original list of the numbers :" , numbers)


# list tuple
print("list of tuple")
items = [
    ("product1" , 10) ,
    ("product2" , 20) ,
    ("product3" , 30) ,
    ("product4" , 14)
]
# items.sort()
# print(items)
def sort_item(item):
    return item[1]


items.sort(key = sort_item)
print(items)

# def sort_item(items):
#     return items[1]
#
#
#
# items.sort(key = sort_item(items))
# print(items)


#                                                # Lambda functions Lecture_8
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Lambda functions Lecture_8")


# list tuple
print("list of tuple")
items= [
    ("product1" , 10) ,
    ("product2" , 20) ,
    ("product3" , 30) ,
    ("product4" , 14)
]
# items.sort()
# print(items)
def sort_item(item):
    return item[1]


items.sort(key = sort_item)
print("sort list using user define function :")
print(items)

# the above task we can also perform using lambda function in easy way
print("list of tuple")
items_lambda= [
    ("product1" , 10) ,
    ("product2" , 20) ,
    ("product3" , 30) ,
    ("product4" , 14)
]
print("lambda function")
items_lambda.sort(key = lambda item : item[1])
print("sort list using lambda function :")
print(items_lambda)


#                                                # Map functions Lecture_9
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Map functions Lecture_9")


