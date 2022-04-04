# plain_text = "01110010"
# key = "1010000010"
plain_text = str(input("Enter plain text: "))
key = str(input("Enter the key: "))
p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
p8 = [6, 3, 7, 4, 8, 5, 10, 9]
p4 = [2, 3, 4, 1]
ip = [2, 6, 3, 1, 4, 8, 5, 7]
ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
ep = [4, 1, 2, 3, 2, 3, 4, 1]

s0_box = [['01', '00', '11', '10'], ['11', '10', '01', '00'],
          ['00', '10', '01', '11'], ['11', '01', '11', '10']]
s1_box = [['00', '01', '10', '11'], ['10', '00', '01', '11'],
          ['11', '00', '01', '00'], ['10', '01', '00', '11']]

p10_per, key1, key2, per_pt, exp_right_pt = "", "", "", "", ""
left_s0, right_s1, per_sbox_output, ip_inverse = "", "", "", ""

for i in p10:
    p10_per = p10_per+(key[i-1])

print("P10 = "+p10_per+"\n")

left_half = p10_per[:5]
right_half = p10_per[5:]

print("Left half before shift:"+left_half)
print("Right half before shift:"+right_half+"\n")


def shift(left_half):
    new_str = left_half[1:]
    new_str = new_str+left_half[0]
    return new_str


left_half = shift(left_half)
right_half = shift(right_half)

print("Left half after shift:"+left_half)
print("Right half after shift:"+right_half+"\n")

p8_key = left_half+right_half
print("P8 = "+p8_key+"\n")
for i in p8:
    key1 = key1 + p8_key[i-1]

print("Key 1 = "+key1+"\n")

left_half = shift(left_half)
right_half = shift(right_half)

print("Left half after 2nd shift:"+left_half)
print("Right half after 2nd shift:"+right_half+"\n")

p8_key2 = left_half+right_half
for i in p8:
    key2 = key2 + p8_key2[i-1]

print("Key 2 = "+key2+"\n")

# Encryption
print("Plain text:"+str(plain_text))
for i in ip:
    per_pt = per_pt + plain_text[i-1]

print("Permuted plain text:"+per_pt)

left_pt = per_pt[:4]
right_pt = per_pt[4:]

for i in ep:
    exp_right_pt = exp_right_pt + right_pt[i-1]

print("Expanded right plain text:"+exp_right_pt)

ex_or = bin(int(key1, 2) ^ int(exp_right_pt, 2)).replace("b", "")
print("Ex-or with key 1:"+ex_or)
left_exor = ex_or[:4]
right_exor = ex_or[4:]

a = int((left_exor[0]+left_exor[3]), 2)
b = int((left_exor[1]+left_exor[2]), 2)
left_s0 = s0_box[a][b]

c = int((right_exor[0]+right_exor[3]), 2)
d = int((right_exor[1]+right_exor[2]), 2)
right_s1 = s1_box[c][d]
s_box_output = str(left_s0)+str(right_s1)
print("S box output:"+str(s_box_output))

for i in p4:
    per_sbox_output = per_sbox_output + s_box_output[i-1]

print("Permuted S box value:"+str(per_sbox_output))

# left plain text exor permuted sbox
ex_or2 = bin(int(per_sbox_output, 2) ^ int(left_pt, 2)).replace("0b", "")
print("Ex or with left half:"+str(ex_or2)+"\n")

# swap
print("Swap\n")
left_pt2 = right_pt
right_pt2 = ex_or2
exp_right_pt, per_sbox_output = "", ""
for i in ep:
    exp_right_pt = exp_right_pt + right_pt2[i-1]

print("Expanded right plain text:"+exp_right_pt)

ex_or = bin(int(key2, 2) ^ int(exp_right_pt, 2)).replace("b", "")
print("Ex-or with key 2:"+ex_or)
left_exor = ex_or[:4]
right_exor = ex_or[4:]

a = int((left_exor[0]+left_exor[3]), 2)
b = int((left_exor[1]+left_exor[2]), 2)
left_s0 = s0_box[a][b]

c = int((right_exor[0]+right_exor[3]), 2)
d = int((right_exor[1]+right_exor[2]), 2)
right_s1 = s1_box[c][d]

s_box_output = str(left_s0)+str(right_s1)
print("S box output:"+str(s_box_output))

for i in p4:
    per_sbox_output = per_sbox_output + s_box_output[i-1]

print("Permuted S box value:"+str(per_sbox_output))

# left plain text exor permuted sbox
ex_or2 = bin(int(per_sbox_output, 2) ^ int(left_pt2, 2)).replace("0b", "")
print("Ex or with left half:"+str(ex_or2))

str1 = ex_or2+right_pt2

print("Output:"+str(str1))

for i in ip_inv:
    ip_inverse = ip_inverse+str1[i-1]

print("ip inverse:"+str(ip_inverse))
