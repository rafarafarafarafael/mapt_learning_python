myOddSquares = (x*x for x in range(100) if x % 2) # this creates a generator object
print(myOddSquares)
myList = list(myOddSquares) # exhausts object and generate a list
print(myList)