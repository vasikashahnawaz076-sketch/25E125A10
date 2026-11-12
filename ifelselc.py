'''num=[17,18,19,20,21,23,27,32]
for x in num:
    if x%2==0:
        print(x,"is even")
    else:
        print(x,"is odd")
        result=["Even" if x%2==0 else "Odd" for x in num]
print(result)'''

'''write a list comprehension to find out pass and fail'''
marks=[39,47,51,27,77,83,19,93]
result=["Pass" if x>40 else "Fail" for x in marks]
print(result)