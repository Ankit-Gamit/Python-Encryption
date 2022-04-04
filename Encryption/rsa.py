def check_prime(num):
    count = 0
    for i in range(1, num):
        if (num % i) == 0:
            count += 1
    if count >= 2:
        return False
    else:
        return True


p = int(input("Enter value of p:"))
q = int(input("Enter value of q:"))

if check_prime(p) != True:
    print(str(p) + " is not a prime number")
if check_prime(q) != True:
    print(str(q) + " is not a prime number")
M = int(input("Enter message:"))

print("Message:"+str(M))
e_list = list()
n = p*q
print(n)
fi_n = (p-1)*(q-1)
print(fi_n)


def gcd(a, b):
    if a < b:
        a, b = b, a
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


for i in range(2, fi_n):
    gcd_num = gcd(i, fi_n)
    if gcd_num == 1:
        e_list.append(i)

print("e="+str(e_list))
e = e_list[1]

print("Taking e="+str(e))
for i in range(1, 100):
    if (i*e) % fi_n == 1:
        d = i
        break

print("d="+str(d))

public_key = [e, n]
private_key = [d, n]
print("Public key:"+str(public_key))
print("Private key:"+str(private_key))
# Encryption
cipher_text = (M**e) % n
print("Encrypted message:"+str(cipher_text))

# decryption
decrypt = (cipher_text**d) % n
print("Decrypted message:"+str(decrypt))
