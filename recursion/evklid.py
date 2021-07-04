def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else: # a < b
        return gcd(a, b-a)


print(gcd(30, 5))

def gcd_new(a, b):
    if b==0:
        return a
    else:
        return gcd_new(b, a%b)

print(gcd_new(33, 3))

def gcd_final(a, b):
    return a if b==0 else gcd_final(b, a%b)

print(gcd_final(33,3))