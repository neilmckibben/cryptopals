class XOR:
    def xor(self, buffer_one, buffer_two):
        one = list(bin(int(buffer_one, 16))[2:])
        two = list(bin(int(buffer_two, 16))[2:])
        if len(one) > len(two):
            two = ["0"] * (len(one) - len(two)) + two
        elif len(two) > len(one):
            one = ["0"] * (len(two) - len(one)) + one
        i, j = 0, 0
        while i < len(one) and j < len(two):
            if one[~i] == two[~j]:
                one[~i] = "0"
            else:
                one[~i] = "1"
            i += 1
            j += 1
        encoded = "".join(one)
        value = hex(int(encoded, 2))
        return value

    def xor_key(self, key, buffer):
        one = list(bin(int(key, 16))[2:])
        two = list(bin(int(buffer, 16))[2:])
        remainder =  len(two) // len(one)
        one += (one * (remainder - 1))