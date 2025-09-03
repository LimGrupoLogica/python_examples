

def romanToInt(s: str):
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    for character in range(len(s)):
        if character < len(s) - 1 and symbols[s[character]] < symbols[s[character + 1]]:
            result -= symbols[s[character]]
        else:
            result += symbols[s[character]]

    return result

print(romanToInt('MCMXCIV'))
