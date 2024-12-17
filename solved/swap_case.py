# https://www.hackerrank.com/challenges/swap-case/problem


# capital letters' ascii decimal are from 65 to 90
# small letters' ascii decimal are from 97 to 122
def swap_case(s):
    result = ""
    
    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            result += chr(ord(char) + 32)
        elif ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)