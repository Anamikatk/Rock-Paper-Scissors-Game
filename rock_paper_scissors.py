#game : rock,paper,scissors
import random
rock="🧱"
paper="🧻"
scissors="✂️"
game_image=[rock,paper,scissors]
user_choice=int(input("Enter your choice - Type 0 for ROCK ,1 for PAPER, 2 for SCISSORS :  "))
if user_choice>=3 or user_choice<0:
    print("You entered INVALID number :| , YOU LOSE :(")
else:
    print("User Choice :",game_image[user_choice])
    computer_choice=random.randint(0,2)
    print(computer_choice)
    print("Computer Choice : ",game_image[computer_choice])
    if(computer_choice==user_choice):
         print("It's a DRAW.")
    elif computer_choice==0 and user_choice==2:
        print("COMPUTER WIN ")
    elif computer_choice == 2 and user_choice == 0:
        print("YOU WIN :) ")
    elif computer_choice > user_choice:
        print("YOU LOSE :( ")
    elif computer_choice< user_choice:
        print("YOU WIN :) ")
