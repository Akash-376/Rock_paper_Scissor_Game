import random

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# taking name of the current player
name = input("Enter your name : ")

# some counters to keep record
total_matches = 0
draws = 0
userWins = 0
computerWins = 0
while True:
    num = random.randrange(3)
    '''
        if num is equal to 0 then computer choice will be "Stone"
        if num is equal to 1 then computer choice will be "Paper"
        if num is equal to 2 then computer choice will be "Scissor"
    '''
    
    try:
        print("\n")
        userChoice = int(input("Enter your choice\npress 0 for stone\npress 1 for papper\npress 2 for scissor\n"))
    
        if userChoice == 0 or userChoice==1 or userChoice==2:


            winner = ""
            res = ""
            if(num == userChoice):
                winner = YELLOW+"match draw"+RESET
                res = GREEN+"Result : "+RESET+"Match Draw due to same choices"
                draws+=1
            elif(num==0) and (userChoice==1):
                winner = GREEN+name +" won"+RESET
                res = GREEN+"Result : "+RESET+"Paper can wrap the stone"
                userWins+=1
            elif(num==0) and (userChoice==2):
                winner = YELLOW +"computer won"+RESET
                res = GREEN+"Result : "+RESET+"Stone can break the scissor"
                computerWins+=1
            elif(num==1) and (userChoice==0):
                winner = YELLOW +"computer won"+RESET
                res = GREEN+"Result : "+RESET+"Paper can wrap the stone"
                computerWins+=1
            elif(num==1) and (userChoice==2):
                winner = GREEN+name +" won"+RESET
                res = GREEN+"Result : "+RESET+"Scissor can cut the paper"
                userWins+=1
            elif(num==2) and (userChoice==0):
                winner = GREEN+name +" won"+RESET
                res = GREEN+"Result : "+RESET+"Stone can break the scissor"
                userWins+=1
            elif(num==2) and (userChoice==1):
                winner = YELLOW +"computer won"+RESET
                res = GREEN+"Result : "+RESET+"Scissor can cut the paper"
                computerWins+=1

      

            total_matches += 1
            if num==0:
                print(YELLOW+"computer choosed Stone"+RESET)
            elif num==1:
                print(YELLOW+"computer choosed Paper"+RESET)
            else:
                print(YELLOW+"computer choosed Scissor"+RESET)
            print(winner+"\n")
            print(res)
            print()

            cont = int(input("press 1 to continue\npress 0 to Exit "))

            if(cont==0):
                print("Game ended.")
                break
        else:
            print(RED+"Invalid choice. please try again..."+RESET)
    except ValueError:
        print(RED+"Invalid Input type. Please try again with valid number"+RESET)

# final result
print(GREEN+"\n --------------- Score board --------------"+RESET)
print("\nTotal matches ", total_matches)
print("\ncomputer wins ", computerWins)
print("\nUser wins ", userWins)
print("\nTotal Draws ", draws)
print(GREEN+"\n ------------------- END ------------------"+RESET)
