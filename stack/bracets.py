import stack

def check_bracets_sequence(s):
    stack.clear()
    i=0
    while i<len(s):
       if s[i] in ")}]" and stack.is_empty():
          return False
       if s[i] in "({[":
          stack.push(s[i])
       elif s[i] in ")}]":
          op = stack.pop()
          if op=="(" and s[i]!=")":
              return False
          if op=="[" and s[i]!="]":
              return False
          if op=="{" and s[i]!="}":
              return False
       i+=1
    return True


seq=input('Введите скобочную последовательность:')
print("Последовательность корректна" if check_bracets_sequence(seq) else "Последовательность некорректна")
