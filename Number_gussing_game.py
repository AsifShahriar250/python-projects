# This Python code generates a random number between 1 and 100 using the `random.randint(1, 100)`
# function. It then prompts the user to enter a number between 1 and 100.


import random

a=random.randint(1,100)
while True:
  try:
    
    num=int(input("Enter a number between 1 to 100: "))

    if num==a:
      print("Congratulation.")
      break
    elif num > a:
      print("Try small number")
    elif num<a:
      print("Try big number")
    else:
      print("invalid number")
  except ValueError:
    print("Enter valid number")