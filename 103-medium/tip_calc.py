"""
 1. Tip Calculator
Your task is to write a program that calculates how much of a tip to leave at a restaurant.

Prompt the user for two things:

The total bill amount
The level of service, which can be one of the following: good, fair, or bad
Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

good -> 20%
fair -> 15%
bad -> 10%
"""

total_bill_amount = float(input("Total bill amount? "))
level_of_service = input("Level of service? ")

level_good = total_bill_amount * 0.20
level_fair = total_bill_amount * 0.15
level_bad = total_bill_amount * 0.10

if level_of_service == "good":
    print("Tip amount: $", level_good)
    print("Total amount: $", level_good + total_bill_amount)
elif level_of_service == "fair":
    print("Tip amount: $", level_fair)
    print("Total amount: $", level_fair + total_bill_amount)
elif level_of_service == "bad":
    print("Tip amount: $", level_bad)
    print("Total amount: $", level_bad + total_bill_amount)