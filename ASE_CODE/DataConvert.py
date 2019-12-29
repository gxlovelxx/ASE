import os, sys

# global definition

# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]

base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


# bin2dec

# 二进制 to 十进制: int(str,n=10)

def bin2dec(string_num):
    return str(int(string_num, 2))


# hex2dec

# 十六进制 to 十进制

def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


# dec2bin

# 十进制 to 二进制: bin()

def dec2bin(string_num):
    num = int(string_num)

    mid = []

    while True:

        if num == 0: break

        num, rem = divmod(num, 2)

        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


# dec2hex

# 十进制 to 八进制: oct()

# 十进制 to 十六进制: hex()

def dec2hex(string_num):
    num = int(string_num)

    mid = []

    while True:

        if num == 0: break

        num, rem = divmod(num, 16)

        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


# hex2tobin

# 十六进制 to 二进制: bin(int(str,16))
#并自动填补位32位
def hex2bin(string_num,bit_num):
    return dec2bin(hex2dec(string_num.upper())).zfill(bit_num)


# bin2hex
# 二进制 to 十六进制: hex(int(str,2))
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))

ss = "4"
print(ss)
print(bin(int(ss,16)))
bb = bin(int(ss,16))
b32 = bb[2:].zfill(32)
print(b32)
print(bin2hex(b32))
print(hex2bin(ss,32))
print(bin2dec(b32))
print(dec2hex(bin2dec(b32)))
