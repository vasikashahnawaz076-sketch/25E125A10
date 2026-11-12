'''a=[1,2,3,4]
print(id(a))
b=a
b[0]=11
print(id(b))
print(id(a[0]) == id(b[0]))'''

'''a=[1,2,[3,4]]
b=a.copy()
b[0]=11
b[2][1]=44
print(id(a[0])==id(b[0]))
print(id(a[2][1])==id(b[2][1]))'''

import copy
a=[[1,2],[3,4],[5,6]]
b=a
c=a.copy()
d=copy.deepcopy(a)
print(id(a)==id(b))
print(id(a[0])==id(b[0]))
print(id(a)==id(c))
print(id(a[1][0])==id(c[1][0]))
print(id(a)==id(d))
