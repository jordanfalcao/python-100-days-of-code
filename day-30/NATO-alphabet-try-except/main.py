import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


# nato alphabet using Try - Except and Recursive function
def nato_alphabet():
    word = input("Enter a word: ").upper()  # input the word
    try:
        # create a list with the values of the dictionary corresponding with each letter (key) of the word
        name_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        nato_alphabet()  # recursive
    else:
        print(name_list)


nato_alphabet()