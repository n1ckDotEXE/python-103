# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.

start_num = int(input("Starting Number: "))
end_num = int(input("Ending Number: "))
num = start_num - 1
while num < end_num:
    num = num + 1
    print(num)