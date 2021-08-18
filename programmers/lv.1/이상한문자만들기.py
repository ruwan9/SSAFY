s = "try hello world"

# 1
def solution(s):
    words = s.split(' ')  # 띄어쓰기는 제외하고 홀/짝 구분하는거기때문에 필수!

    ans_lst = []
    for word in words:
        ans = ''
        for i in range(len(word)):
            if i % 2 == 0:
                ans += word[i].upper()
            else:
                ans += word[i].lower()
        ans_lst.append(ans)

    return ' '.join(ans_lst)  # idx 사이에 띄어스기 추가해주기

# 2
def solution(s):
    answer = ''

    split_word = s.split(' ')
    print(split_word)

    for w in split_word :
        for i in range(len(w)) :
            if i%2 == 0 :
                answer += w[i].upper()
            else :
                answer += w[i].lower()

        answer += ' '
    answer = answer[:-1]

    
    return answer