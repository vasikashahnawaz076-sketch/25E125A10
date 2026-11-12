'''from functools import reduce

n=[1,2,3,4,5]
def add(x,y):
    return x+y


result=reduce(add,n)
print(result)

'''

l=[10,7,33,25,47,17,53,31]

def max(l):
    max=0
    for x in l:
        if x>max:
            max=x
    return max
print(max(l))

def greater(x,y):
    if x>y:
        return x
    else:
            return y

from functools import reduce
'''max=reduce(greater,l)
print(max)'''

max1=reduce(lambda x,y:x if x>y else y,l)