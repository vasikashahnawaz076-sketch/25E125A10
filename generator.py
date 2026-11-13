'''def count_up_to(n):
    i=1
    while i<=n:
        yield i
        i+=1
for x in count_up_to(5):
    print(x)'''

'''write a program to create a generator_function "filter_high_Sales" that take list of daily sales amount and a threshold value.The function should yield only those values which are greater than the threshold value'''

def filter_high_sales(sales, threshold):
    for sale in sales:
        if sale > threshold:
            yield sale
sales_amounts = [100, 200, 150, 300, 250, 400]
threshold_value = 200
for high_sale in filter_high_sales(sales_amounts, threshold_value):
    print(high_sale)
