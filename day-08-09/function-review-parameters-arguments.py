# Function Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# greet fuction with a input
# def greet(name):
#   print(f"Hello, {name}.")
#   print(f"How are you, {name}?")
#   print("Isn't the weather nice today?")

# greet(input("Whats is your name?"))

# function with more than 1 input
def greet_with(name, location):
  print(f"Hello, {name}.")
  print(f"How are you, {name}?")
  print(f"{location} is a nice place.")

# greet_with('Jordan', 'Cabedelo')

### or with an input
# greet_with(input("What is your name?"), input("Where are you from? "))

# if we set equalities to the arguments, it does'nt matter the order
greet_with(location = 'Cabedelo', name = 'Jordan')