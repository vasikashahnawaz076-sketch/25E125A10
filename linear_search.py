roll =[11,13,9,27,23,37,41,55,17,26]
Student=37
found=False
found = True
n=int(input("Enter the roll number of the student:"))

print(n in roll)

for i in range(n):
    if roll[i] ==n:
        print("Student found")
        print("Position:",i)
        found = True
        break

    if found==False:
        print("Student not found")

    