'''create a list containing the squares from 1 to 5'''
'''square=[]
for i in range(1,6):
    square.append(i**2)
print(square)
square_l=[i**2 for i in range(1,6)]
print(square_l)
'''

'''word="Python"
letters=[ch for ch in word]
print(letters)
'''
'''words=["python","java","c++","django"]
length=[len(w) for w in words]
print(length)'''

'''create a list from a_list which contains even numbers'''
'''a_list=[10,7,9,12,16,13,19,8,7,2]
even=[]
for x in a_list:
    if x%2==0:
        even.append(x)
        print(even)
even_numbers=[x for x in a_list if x%2==0]
print(even_numbers)'''


'''create a list that contains negative numbers
numbers=[-5,10,-3,8,-1,7]
negative=[x for x in numbers if x<0]
print(negative)
positive=[x for x in numbers if x>0]
print(positive)'''

'''create a list of squares of even numbers from 1 to 10'''
even_numbers=[x**2 for x in range(1,11) if x%2==0]
print(even_numbers)