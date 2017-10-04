items = [0, None, 0.0, True, 0, 7] # True and 7 evaluate to True
found = False # This is called "flag"
for item in items:
    print('scanning item ', item)
    if item:
        found = True # We update the flag
        break

if found: # We inspect the flag
    print('At least one item evaluates to True')
else:
    print('All item evaluate to False')
