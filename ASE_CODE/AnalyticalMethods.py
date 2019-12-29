import struct
import ctypes
from ctypes import *
import binascii
#from ctypes import *
#import bitarray
#大小端转换
def big_small_end_convert(data):
    return binascii.hexlify(binascii.unhexlify(data)[::-1])

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def float2hex(s):
    fp = ctypes.pointer(ctypes.c_float(s))
    cp = ctypes.cast(fp,ctypes.POINTER(ctypes.c_long))
    return hex(cp.contents.value)

def hex_to_float(h):
    i = int(h,16)
    return struct.unpack('<f',struct.pack('<I', i))[0]

def hex2float(h):
    i = int(h,16)
    cp = ctypes.pointer(ctypes.c_int(i))
    fp = ctypes.cast(cp,ctypes.POINTER(ctypes.c_float))
    return fp.contents.value

def hex_to_ubnr(value):
    return int(value, 16)

def convert(s):
    i = int(s, 16)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value         # dereference the pointer, get the float

# def str2bitarray(s):
#     ret = bitarray(''.join([bin(int('1' + hex(c)[2:], 16))[3:] for c in s.encode('utf-8')]))
#     return ret

def bitarray2str(bit):
    return bit.tobytes().decode('utf-8')



if __name__ == '__main__':
    f = [1.5,-1.5,3.5,-3.5]
    h = []
    for i in f:
        print(float_to_hex(i),"   |   ",float2hex(i))
        h.append(float_to_hex(i))
    print(h)
    for i in h :
        print(hex_to_float(i),"   |   ",hex2float(i))

    print(hex_to_float("3FA00000"))
    #c6001f1