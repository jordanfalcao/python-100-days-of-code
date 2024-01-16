line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# initializing the index to be changed
first_index = 0
second_index = 0

# setting the first index based on the NUMBER
if position[1] == '1':
  first_index = 0
elif position[1] == '2':
  first_index = 1
else:
  first_index = 2

# setting the second index based on the LETTER
if position[0] == 'A':
  second_index = 0
elif position[0] == 'B':
  second_index = 1
else:
  second_index = 2

# setting the chosen index
map[first_index][second_index] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

###################################################################3
# ALTERNATIVE WAY

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# setting the NUMBER index
number_index = int(position[1]) -1

# setting the LETTER index
letter = position[0].lower()        # lower to get general cases
abc = ['a', 'b', 'c']               # 'abc' list to compare the letters
letter_index = abc.index(letter)    # seeting the letter index according to 'abc' list and the input given

# setting the chosen index: observe NUMBER is the first index and LETTER is the second one
map[number_index][letter_index] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")