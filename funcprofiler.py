'''import time
t1=time.time()
time.sleep(3)
t2=time.time()
print("Execution time:", t2 - t1)'''

import time
def calculate():
    a,b,c=10,20,30
    d=a+b+c
    return d
def calculate_time(fun):
    def wrapper():
        t1=time.time()
        r=fun()
        time.sleep(10)
        t2=time.time()
        print("Execution time:", t2 - t1)
    return wrapper
cal=calculate_time(calculate)
time_taken=cal()
print(time_taken)
