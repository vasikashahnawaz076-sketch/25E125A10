student={"Rahul":85,"Amit":90,"Misha":78,"Bobby":83}
names=[name for name in student.keys()]
marks=[mark for mark in student.values()]
result=[(name,mark) for name,mark in student.items()]
print(marks)
print(result)