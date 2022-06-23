                    # -----------Functional Programming-------
from functools import reduce
                    #   ---------map,filter------------
def multi(item):
    return item**2
def odd(item):
    return  item%2!=0
li=[1,2,3,4,5,6,7]
print(list(map(multi,li)))
print(list(filter(odd,li)))
                    #   -------- Reduce -----------
def acc(aa,i):
    return i+aa
li=[1,2,3,4,5]
print(reduce(acc,li))

my=[1,2,3,4]
print(list(map(lambda it:it*2,my)),end="\n")

a=[(0,1),(552,-5),(-2,56),(42,8)]
a.sort(key=lambda x:(x[0]+x[1]))
print(a)

my={i for i in 'hello'}
print(my)

li=[1,2,3,2,3,1,3,1,1]
print(set([x for x in li if li.count(x)>2]))
