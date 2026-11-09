roll =[11,13,9,27,23,37,41,55,17,26]
start=0
end=len(roll)
mid=(start + end)//2
n=int(input("Enter the roll number of the student:"))
while (start<end):
    if (roll[mid]==n):
        print("Found", mid)
        break
    elif roll[mid]>n:
        s=mid+1
        