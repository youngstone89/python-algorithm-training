def evenOrOdd(num):
    
    s = ""
    if num > 0 and num%2==0:
        s = "Even"
    elif num > 0 and num%2==1:
    	s = "Odd"    
    #함수를 완성하세요

    return s

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
