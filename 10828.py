# https://www.acmicpc.net/problem/11723
import sys
n = int(sys.stdin.readline())
#명령의수

stack=set
#스택 만들기
for i in range(n):
    command = sys.stdin.readline().split()
    #명령 입력    

    if command[0]=='add':
        if stack.count(command[1])>0:
            pass
        stack.append(command[1])
        #푸쉬한값 스택에 넣기
    elif command[0]=='remove':
        if stack.count(command[1])==0:
            pass
        else:
            print(stack.remove(command[1]))
        #있으면 pop하고 없으면-1
    elif command[0] == 'toggle':
        if stack.count(command[1])>0:
            stack.remove(command[1])
        else:
            stack.append(command[1])
    elif command[0] == 'check':
        if stack.count(command[1])>0:
            print(1)
        else:
            print(0)
    elif command[0] == 'all':
        stack={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    else:
        stack={}