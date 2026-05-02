import random
choices= ('r','p','s')
while True:
  user_choice=input("Rock, paper,or scissors(r/p/s): ").lower()
  if user_choice not in choices:
    print("Invalid choice")
    continue
  computer_choice=random.choice(choices)
  print(f"You choice {user_choice}")
  print(f"Computer choice {computer_choice}")
  if computer_choice==user_choice:
    print("Its a draw!") 
  elif(user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
    print("🎉 You win!")
  else:
    print("Computer win")
  a=input("Continue?(y/n): ").lower()
  if(a=="n"):
    break