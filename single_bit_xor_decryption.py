import string
from fixed_xor import XOR


# 32 to 126 are actual mesages ascii values
def xor_key(key, byte):
    int_val = int(byte, 16)
    value = key ^ int_val
    ascii_character = chr(value)
    return ascii_character


# Break into bytes and then apply key
def decrypt(encoded):
    # Generate array of int valued hex bytes:
    hex_bytes = []
    i = len(encoded)
    while i >= 2:
        byte = encoded[i - 2: i]
        hex_bytes.append(byte)
        i -= 2
    if i == 1:
        # Not byte aligned
        hex_bytes.append(encoded[0])
    hex_bytes.reverse()

    ascii_set = set(string.printable)
    canidates = []
    for i in range(1, 257):
        unencrypted = ""
        for byte in hex_bytes:
            unencrypted += xor_key(i, byte)
        #Try to limit the possible values by only printing unecrypted values that make sense
        if all(x in ascii_set for x in unencrypted):
            canidates.append(unencrypted)
    return canidates

#Challenge 4: Now that the party is jumping
def decrypt_multiple(file):
    f = open(file, "r")
    for encoded in f:
        value = encoded.rstrip()
        print("----------------------------")
        canidates = decrypt(value)
        if len(canidates) == 0:
            print("No strong canidates")
        for i in canidates:
            print(i)

# Add 0x
# input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
# decrypt(input)
file = "4.txt"
decrypt_multiple(file)
