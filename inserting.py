'''Inserting nums'''

nums=[1,2,3,4,5]
nums[2:2]=[99,100]
print(nums)

'''Removing'''
nums=[10,20,30,40,50,60,70]
nums[1:4]=[]
print(nums)

colors=["red","green","blue"]
colors[:]=["cyan","magenta","yellow","black"]
print(colors)

matrix=[[1,2,3],[4,5,6]]
matrix[1][1:3]=[19,23]
print(matrix)