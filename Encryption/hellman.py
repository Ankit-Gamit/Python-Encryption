def check_prime(num):
    count = 0
    for i in range(1, num):
        if (num % i) == 0:
            count += 1
    if count > 2:
        return False
    else:
        return True


def primi_root(p):
    mods = []
    #check = [i for i in range(1, p)]
    for i in range(2, p):
        for j in range(1, p):
            mods.append((i**j) % p)
        for l, v in enumerate(mods):
            if l == v:
                check = True
            else:
                check = False
                break
        if check == True:
            print(mods)
        mods = []


p = int(input("Enter a Prime number: "))
if check_prime(p) != True:
    print(str(p)+" is not a prime number")
alpha = primi_root(p)
print("Alpha: "+str(alpha))
'''
Xa = 4
Xb = 3

x = (alpha**Xa) % p
print("Public key A: " + str(x))
y = (alpha**Xb) % p
print("Public key B: " + str(y))

key_1 = (y**Xa) % p
key_2 = (x**Xb) % p

print("Key 1: "+str(key_1))
print("Key 2: "+str(key_2))
'''
