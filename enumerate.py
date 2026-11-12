'''Enumerate()
It automatically add the index to print the counter

It works on any iterable:Tuples,List,Strings

It returns a pair value(Index,Value) for each element.'''

'''fruits=['banana','orange','apple','mango']
c=1
for x in fruits:
    print(c,":",x)

efruits=list(enumerate(fruits,start=0))
print(efruits)

for index, fruit in enumerate(fruits,start=1):
    print(index,":"<fruit)

for index,fruit in enumerate (fruits):
    if(fruits=="apple"):
        print(index)'''

'''Find roll number'''

roll = [11, 12, 13, 9, 17, 36, 23, 19]
for index, number in enumerate(roll):
    if number == 19:
        print("Found", number, "at", index)


