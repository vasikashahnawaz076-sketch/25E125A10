import copy
list1=[[11,13,17],[19,23,29],[31,37,43]]
list2=list1
list3=list1.copy()
list4=copy.deepcopy(list1)
list2[1]=[53,67,73]
print(list1)
list3[2][1]=77
print(list2)
list4[1][2]=83
print(list3)
print(list4)