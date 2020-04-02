"""
2. Tip Calculator 2
Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst.
"""


total_bill_amount = float(input("Total bill amount? "))
level_of_service = input("Level of service? ")
split = int(input("Split how many ways? "))

level_good = total_bill_amount * 0.20
level_fair = total_bill_amount * 0.15
level_bad = total_bill_amount * 0.10

if level_of_service == "good":
    print("Tip amount: $", level_good)
    print("Total amount: $", level_good + total_bill_amount)
    print("Amount per person: $", (level_good + total_bill_amount) / split)

elif level_of_service == "fair":
    print("Tip amount: $", level_fair)
    print("Total amount: $", level_fair + total_bill_amount)
    print("Amount per person: $", (level_fair + total_bill_amount) / split)

elif level_of_service == "bad":
    print("Tip amount: $", level_bad)
    print("Total amount: $", level_bad + total_bill_amount)
    print("Amount per person: $", (level_bad + total_bill_amount) / split)