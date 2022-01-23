import sys

# var = input()  # everything is a string when you input it. You will need to convert the data type to other stuff like an int if u need to use it

# print(var)
# print(type(var))
# print(type(int(var)))

# my_int = int(input("Enter integer: ")) # Data type is string
# my_float = float(input("Enter integer: ")) # Data type is string

print("Hello World!", "Good!\nBye")
x = "xyz"
y = 3.14
    # Format #1
print("x = {}, y = {}".format(x, y))
    # Format #2
print("x = {:>7}, y = {:.2f}".format(x, y))
    # Format #3
print(f"x = {x:>8}, y = {y:.2f}")