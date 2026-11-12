'''def describe_users(name,**extras):
    return{"name":name,**extras}
dict1={}
dict1=describe_users("Amara",role="Doctor",gender="Male",age=25,active="True")
print(dict1)'''

def use_both(*args,**kwargs):
    for i in args:
        print(i)
    for j in kwargs:
        print(j,":",kwargs[j])
use_both(1,2,3,4,a=10,b=20,c=30)

'''write a program that can accept any number of sales amount as positional arguments (*args) and additional information such as salesperson name,location,date,gender etc as keyword arguments(**kwargs)'''

def sales_report(*args,**kwargs):
    for i in args:
        sum_sales=sum(args)
        print("Sales Amount:",i)
    for j in kwargs:
        print(j,":",kwargs[j])
    print("Total Sales:", sum_sales)
sales_report(1000,2000,3000,4000,name="Vasika",location="Kashmir",date="2024-06-15",gender="Female")