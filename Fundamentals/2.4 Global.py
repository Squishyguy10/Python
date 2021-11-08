i = 10
def function_i():
    global i
    i = 20
    print(i)
    
print(i)
function_i()
print(i)