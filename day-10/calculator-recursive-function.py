# creating operation functions (as many as you want)
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# dictionary from operation functions
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

from art import logo

# caculator function with RECURSION
def calculator():
  print(logo)
  continue_value = True  # flagging variable
  
  num1 = float(input("What's the first number?: "))  # first number input

  # while loop to continue calculating
  while continue_value:
    for symbol in operations:   # for loop to print out the operations
      print(symbol)
      
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    
    calculation_function = operations[operation_symbol](num1, num2)  # calling the operation function by the key of the dictionary
    answer = calculation_function
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    continue_question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
  
    if continue_question == "y":
      num1 = answer    # setting number 1 equal to the answer
    else:
      continue_value = False  # setting the flag to false to exit the while loop
      calculator()            # RECURSIVE FUNCTION

# callig the function
calculator()

