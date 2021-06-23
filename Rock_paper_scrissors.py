import random 

computer_pick = random.choice(['Rock','Paper','Scissors'])
your_pick = input("pick from Rock, Paper, Scissors\n")

if computer_pick == your_pick:
    print("TIE")
    print("Computer picked " + computer_pick)
elif your_pick == "Rock" and computer_pick == "Scissors":
    print("WIN")
    print("Computer picked " + computer_pick)
elif your_pick == "Paper" and computer_pick == "Rock":
    print("WIN")
    print("Computer picked " + computer_pick)
elif your_pick == "Scissors" and computer_pick == "Paper":
    print("WIN")
    print("Computer picked " + computer_pick)
else: 
    print("You lose, succer!")
    print("Computer picked " + computer_pick)
