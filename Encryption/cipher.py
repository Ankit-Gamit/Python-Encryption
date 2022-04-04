import Symmetric_enc
from sys import exit
print("\n"+"*"*20+"ENCRYPTION"+"*"*20)
while True:
    print("\nChoose encryption method:\n1. Caeser cipher\n2. Monoalphabetic cipher\n3. Rail fence cipher\n4. Columnar cipher\n5. Playfair cipher\n0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n"+"*"*20+"Caeser Cipher"+"*"*20+"\n")
        Symmetric_enc.caeser_cipher()
    elif choice == 2:
        print("\n"+"*"*20+"Monoalphabetic Cipher"+"*"*20+"\n")
        Symmetric_enc.monoalphabetic_cipher()

    elif choice == 3:
        print("\n"+"*"*20+"Rail fence Cipher"+"*"*20+"\n")
        Symmetric_enc.rail_fence_cipher()

    elif choice == 4:
        print("\n"+"*"*20+"Columnar Cipher"+"*"*20+"\n")
        Symmetric_enc.columnar_cipher()

    elif choice == 5:
        print("\n"+"*"*20+"Playfair Cipher"+"*"*20+"\n")
        Symmetric_enc.playfair_cipher()
    elif choice == 0:
        exit()
    else:
        print("PLEASE SELECT A VALID OPTION")
