# https://www.acmicpc.net/problem/9012

while True:
    l = []
    a=input()
    if a == '.':
        #입력값이 '.'이면 종료
        break
    for i in a:
        if i == '(':
            #열린괄호는 통과
            l.append(i)
        elif i == ')':
            if l and l[-1] == '(':
                #리스트에 열린 괄호가 있으면 괄호 pop
                l.pop()
            else: 
                #없으면 절대 닫을수 없는 괄호가 생니니 바로 종료
                print("no")
                break
        elif i == '[':
            #열린 대괄호는 통과
            l.append(i)
        elif i == ']':
            if l and l[-1] == '[':
                #리스트에 열린 대괄호가 있으면 대괄호 pop
                l.pop()
            else: 
                #없으면 절대 닫을수 없는 대괄호가 생니니 바로 종료
                print("no")
                break
    else:
         
        if l: 
             #내용물이 있으면 모든 열린 괄호가 pop되지 않은 거니 no
            print("no")
        else: 
            #비어 있으면 yes
            print("yes")