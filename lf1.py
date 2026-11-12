average=lambda x,y,z:(x+y+z)/3
x=int(input("Enter x:"))
y=int(input("Enter y:"))
z=int(input("Enter z:"))
print(average(x,y,z))

check=lambda x:"Even"if x%2==0 else "Odd"
print(check(10))
print(check(7))

