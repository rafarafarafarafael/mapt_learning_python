names = ['John', 'Jane', 'James', 'June']
ages = [23, 48, 32, 12]

#zip function packs N sequences in a list of tuples of N items
for name, age, in zip(names, ages): 
    print(name, age)