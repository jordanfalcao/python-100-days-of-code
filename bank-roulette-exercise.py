names = names_string.split(", ")  
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

# import random module
import random 

# lenght of the list
length = len(names)

# randomly choosing a number from 0 to lenght of the list - 1
random_name = random.randint(0, length - 1)

# printing the name of the 
print(f"{names[random_name]} is going to buy the meal today!")