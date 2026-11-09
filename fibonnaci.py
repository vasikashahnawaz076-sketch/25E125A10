'''write a program to find nth fibonnaci number.Print fibo numbers less than n'''

n=(int)(input ("Enter n:"))
a=0
b=1
c=0
while (True):
    print(a,end=" ")
    a,b=a+b,a
    c+=1
    if(c==n):
        break
   
   