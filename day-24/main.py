# read and write files

# # open and read thw file:
# file = open("my_file.txt")  # open the file .txt
# contents = file.read()  # read all the text and sets to our variable
# print(contents)
# file.close()  # close the opened file - performs better

# # another way to open, we don't need to close the file:
# # when we've done with the file, 'with' keyword will close it
# with open("my_file.txt") as file:
#     contents = file.read()  # read all the text and sets to our variable
# print(contents)

# # delete the contents and write over in the file mode="w":
# with open("my_file.txt", mode="w") as file:
#     file.write("My favorite place is the beach.")

# # append new contents in the file mode="a":
# with open("my_file.txt", mode="a") as file:
#     file.write("\nMy favorite place is the beach.")

# if the file you open in 'w' mode doesn't exist, it'll create the file for you:
with open("new_file.txt", mode="w") as file:
    file.write("Creatine another .txt file with open in mode='w'.")