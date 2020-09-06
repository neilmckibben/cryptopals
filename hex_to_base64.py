import base64
import string
lookup = list(string.ascii_uppercase) + list(string.ascii_lowercase) + [str(i) for i in range(0, 10)] + ["+", "/"]
# val = input("Enter your hex value: ")
val = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
#Convert hex to binary
#TODO
b = bin(int(val, 16))
binary = b[2:]
#Process in 1 byte chunks
print(binary)
base_64 = []
i = len(binary)
while i >= 6:
    byte = binary[i - 6: i]
    base_64.append(lookup[int(byte, 2)])
    i -= 6
if len(binary) % 6 != 0:
    remainder = len(binary) % 6
    initial_byte = "0" * (6 - remainder) + binary[:remainder]
    base_64.append(lookup[int(byte, 2)])
base_64 = base_64[::-1]
base_64_str = ''.join(base_64)
print(base_64_str)