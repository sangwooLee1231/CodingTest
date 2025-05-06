T = int(input())  # 테스트 케이스의 수를 입력 받음

for _ in range(T):
    string = input()
    stk = []
    IsVps = True
    
    for char in string:
        if char == '(':
            stk.append(char)
        else:
            if len(stk) > 0:
                stk.pop()
            else:
                IsVps = False
                break
    
    if IsVps and len(stk) == 0:
        print("YES")
    else:
        print("NO")