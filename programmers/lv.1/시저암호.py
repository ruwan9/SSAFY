s = 'a B z'
n = 4

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():  # 대문자일때
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():  # 소문자일때
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s)

print(caesar(s, n))