'''write in list comprehension to find names start with A'''
'''students=["Rahul","Amit","Priya","Ananya","Rohan","Anuradha"]
a_names=[name for name in students if name.startswith("A")]
print(a_names)'''

'''find the salaries greater than 30000 and increase 10% of them'''
'''salaries=[25000,45000,32000,60000,28000,40000]
result=[salary*1.1 for salary in salaries if salary>30000]
print(result)'''


'''write a program to check for a valid email id it should contain @ and it should end with .com or .org'''
'''data=["user@gmail.com","abc.org","xyz@map.com","Hello@hi.org","you@him","test.abc","soa@iter"]
result=[email for email in data if("@" in email and (email.endswith(".com") or email.endswith(".org")))]
print(result)'''

'''Remove the empty strings from the list'''
words=["Python","","Java","c++","","Djnago","","C",""]
result=[x for x in words if x]
print(result)