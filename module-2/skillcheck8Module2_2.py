# Name: Brian Guadron
# Date: 11/01/2026
# Assignment Number - Module 1.2 Assignment - Documented Debugging + Flowchart(s)
#
# Purpose - The purpose is to develop a Python program that creates and use functions to add two numbers. One function prints the result, while the other returns the result
# so it can be stored in the variable and printed later.
#

# Created a function that prints the sum result when the function gets called
# The function takes two parameters as number
# The functions print the result of the sum of the two numbers
def sum_and_print(number_1, number_2):
    sum_result = number_1 + number_2
    print(f"The result of the sumAndPrint function is: {sum_result}")


# Created a function that returns the sum result when the function gets called
# The function takes two parameters as number
# The functions returns the result of the sum of the two numbers
def sum_and_return(number_1, number_2):
    sum_result = number_1 + number_2
    return sum_result

# Calling the sum_and_print function which prints the result from inside the function
sum_and_print(5, 10)

# Calling the sum_and_return function which returns the result of the sum value
# Storing the result returned by the sum_and_return into my returned_result variable
# Then printing the value of the returned_result variable
returned_result = sum_and_return(15, 20)
print(f"The result of the sumAndReturn function is: {returned_result}")