'''a_list=[1,2,[5,10]]
b_list=a_list.copy()
b_list[0]=0
b_list[1]=0
b_list[2][0]=0
b_list[2][1]=0
print(a_list)
print(b_list)'''

'''a=[[1,2],[3,4],[5,6]]
b=list(a)
b.append([7,8])
print(a)
print(b)'''

import copy
a_list=[1,2,[5,6]]
b_list=copy.deepcopy(a_list)
b_list[2][0]=11
b_list[2][1]=13

print(a_list)
print(b_list)