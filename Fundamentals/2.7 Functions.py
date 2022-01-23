def empty_function():   # No data type
    pass        # Do nothing

def my_function(num1, num2, num3 = 15):
    print("Number 3 is", num3)

my_function(num2 = 5, num1 = 10)
my_function(num1 = 5, num2 = 10, num3 = 20)