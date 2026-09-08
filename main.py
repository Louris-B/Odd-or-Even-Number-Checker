num = int(input("Enter a positive whole number: ")) #Asks the user for the value of num

if num < 0: #Checks whether num is a positive whole number
    print("The value must be positive, please try again.") #Tells the user to retry
else:
    if num % 2 == 0: #Checks whether num is even
        print(f"{num} is even.") #What it outputs for num is even
    else:
        print(f"{num} is odd.") #What it outputs for num is odd
