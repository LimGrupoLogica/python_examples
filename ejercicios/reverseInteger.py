def reverse(x: int):
    print(x.bit_length())
    reversed = int(str(x).replace('-', '')[::-1])
    print(reversed.bit_length())

    if x >= 0:
        if reversed.bit_length() > 31 or reversed.bit_length() < -31:
            return 0
        else:
            return reversed
    else: 
        if reversed.bit_length() > 31 or reversed.bit_length() < -31:
            return 0
        else:
            return int('-' + str(reversed))


def reverse2(x: int):
    print(x.bit_length())
    if x == 0: return 0

   
    #print(reversed.bit_length())

    if x >= 0:
        reversed = int(str(x)[::-1])
        if reversed.bit_length() > 31:
            return 0
        return reversed
    else: 
        reversed = int(str(x).replace('-', '')[::-1])
        if reversed.bit_length() > 31:
            return 0
        return int('-' + str(reversed))

print(reverse2(-2147483412))
