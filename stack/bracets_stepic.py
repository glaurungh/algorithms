# put your python code here

_stack=[]

def push(x):
    _stack.append(x)


def pop():
    return _stack.pop()


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


def check_bracets_sequence(s):
    clear()
    i=0
    n=0
    while i<len(s):
        if s[i] in ")}]" and is_empty():
            print(i+1)
            break
        if s[i] in "({[":
            push(s[i])
            n=i+1
        elif s[i] in ")}]":
            op = pop()
            if op=="(" and s[i]!=")":
                print(i+1)
                break
            if op=="[" and s[i]!="]":
                print(i+1)
                break
            if op=="{" and s[i]!="}":
                print(i+1)
                break
            n-=1
        i+=1
    else:
        if is_empty():
            print("Success")
        else:
            print(n)

s=input()
check_bracets_sequence(s)
