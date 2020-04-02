"""
3. How many coins?
Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. Example run:
"""

coins = 0
print("You have %s coins" % (coins,))

more_coins = True

while more_coins:
    request = input("Do you want another? ")
    
    if request.lower() == "yes":
        coins += 1
        print("You have %s coins." % (coins,))

    elif request.lower() == "no":
        more_coins = False
        print("Bye")

    else:
        print("That is not a valid input. Enter 'Yes' or 'No'")