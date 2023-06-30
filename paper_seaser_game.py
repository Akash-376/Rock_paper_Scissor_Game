import random

name = input("Enter your name")

total_matches = 0
draws = 0
userWins = 0
computerWins = 0
while True:
    num = random.randrange(3)
    # print(num)
    
    # computer = ""
    # if(num==0):
    #     computer = "stone"
    # elif(num==1):
    #     computer = "papper"
    # else:
    #     computer = "scissor"
    print("\n")
    userChoice = int(input("Enter your choice\npress 0 for stone\npress 1 for papper\npress 2 for scissor"))

    winner = ""
    if(num == userChoice):
        winner = "match draw"
    elif(num==0) and (userChoice==1):
        winner = name +" won"
    elif(num==0) and (userChoice==2):
        winner = "computer won"
    elif(num==1) and (userChoice==0):
        winner = "computer won"
    elif(num==1) and (userChoice==2):
        winner = name+" won"
    elif(num==2) and (userChoice==0):
        winner = name +" won"
    elif(num==2) and (userChoice==1):
        winner = "computer won"

    if(winner == "match draw"):
        draws+=1
    elif(winner == "computer won"):
        computerWins+=1
    else:
        userWins+=1

    total_matches += 1

    print(winner+"\n")

    cont = int(input("press 1 to continue\npress 0 to Exit"))

    if(cont==0):
        print("Game ended.")
        break


print("Result")
print("Total matches ", total_matches)
print("computer wins ", computerWins)
print("User wins ", userWins)
print("Total Draws ", draws)
