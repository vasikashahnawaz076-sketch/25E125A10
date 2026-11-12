'''x=[1,2,3,4,5,6,7]
y=[3,1,7,4,5]
y.sort()
print(y)'''

'''words=["banana", "apple", "cherry", "date"]
words.sort()
reverse=True
print(words)
words.sort(key=len)
print(words)
words.sort(key=len, reverse=True)
print(words)'''

'''a=[10,20,30,40]
a.insert(100,70)
print(a)'''

a_list=["ram","Anu","mohan","babul","Nitin","payal","Khidisj"]
b_list=a_list[:]
a_list.sort()
print(a_list)
a_list.sort(key=len)
print(a_list)
a_list.sort(key=str.casefold)
print(a_list)