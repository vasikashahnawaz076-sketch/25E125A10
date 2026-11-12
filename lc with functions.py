def square(x):
    return x**2
result=[square(x) for x in range(1,11)]
print(result)

def even(y):
    if y%2==0:
        return True
    else:
        return False
result=[y for y in range(1,101) if even(y)]
print(result)
    