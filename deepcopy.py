import copy
list1=[[3,5],[7,9]]
list2=copy.deepcopy(list1)
list2[1][0]=77
print(list1)
print(list2)