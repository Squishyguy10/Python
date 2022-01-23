# JSON (JavaScript Object Notation)
# It is a syntax(text) for storing and exchanging data
# JSONs are nested Lists and Dictionaries


def list():
    peoples = [
        {
            "name": "Bob",
            "city": "Toronto",
            "age": 4
        },
        {
            "name": "Joe",
            "city": "NA",
            "age": 39
        }
    ]

    for people in peoples:
        print()
        for key, value in people.items():
            print(key + ":", value)

def dict():
    data = {
        "peoples":
        [
            {
                "name": "Bob",
                "city": "Toronto",
                "age": 4
            },
            {
                "name": "Joe",
                "city": "NA",
                "age": 39
            }
        ]
    }

    print(data.items())

    for people in data["peoples"]:
        print()
        for key, value in people.items():
            print(key + ":", value)

def string_to_json():
    import json

    str_json = '[{"name": "John", "city": "Ottawa", "age": 30}, {"name": "Smith", "city": "Toronto", "age": 31}]'
    data = json.loads(str_json)
    print(data[0]["city"])

def write_and_read_json():
    import json

    data = {
        "peoples":
        [
            {
                "name": "Bob",
                "city": "Toronto",
                "age": 4
            },
            {
                "name": "Joe",
                "city": "NA",
                "age": 39
            }
        ]
    }

    with open("data.json", "w") as w_file:
        json.dump(data, w_file)

    with open("data.json", "r") as r_file:
        file = json.load(r_file)

    print(file)
    print(file[0])


# list()
# dict()
# string_to_json()
write_and_read_json()