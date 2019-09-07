import random
def main():
    userMove = input("Enter:")
    userMove = userMove.lower()
    if userMove not in ['rock','paper','scissors']:
        print("Invalid Move!")
        return 1
    else:
        r = random.randint(1,3)
        if r == 1:
            compMove = "rock"
        elif r == 2:
            compMove = "paper"    
        else:
            compMove = "scissors"
        if (userMove == "rock" and compMove == "scissors") or (userMove == "paper" and compMove == "rock") or (userMove == "scissors" and compMove == "paper"):
            print(userMove,"vs",compMove,"You win!")
        elif (userMove == compMove):
            print(userMove,"vs",compMove,"Draw")
        else:
            print(userMove,"vs",compMove,"Computer Wins")
        return 0

run = 1
while run == 1:
    run = main()