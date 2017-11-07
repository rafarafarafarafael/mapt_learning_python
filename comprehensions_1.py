# This is a list comprehension
myList = [x for x in range(12)]
print(myList)

# a more complex example
myList = [x*x + x for x in range(100) if x%2 == 0]
print(myList)

myList = [x*y for x,y in zip(range(50),range(50, 100))]
print(myList)

# nested loops in comprehensions
myList = [x * y for x in range(10) for y in range(1, 3)]
print(myList)

# This is a dictionary comprehension
myNicks = ['abe', 'superman', 'flash']
myNames = ['Abraham', 'Clark', 'Barry']
myDict = {nick:name for nick,name in zip(myNicks, myNames)}
print(myDict)

# and a set comprehension
myString = list('hello')
mySet = {c.upper() for c in myString}
print(mySet)