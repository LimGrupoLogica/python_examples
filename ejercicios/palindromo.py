


def isPalindrome(x: int):
    original =str(x)
    reverse = str(x)
    print(reverse[::-1])
    print(original)

    return original == reverse[::-1]

print(isPalindrome(11))

