'''write a function to check whether the password is good or not'''

def check_password(password):
    length=check_length(password)
    alpha=check_alpha(password)
    num=check_num(password)
    if length and alpha and num:
        return "Good password"
    else:
        return "Bad password"
    
def check_length(password):
    n=len(password)
    if n>=8:
        return True
    else:
        return False

def check_alpha(password):
    for ch in password:
        if ch>="a" and ch <="z":
            return True
    else:
        return False

def check_num(password):
    for num in password:
        if num.isdigit():
            return True
    else:
        return False

password =input("Enter a password:")
print (check_password(password))

