# https://www.acmicpc.net/problem/1769
import sys
n = int(sys.stdin.readline())
#명령의수

stack=[]
#스택 만들기
for i in range(n):
    command = sys.stdin.readline().split()
    #명령 입력    

    if command[0]=='push':
        stack.append(command[1])
        #푸쉬한값 스택에 넣기
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
        #있으면 pop하고 없으면-1
    elif command[0] == 'size':
        print(len(stack))
        #길이 출력하기
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)

        else:
            print(0)
            #비어있으면1 아니면0
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
        #비어있으면-1 아니면 마지막 수 출력