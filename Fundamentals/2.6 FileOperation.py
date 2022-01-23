import sys

def file_write():
    # file = open("filename.txt", "w")
    # file.write("Now the file has more context")
    # file.close()

    # Better way "w" "a"    w = overwrite     a = append (add on)
    with open("filename.txt", "w") as w_file:    # true
        w_file.write("Hello World!\n")
        w_file.write("Hello World!")


def file_read():
    # Reading files         r = read
    with open("filename.txt", "r") as r_file:
        # Method 1
        for line in r_file:
            print(line)

        # Method 2      only reads the first line of the file
        print(r_file.readline())

        # Method 3
        print(r_file.readlines())

file_write()
file_read()