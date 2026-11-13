import time
def timer(fun):
    def wrapper(*args, **kwargs):
        start=time.perf_counter()
        result=fun(*args, **kwargs)
        end=time.perf_counter()
        print(f"{fun.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def compute():
    total=sum(i*i for i in range(1000000))
compute()