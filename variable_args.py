def min(*n): # * before the argument name makes it a variable size argument
    mn = n[0] # n behaves as a tuple within the function
    for val in n[1:]:
        if mn > val:
            mn = val
    return mn
    
print(min(1, 3, 4, 2, 6, 10, -1, -2))
