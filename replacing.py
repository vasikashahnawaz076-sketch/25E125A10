'''Replacing elements with step'''

letters=['a','b','c','d','e','f','g','h']
letters[::2]=['A','B','E','G']
print(letters)

nums=[0,1,2,3,4,5]
print(nums)
nums[::2]=[10,20,40,]
print(nums)
nums[::2]=[11,22]
print(nums)
nums[::2]=[111,222,333,444,555]
print(nums)