mat=[[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]
    
row=len(mat)
column=len(mat[0])
for i in range(row):
    if i%2==0:
        for j in range(column):
            print(mat[i][j])
        else:
            for j in range(column-1,-1,-1):
                print(mat[i][j])



        

    
    

