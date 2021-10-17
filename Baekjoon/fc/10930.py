import sys
sys.stdin = open('input_files/5397.txt')
import hashlib

S = input()
encoded_S = S.encode()
res = hashlib.sha256(encoded_S).hexdigest()

print(res)
