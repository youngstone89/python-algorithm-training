def rm_small(mylist):
    # 함수를 완성하세요
    if len(mylist) > 0:
        smalleast_num = mylist[0]
        for num in mylist:
            
            if smalleast_num > num:
                smalleast_num = num
                
        
        index_to_pop = mylist.index(smalleast_num)
        mylist.pop(index_to_pop)
        
    
    return mylist


# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [10,8,22]
print("결과 {} ".format(rm_small(my_list)))
