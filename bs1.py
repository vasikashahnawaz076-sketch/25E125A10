employees=[11,13,17,19,23,29,31,37,43,47]
target=int(input("Enter the id of the employee to search for:"))
employees.sort()
start=0
end=len(employees)-1
while start<=end:
    mid=(start+end)//2
    if employees[mid]==target:
        print("Found:", mid)
        break
    elif employees[mid]<target:
        start=mid+1
    elif employees[mid]>target:
        end=mid-1
else:
    print("Employee not found.")