queue=[]
n=int(input("enter the limit of stack"))
def enqueue():
  ele=input("ele")
  queue.append(ele)


def dequeue():
  if not dequeue:
    print("stack is empty!")
  else:
    e=queue.pop(0)
    print(e)

def display():
  print(queue)
  
while True:
  print("enter the choice 1-push 2-pop 3-display 4-exit")
  choice=int(input())
  if choice==1:
    enqueue()
  elif choice==2:
    dequeue()
  elif choice==3:
    display()
  elif choice==4:
    break
  else:
    print("invalid choice")
