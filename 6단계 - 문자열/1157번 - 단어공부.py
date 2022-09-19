#1 (정상작동)

word = input().upper()                          # 모두 대문자로 입력

word_list = list(set(word))                     # 집합자료형(set)을 통해 구별된 단어만을 선별

 

many = []

for i in word_list :

    cnt = word.count(i)                         # 입력받은 word에 i가 몇 번 있었는지 세서 cnt에 저장

    many.append(cnt)                            # many 리스트에 그 값을 저장

 

if many.count(max(many)) >= 2 :                 # many에 저장된 값들 중 가장 큰 값의 개수가 many 안에서 2개 이상이면

    print('?')                                  # ? 출력

else :                                          # 1개 라면

    print(word_list[(many.index(max(many)))])   # many에 저장된 값들 중 가장 큰 값의 index를 찾아

                                                # word_list 의 인덱스로 삼으면 가장 많이 나온 알파벳을 찾을 수 있다



#2 (시간초과)
                                                
def cnt(s,letter) :                             # 철자 개수 세기
    count = 0
    for x in s :
        if x == letter :
            count += 1
    return count

s = input().upper()
M_count = cnt(s,s[0])
M_letter = s[0]

for letter in s :
    C = cnt(s, letter)
    if M_letter != letter :
        if C > M_count :                        # 최대 개수 갱신
            M_letter = letter
            M_count = C
        elif C == M_count :                     # 같으면 물음표
            M_letter = '?'
    
print(M_letter)                                    
