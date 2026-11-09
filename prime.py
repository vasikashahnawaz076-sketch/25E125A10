list=[]
for i in range(1, 25):
    list.append(i)
print(list)

for j in range(2, 6):
    for k in range(len(list)):
        if list[k] % j == 0 and list[k] != j:
            list[k]=0
print(list)

prime=[]
for x in list:
    if x != 0:
        prime.append(x)
print(prime)


    
