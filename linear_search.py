##                                Linear Search for repeated ones also
def search(list1,key):
  list2=[]
  flag=False
  for i in range(len(list1)):
    if key == list1[i]:
      flag =True
      list2.append(i)
  if flag == True:
    for i in list2:
      print('found at',i)
  else:
    print("Not Found")
list1=[5,89,954,6,694,6,894,6,8,13,6,8,458]
key=int(input("k="))
search(list1,key)
##                                Method-2
pos=-1
def search(list,n):
  i=0
  while i<len(list):
    if list[i]==n:
      globals()['pos']=i
      return True
    i=i+1
  return False
list=[5,89,954,6,694,6,894,6,8,13,6,8,458]
n=894
if search(list,n):
  print("found at", pos+1)
else:
  print("not found")
