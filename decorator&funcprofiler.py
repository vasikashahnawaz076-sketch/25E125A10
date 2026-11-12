'''def my_decorator(fn):
    def wrapper():
        print("Before 'fn' execute")
        fn()
        print("After 'fn' execute")
    return wrapper'''

def greet():
    print("Hello:Section F3")
def my_decorator(fun):
    def wrapper():
        print("Before the greet")
        fun()
        print("After the greet")
        fun()
    return wrapper
decorated_greet=my_decorator(greet)
decorated_greet()