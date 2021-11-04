import random
print("오징어 게임에 참가하셨습니다")
print("이번 게임은 다리 건너기 입니다")
 
 # 오른쪽일까? 왼쪽일까?
print("오른쪽 왼쪽 중에 선택 하세요")
 
 # 1번은 왼쪽 2번은 오른쪽
print("1번은 왼쪽 2번은 오른쪽")

# 총 10칸의 다리가 있다
bridge = 1  # 다리가 한개면
blist = [] #다리의 칸이 10개
# 다리 리스트가 고정이네? 무작위로 다리의 정보를 나타내자
for i in range(10):
    blist.append(random.randint(1,2))

print(blist)
# 숫자로 점프를 왼쪽 오른쪽이 나왔으면 좋겠다
lr_dict = {1:"왼쪽",2:"오른쪽"}
print(lr_dict)
# 왼쪽인지 오른쪽인지 맞추면 살 수 있고
# 틀리면 죽는다
# 최종 10칸까지 다가면 승리
# 중간에 틀리면 탈락 게임 오버
# 다리의 갯수만큼 반복
for i, v in enumerate(blist):
    num = int(input("선택하세요(숫자만): "))
    print("{}번으로 점프".format(lr_dict[num]))    

    # 내 선택에 따라 살고 죽는다


    if v == num:
        print("{}번 다리 통과~".format(i+1))
        if i == len(blist) - 1:
            print("휴~ 살았다")
            print("다음 스테이지로 이동~")
    else:
        print("으아아아아악~")
        print("게임오버")
        break
print("게임이 끝났습니다")
