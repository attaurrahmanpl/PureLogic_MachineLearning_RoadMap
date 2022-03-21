

#                                                # List comprehensions Lecture_11
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("List comprehensions Lecture_11")
print("Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).\n")

items = [
    ("item1" , 20) ,
    ("item2" , 225) ,
    ("item3" , 234) ,
    ("item4" , 22) ,
]
print("map function is:")
prices = list(map(lambda item : item[1] , items))
print(prices)
print("\n filter function is: ")
filtered = list(filter(lambda item: item[1]>=100 , items))
print(filtered)

print("The above two task we can also perform using list comprehensions")
price = [item for item in items if item[1] > 100]
print(price)



#                                                # Zip function Lecture_12
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Zip function Lecture_12")

list1 = [1 , 2 , 3 , 4]
list2 = [2 , 4 , 6 , 8]
print(list(zip("zipizipi" , list1, list2)))



#                                                # Stack Lecture_12
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Stack Lecture_12")

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.append(4)
browsing_session.append(5)
print("This the simple list\n" , browsing_session)
print("the below function will remove the laste element from the list")
last = browsing_session.pop()
print("we can seee here the lase element is now is:" , browsing_session[-1])
print(browsing_session)
print("so the stack use lifo to remove the last value first")


#                                                # Queue Lecture_13
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Queue Lecture_13")
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print("in queue we also remove firs element")
first_item = queue.popleft()
print(queue)
print("removed item is" , first_item)

if not queue:
    print("empty")


#                                                # Tuple Lecture_14
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Tuple Lecture_14")
print("A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a\nlist in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.")

points = (1 , 2 , 3 , 5 , 6 , 7)
print("this is the simples tuple\n" , points)

print("\nto concatenate tuple")
points = points + (90 , 87 , 87 , 6)
print("concatenated tiple is : " , points)
print("to print single item from tuple : " , points[6])
print("To print range of tuple" , points[:4])
print("to unpack tuple")
x , y ,z = points[0:3]
print(x,y,z)


#                                                # Swap variable Lecture_15
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Swap variable Lecture_16")

x = 30
y = 40
print("x = :" , x , "\ny = :" , y)
print("after swaping values")
tem = x
x = y
y = tem
print("x = :" , x , "\ny = :" , y)
print("we can also swap value without extra variable")
x , y = y , x
print("x = :" , x , "\ny = :" , y)


#                                                # Arrays Lecture_16
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Arrays Lecture_16")

from array import array
# the below "i" is type code because array have only contain single data type at time
numbers = array('i' , [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8])
print('"i" is type code for integer')
print(numbers)
print("append value in array")
numbers.append(20)
print("array after appending numbers")
print(numbers)
print("after apply inser function")
numbers.insert(0,23)
print(numbers)
print("after applying pop")
numbers.pop()
print(numbers)
print("after applying remove function")
numbers.remove(8)
print(numbers)
print(" acces item using index")
print(numbers[0])
print("updating array")
numbers[4] = 45
print(numbers)


#                                                # Sets Lecture_17
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n")
print("Sets Lecture_17")
print("Sets Lecture_17")

