from math import sqrt
def nextSqure(n):
    # 함수를 완성하세요
    x='no'
    if int(sqrt(n))==sqrt(n):
        x=(sqrt(n)+1)**2
    return x

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(1036355)));