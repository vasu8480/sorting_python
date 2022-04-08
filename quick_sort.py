def pivot_place(list,first,last):
  pivot=list[first]
  left=first+1
  right=last
  while True:
    while left<=right and list[left] <=pivot:
      left=left+1
    while left<=right and list[right] >=pivot:
      right=right-1
    if right<left:
      break
    else:
      list[left],list[right]=list[right],list[left]
  list[first],list[right]=list[right],list[first]
  return right

def quicksort(list,first,last):
  if first<last:
    p=pivot_place(list,first,last)
    quicksort(list,first,p-1)
    quicksort(list,p+1,last)

list=[26,85,96,45,68,8545]
n=len(list)
quicksort(list,0,n-1)
print(list)
