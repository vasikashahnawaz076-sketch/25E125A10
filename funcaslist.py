def double(x):
    return 2*x
def square(y):
    return y**2
def negate(z):
    return -z
functions=[double,square,negate]
value=7
print(functions[0](value))
print(functions[1](value))
print(functions[2](value))
for func in functions:
    print(func(value))
for func in functions:
    print(f"{func.__name__}  {value} ={func(value)}")
