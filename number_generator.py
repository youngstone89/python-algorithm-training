def number_generator(x, n):
    return [x*(i+1) for i in range(n)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(4,3))