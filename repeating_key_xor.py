from binascii import hexlify


def encode_byte(key, byte):
    string_val = ord(byte)
    key = ord(key)
    value = string_val ^ key
    return hex(value)


def repeating_key_xor(key, string_to_encode):
    char_string = list(string_to_encode)
    key_count = 0
    for i in range(0, len(char_string)):
        if key_count >= len(key):
            key_count = 0
        encoded_byte = encode_byte(key[key_count], char_string[i])[2:]
        if len(encoded_byte) == 1:
            encoded_byte = "0" + encoded_byte
        char_string[i] = encoded_byte
        key_count += 1
    return "".join(char_string)



input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
encrypted = repeating_key_xor("ICE", input)