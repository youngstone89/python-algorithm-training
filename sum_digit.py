def sum_digit(number):
    x = str(number)
    s = 0
    for n in x:
    	s+=int(n)    
    return s
    '''number의 각 자릿수를 더해서 return하세요'''

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));