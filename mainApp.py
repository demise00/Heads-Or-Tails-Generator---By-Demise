import random
import time

working = True
while working == True:

    print("How many flips do you want? ")
    tries = int(input("Flips: "))
    possibilities = ["Heads", "Tails"]
    headsCount = 0
    tailsCount = 0
    amount_of_tries = 0

    for i in range(tries):
        randomSide = random.choice(possibilities)
        if randomSide == "Tails":
            tailsCount += 1
        elif randomSide == "Heads":
            headsCount += 1
        amount_of_tries += 1
        print(amount_of_tries, end='\r')
        
    

    print("Done! This is the amount of heads and tails you've gotten!")
    print("TAILS: " + str(tailsCount))
    print("HEADS: " + str(headsCount))


    restart = input("Do you want to restart and try again? [yes/no] ")
    if restart.lower() == "yes":
        working = True
    else: 
        print("Goodbye!")
        time.sleep(0.5)
        working = False

