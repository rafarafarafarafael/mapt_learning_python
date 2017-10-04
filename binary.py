n = 39
remainders = []

while n > 0:
    remainder = n % 2
    remainders.append(remainder)
    n //= 2

print (''.join(str(x) for x in remainders[::-1]))