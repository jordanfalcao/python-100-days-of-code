# Write your code here 👇

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0: # number is divisible by both 3 and 5
    print("FizzBuzz")
  elif i % 3 == 0:              # number is divisible by 3
    print("Fizz")
  elif i % 5 == 0:              # number is divisible by 5
    print("Buzz")
  else:                         # else print the number itself
    print(i)