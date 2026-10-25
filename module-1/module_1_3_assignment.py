# Name: Brian Guadron
# Date: 10/25/2026
# Assignment Number - Module 1.3 Assignment
#
# Purpose - The purpose is to develop a Python program that ask the user how many bottles of beer are on the wall, then count down to one bottle, and then remind the user to
# buy more bottles of beer.
#
# Resource: I used stackoverflow posts to complete the assignment.
# stackoverflow url: https://stackoverflow.com/questions/16141476/calculating-gpa-with-classes-using-credits-and-grades


# Created a function that takes the number of bottles from the user
# If the user input is greater than 1, it will continue with the print statement, it will decrease the bottle count by 1, then break the condition
# once bottle count is not greater than 1
def bottles_countdown(bottles_count):
    while bottles_count > 1:
        print(f"{bottles_count} bottles of beer on the wall, {bottles_count} bottles of beer.")
        print(f"Take one down and pass it around, {bottles_count - 1} bottle(s) of beer on the wall.")
        print()
        bottles_count = bottles_count - 1

# When bottles count equal 1, it will do the print the statement with a single bottle
    if bottles_count == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, 0 bottle(s) of beer on the wall.")

# Asking the user to provide a bottle count value
user_bottles = int(input("Enter the number of bottles: "))
print()

# Calling the bottle count function
bottles_countdown(user_bottles)

# Prints then message tha lets the user know they need to buy more beers
print()
print("Time to buy more bottles of beer.")