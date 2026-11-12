'''mat1=[[10,20,30],
    [40,50,60],
    [70,80,90]]'''
'''sum=0
for row in mat1:
    for j in row:
        sum+=j
print(sum)
'''
'''find sum of each row'''
'''sum=0
    for j in row:
        sum+=j'''

'''for row in mat1:
    print(sum(row))'''

'''for i,row in enumerate(mat1):
    print("Row",i,"Sum",sum(row))'''

A=[[10,20,30],
    [40,50,60],
    [70,80,90]]
rows=len(A)
colums=len(A[0])
for j in range(colums):
    colums_sum=0
for i in range(rows):
    colums_sum+=A[i][j]
    print(colums_sum)

