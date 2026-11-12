'''calculate the mean of a list of numbers'''
def mean(nums):
    m=sum(nums) / len(nums)
    print(m)
nums=[1,2,3,4,5]
mean(nums)

def mean(*nums):
    m=sum(nums)/len(nums)
    return m
    print(mean(1,2,3,4,5))
    print(mean(1,2,3))
    print(mean(1,2,3,4,5,6,7,8,9,10))

def fun_name(*args):
    print(args)