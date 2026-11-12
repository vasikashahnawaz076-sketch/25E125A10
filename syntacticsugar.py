def greet():
    print("Hello")

def my_greet(fun):
    def wrapper():
        print("Before")
        fun()
        print("After")
    return wrapper
'''decorated_greet=my_greet(greet)
decorated_greet()'''

@my_greet
def greet():
    print("Hello")
greet()

@my_greet
def Hello():
    print("Hi")
Hello()