myList = [1, 2, 3, 4, 5]
myList2 = [6, 7, 8, 9, 10]
print(list(map(lambda *s: 2 * s, myList, myList2)))