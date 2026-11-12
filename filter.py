'''numbers=[1,2,3,4,5,6]
even_numbers = (filter(lambda x: x % 2 == 0, numbers))
print(list(even_numbers))'''

'''write a program a list is given  square every element of the list and find the sum of the squared list'''
'''l=[2,3,5,7,11]
from functools import reduce
squares=map(lambda x:x**2,l)
sum=reduce(lambda x,y:x+y,squares)
print(sum)'''

'''a list is given ,find the odd numbers and sum them'''
'''l=[1,2,3,4,5,6,7]
odd_numbers=filter(lambda x:x%2!=0,l)
sum=reduce(lambda x,y:x+y,odd_numbers)
print(sum)'''

''' a list is given filter the even numbers, find the square of the evens and then sum the squares'''
'''l=[1,2,3,4,5,6,7]
even_numbers=filter(lambda x:x%2==0,l)
squares=map(lambda x:x**2,even_numbers)
sum=reduce(lambda x,y:x+y,squares)
print(sum)'''

'''from functools import reduce
marks=[39,72,33,81,55,27,35,90,17]
sum=reduce(lambda x,y:x+y,map(lambda x:x+5,filter(lambda x:x<40,marks)))
print(sum)'''
'''passing_marks=filter(lambda x:x<40,marks)
grace=map(lambda x:x+5,passing_marks)
sum=reduce(lambda x,y:x+y,grace)
print(sum)'''

from functools import reduce
words=["Python","is","a","powerful","language"]
result=reduce(lambda x,y:x+" "+y,words)
print(result)