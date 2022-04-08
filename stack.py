stack=[]
n=int(input("enter the limit of stack"))
def push():
  if len(stack)==n:
    print("list is full")
  else:
    ele=input('ele')
    stack.append(ele)
    print(stack)

def pop():
  if not stack:
    print("stack is empty!")
  else:
    e=stack.pop()
    print(e)
    print(stack)
while True:
  print("enter the choice 1-push 2-pop 3-exit")
  choice=int(input())
  if choice==1:
    push()
  elif choice==2:
    pop()
  elif choice==3:
    break
  else:
    print("invalid choice")
