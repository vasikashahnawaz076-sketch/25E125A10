'''avg marks,min,max,number of students above average'''

N=10
sum=0
marks=[77,67,83,91,79,67,87,95,83,77]
for i in range(10):
    sum=sum+marks[i]

avg=sum/N
count=0
for i in range(10):
    if(marks[i]>avg):
        count+=1

print("Max:", max(marks))
print("Min:", min(marks))
print("Number of students  with greater marks than average:",count)
