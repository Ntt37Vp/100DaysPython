# f = open("my_file.txt", "r")
# print(f.read())
# f.close()


# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# appends contents on existing file
with open("my_file.txt", "a") as file2:
    file2.write("\nNew line added.")

# create a new file with contents
with open("new_file.txt", "w") as file3:
    file3.write("Hello World!")
