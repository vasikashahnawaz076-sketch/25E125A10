marks=int(input("Enter marks:"))
grade= lambda x:"O" if x>90 else ("E" if x>80 else "A" if x>70 else "B" if x>60 else "c" if x>50 else "D" )
print(grade(marks))