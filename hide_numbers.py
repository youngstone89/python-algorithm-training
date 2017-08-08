def hide_numbers(s):
    #함수를 완성해 별이를 도와주세요
    unmasked = s[-4:]
    masked = s[0:-4]
    masked = "*"*len(masked)
    return masked+unmasked
	
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));