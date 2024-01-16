print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# put all letters in lowercase
name1_lower = name1.lower()
name2_lower = name2.lower()

# count the TRUE letters in the names
t = name1_lower.count('t') + name2_lower.count('t')
r = name1_lower.count('r') + name2_lower.count('r')
u = name1_lower.count('u') + name2_lower.count('u')
e = name1_lower.count('e') + name2_lower.count('e')

true_total = t + r + u + e

# count the LOVE letters in the names
l = name1_lower.count('l') + name2_lower.count('l')
o = name1_lower.count('o') + name2_lower.count('o')
v = name1_lower.count('v') + name2_lower.count('v')

love_total = l + o + v + e

# concatenate the two numbers
total = int(str(true_total) + str(love_total))

# conditional of the problem
if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")

