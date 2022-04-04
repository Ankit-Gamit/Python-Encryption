from random import randint
from prettytable import PrettyTable


def caeser_cipher():

    plain_text = str(input("Enter the plain text:"))
    key = int(input("Enter the key:"))
    cipher_text = ""
    decrypted_text = ""

    print("Original text is:", plain_text)
    for letter in plain_text:
        a = (ord(letter)+key % 26)
        cipher_text += chr(a)

    print("Cipher text:", cipher_text)

    for letter in cipher_text:
        a = (ord(letter)-key % 26)
        decrypted_text += chr(a)

    print("Recovered text:", decrypted_text)


def monoalphabetic_cipher():
    plain_text = str(input("Enter the plain text:"))
    plain_text = plain_text.replace(" ", "")
    cipher_text = ""
    list1 = [chr(i) for i in range(ord('a'), ord('z')+1)]
    print(list1)
    list2 = []
    while len(list2) != len(list1):
        index = randint(0, len(list1)-1)
        if list1[index] not in list2:
            list2.append(list1[index])
    print(list2)
    for i in plain_text:
        if i in list1:
            index = list1.index(i)
            cipher_text += list2[index]
    print(cipher_text)


def rail_fence_cipher():
    plain_text, a = str(input("Enter the plain text: ")), ""
    depth = int(input("Enter the depth: "))
    cipher_text = []
    plain_text = plain_text.replace(" ", "")
    print("Plain text: "+plain_text)

    for i in range(0, len(plain_text), depth):
        if i == len(plain_text)-depth:
            cipher_text.append(plain_text[i])
            break
        else:
            cipher_text.append(plain_text[i:i+depth])

    if len(cipher_text[-1]) != depth:
        cipher_text[-1] += "x"*(depth-len(cipher_text[-1]))

    new_str = []

    for j in range(depth):
        str1 = ""
        str1 += " "*j
        for i in range(len(cipher_text)):
            str1 += " " + cipher_text[i][j]
        new_str.append(str1)

    for i in new_str:
        print(i)

    for j in range(depth):

        for i in range(len(cipher_text)):
            a += (cipher_text[i][j])

    print("Cipher text:"+a)


def columnar_cipher():
    plain_text = str(input("Enter the plain text: "))
    key = []
    key_size = int(input("Enter the size of key: "))
    print("KEYS MUST BE EITHER NUMBERS OR ALPHABETS, NOT A COMBINATION OF THEM.")
    for i in range(key_size):
        key.append(input("Enter key "+str(i+1)+": "))
    cipher_text, ct = [], []
    plain_text = plain_text.replace(" ", "")
    enc_text = ""
    table = PrettyTable(key)

    print("Plain text: "+plain_text)

    for i in range(0, len(plain_text), len(key)):
        if i >= len(plain_text)-len(key):
            cipher_text.append(plain_text[i:])
            break
        else:
            cipher_text.append(plain_text[i:i+len(key)])

    if len(cipher_text[-1]) != len(key):
        cipher_text[-1] += "x"*(len(key)-len(cipher_text[-1]))

    for i in cipher_text:
        new_list = list()
        for a in i:
            new_list.append(a)
        table.add_row(new_list)
    print(table)

    for j in range(len(key)):
        a = ""
        for i in range(len(cipher_text)):
            a += (cipher_text[i][j])
        ct.append(a)

    if type(key[0]) == int:
        for i in key:
            enc_text += ct[i-1]
    else:
        for i in sorted(key):
            a = key.index(i)
            enc_text += ct[a]

    print("Cipher text: "+str(enc_text))


def playfair_cipher():
    plain_text = str(input("Enter plain text:"))
    key = str(input("Enter key:"))
    plain_text = plain_text.replace(" ", "").lower()
    group = list()

    matrix = list()
    new_matrix = list()
    list1 = list()

    # insert key in the matrix
    for a in key.lower():
        if a in matrix:
            pass
        else:
            matrix.append(a)

    # insert rest of the alphabets in the matrix
    for a in range(ord('a'), ord('z')+1):
        if chr(a) in matrix or chr(a) == "j":
            pass
        else:
            matrix.append(chr(a))

    # creating 5x5 matrix
    for i in range(0, len(matrix), 5):
        new_matrix.append(matrix[i:i+5])

    print("5x5 Matrix:")
    for i in range(5):
        print(new_matrix[i])
    print()

    def change_pt(i, plain_text):
        plain_text = plain_text[:i]+"x"+plain_text[i:]
        return plain_text

    for i in range(0, len(plain_text)-1, 2):
        if i == len(plain_text):
            pass
        else:
            if plain_text[i] == plain_text[i+1]:
                plain_text = change_pt(i+1, plain_text)
        group.append(plain_text[i]+plain_text[i+1])

    print("Divide plain text in groups of 2:")
    print(group)
    print()

    print("Cipher text:")
    for word in group:
        for i in range(5):
            for j in range(5):
                if word[0] in new_matrix[i][j]:
                    index_of_l1 = [i, j]
                if word[1] in new_matrix[i][j]:
                    index_of_l2 = [i, j]
    # for same row
        if index_of_l1[0] == index_of_l2[0]:

            if index_of_l1[1] == 4:
                print(new_matrix[index_of_l1[0]][0] +
                      new_matrix[index_of_l2[0]][index_of_l2[1]+1])

            elif index_of_l2[1] == 4:
                print(new_matrix[index_of_l1[0]]
                      [index_of_l1[1]+1] + new_matrix[index_of_l2[0]][0])

            else:
                print(new_matrix[index_of_l1[0]][index_of_l1[1]+1] +
                      new_matrix[index_of_l2[0]][index_of_l2[1]+1])

    # for same column

        elif index_of_l1[1] == index_of_l2[1]:
            if index_of_l1[0] == 4:
                print(new_matrix[0][index_of_l1[1]] +
                      new_matrix[index_of_l2[0]+1][index_of_l2[1]])

            elif index_of_l2[0] == 4:
                print(new_matrix[index_of_l1[0]+1]
                      [index_of_l1[1]] + new_matrix[0][index_of_l2[1]])
            else:
                print(new_matrix[index_of_l1[0]+1][index_of_l1[1]] +
                      new_matrix[index_of_l2[0]+1][index_of_l2[1]])

    # different row and column
        else:
            print(new_matrix[index_of_l1[0]][index_of_l2[1]] +
                  new_matrix[index_of_l2[0]][index_of_l1[1]])
