##              Selection Sort method-1

def sort(n):
  k=len(n)
  for i in range(k):
    minpos=i
    for j in range(i,k):
      if n[j]<n[minpos]:
        minpos=j
    n[i],n[minpos]=n[minpos],n[i]
n=[5,54,46,4,64,66]
sort(n)
print(n)


##            method-2
list=[5,54,46,4,64,66]
print('original =',list)
for i in range(len(list)):
  min_val=min(list[i:])
  min_ind=list.index(min_val)
  list[i],list[min_ind]=list[min_ind],list[i]
print(list)

##            method-3 (DESC ORDER)
list=[5,54,46,4,64,66]
print('original =',list)
for i in range(len(list)):
  min_val=min(list[i:])
  min_ind=list.index(min_val)
  list[i],list[min_ind]=list[min_ind],list[i]
print(list)
