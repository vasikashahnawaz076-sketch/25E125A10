'''find the numbers which are divisible by 3&7 from 1 to 100'''
numbers=[x for x in range(1,101) if x%3==0 and x%7==0]
print(numbers)