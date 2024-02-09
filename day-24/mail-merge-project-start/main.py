# TODO: Create a letter using starting_letter.txt

with open("Input/Names/invited_names.txt") as file:
    names = []

    # Iterate over the lines of the file
    for line in file:
        # Remove the newline character ('\n') at the end of the line
        line = line.strip()

        # Append the line to the list
        names.append(line)

# read all the text and sets to variable 'letter'
with open("Input/Letters/starting_letter.txt") as f:
    letter = f.read()

# write the letters in the ReadyToSend folder:
letters = []
for name in names:
    new_letter = letter.replace('[name]', name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f2:
        f2.write(new_letter)
