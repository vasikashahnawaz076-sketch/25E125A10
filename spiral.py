A = [[1, 2, 3, 4, 5],[6, 7, 8 ,9 ,10],[11, 12, 13, 14 ,15]]

top = 0
bottom = len(A) - 1
left = 0
right = len(A[0]) - 1

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        #result.append(matrix[top][i])
        print(matrix[top][i], end=" ")
        #print()
        #top +=1
        #break
#2.Traverse from top to bottom along the right column
    for i in range(top, bottom + 1):
        #result.append(matrix[i]][right])
        print(matrix[i][right], end=" ")
        #right -=1
        #print()
        #break
#3.Traverse from right to left along the bottom row(if still valid)
    if top <= bottom:
        for i in range(right, left - 1, -1):
            #result.append(matrix[i]][bottom])
            print(A[bottom][i], end=" ")
            #bottom -=1
            #print()
            #break
#4.Traverse from bottom to top along the left column(if still valid)
    if left <= right:
        for i in range(bottom, top , -1):
            #result.append(matrix[i]][bottom])
            print(matrix[i][left],end=" ")
            #print()
            #left +=1
            #break
            top +=1
            right -=1
            bottom -=1






    
