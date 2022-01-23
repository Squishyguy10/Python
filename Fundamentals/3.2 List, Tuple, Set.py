fruits = ["apple", "banana", "orange", "melon"]

def access():
    print(fruits)
    print(fruits[1])        # Index 1
    print(fruits[-1])       # Index -1 is the last one (-2 would be 2nd last)
    print(fruits[0:2])      # Items from index 0-2
    print(len(fruits))      # Size of list

    other_list = ["apple", "banana", "orange", 1, 2, 'c', 3.1]

    if "apple" in fruits:       # Find function
        print("Found apple")

def add_and_modify():
    # Add a fruit to fruit_list from the end
    fruits.append("cherry")
    print(fruits)

    # Add a fruit to fruit_list from anywhere by index
    fruits.insert(1, "pear")    # (index, item)
    print(fruits)

    # Modify item
    fruits[1] = "lemon"
    print(fruits)

def remove():
    # Remove a specific item
    fruits.remove("banana")
    print(fruits)

    # Removes  the specified index, or the last item if index is no specified
    fruits.pop()        # Removes last element
    print(fruits)

    fruits.pop(1)       # Removes fruits[1]
    print(fruits)

    fruits.clear() # Empties the list

def iterate():
    # Iterate list by index
    for i in range(len(fruits)):
        print(fruits[i])

    # Iterate list by item
    for i in fruits:
        print(i)

def copy():
    # Just the pointer, changing new_fruits will change fruits
    # new_fruits = fruits       Incorrect
    # new_fruits[0] = "a", so fruits[0] is "a" now

    # 2 different lists with the same data
    new_fruits = fruits.copy()

def sort():
    # The default order is ascending
    list1 = [5, 4, 7, 1, 3]
    list1.sort()
    print(list1)

    # Make a new list with sort
    old_list = [8, 3, 6, 2, 4]
    new_list = sorted(old_list)
    print(old_list)
    print(new_list)

    # Descending
    old_list.sort(reverse = True)
    print(old_list)

def extend():
    # Combine two lists with different data types
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3)

    list1.extend(list2)
    print(list1)

def append():
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    list1.append(list2)
    print(list1)

    # Append a list to a list
    # ist['a', 'b', 'c', [1, 2, 3]]

# access()
# add_and_modify()
# remove()
# iterate()
# copy()
# sort()
# extend()
append()