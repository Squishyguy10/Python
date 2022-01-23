# # Map in C++
# car_dict = {
#     "brand": "Toyota",  # Key: Value
#     "colour": "Grey",
#     "year": "2001",
# }

# print(car_dict)
# print(car_dict["colour"])       # If it doesn't exist, it will break
# print(car_dict.get("colour"))   # If it doesn't exist, it will print "none"
# print(len(car_dict))
# if "brand" in car_dict:
#     print("Found brand")

# print(car_dict.get("flying_car, no"))   # If 1st doesn't exist, it print 2nd

# # ---------------------------------------------------------------------------------------------- #
# # Add/modify
# car_dict["seats"] = "5" # Add
# car_dict["year"] = "2005" # change

# # Deleting
# car_dict.pop("model") 
# del car_dict["model"]

# # Removes last item
# car_dict.popitem()

# # 2 ways to empty dict (still exists)
# car_dict.clear()
# del car_dict

# # ---------------------------------------------------------------------------------------------- #
# # Iterating
# for key in car_dict:
#     print(key)
#     print(car_dict[key])

# for value in car_dict.values():
#     print(value)

# for key, value in car_dict.items():
#     print(key, value)

# new_car_dict = car_dict # changes when you change car_dict
# new_car_dict = car_dict.copy() # Makes an actual copy

# # Sorting
# for key in sorted(car_dict): # Dict itself doesn't change
#     print(key)
#     print(car_dict[key])

family = {
    "child1": {
        "name": "aron yand",
        "age": 2,
        "height": 3
    },
    "child2": {
        "name": "squingy",
        "age": 80,
        "height": 298
    },
    "child3": {
        "name": "mingwon",
        "age": 1012,
        "height": 23
    }
}

for child_num, qualities in family.items():
    print("\n" + child_num)

    for key, value in qualities.items():
        print(key + ':', value)
