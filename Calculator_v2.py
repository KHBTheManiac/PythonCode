version = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계:"))
if version == 1 :
    math = input("*** 수식을 입력하세요:")
    result = eval(math)
    print(math,"결과는",result,"입니다.")

elif version == 2:
    n1 = int(input("*** 첫 번째 숫자를 입력하세요:"))
    n2 = int(input("*** 두 번째 숫자를 입력하세요:"))
    sol = (n1+n2)*(n2-n1+1)/2
    print(n1,"+ ... +",n2,"는",sol,"입니다.")

else:
    print("올바른 숫자를 입력해주세요.")