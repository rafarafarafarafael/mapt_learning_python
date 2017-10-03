# This is a Tuple
myTuple = (0, 1, 2, 3)
print('the type of myTuple is ' + str(type(myTuple)) + ' and the contents are ' + str(myTuple))

# Tuples can contain any type of objects
myTuple = tuple('rafa')
print(myTuple)

myTuple = ('rafa', )
print(myTuple)

# But tuples are immutable
print('the id of the tuple ' + str(myTuple) + ' is ' + str(id(myTuple)))
myTuple = (2, 3, 4, 5)
print('the id of the tuple ' + str(myTuple) + ' is ' + str(id(myTuple)))

# This is a List
myList  = [1, 2, 3, 4]
print('the type of myList is ' + str(type(myList)) + ' and the contents are ' + str(myList))

# Like tuples, lists can contain different object types
myList = list('rafa')
print(myList)

myList = ['rafa']
print(myList)

# Lists are mutable though
print('the id of the list ' + str(myList) + ' is ' + str(id(myList)))
myList.extend([2, 3, 4, 5])
print('the id of the list ' + str(myList) + ' is ' + str(id(myList)))

# Lists can also contain duplicates
myList.append('2')
print(myList)
myList.extend([5, 6 ,7 ,8 ,9])
print(myList)

# Then there are Sets
mySet = {1, 2, 3}
print('the type of mySet is ' + str(type(mySet)) + ' and the contents are ' + str(mySet))

# Sets discard duplicated elements
mySet.add(2)
mySet.add(3)
mySet.add(4)
print(mySet)

# Sets are not ordered, so trying to access an index returns an error
try:
    mySet[0]
except TypeError as t:
    print(t)

# And sets are good for testing membership as they are faster than lists
print(5 in mySet)