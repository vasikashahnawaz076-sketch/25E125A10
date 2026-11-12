'''print the matrix row by row'''

mat=[[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]

'''for row in mat:
    for e in row:
        print(e,end=",")'''

'''row=len(mat)
column=len(mat[0])
for i in range(row):
    for j in range(column):
        print(mat[i][j],end=",")'''

'''print the matrix column by column'''

row=len(mat)
column=len(mat[0])
for j in range(column):
    for i in range(row):
        print(mat[i][j],end=",")

