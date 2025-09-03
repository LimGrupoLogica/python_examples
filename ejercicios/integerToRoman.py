

def intToRoman(num: int):
    symbols = {
         1000: 'M',
         900: 'CM',
         500: 'D',
         400: 'CD',
         100: 'C',
         90: 'XC',
         50: 'L',
         40: 'XL',
         10: 'X',
         9: 'IX',
         5: 'V',
         4: 'IV',
         1: 'I', 
    }

    result = ''
    acumulado = 0
    numCopy = num
    while acumulado < num:
        for keyValue in symbols.keys():
            if numCopy >= keyValue:
                result += symbols[keyValue]
                acumulado += keyValue
                numCopy -= keyValue
                break
    return result

print(intToRoman(1994))


