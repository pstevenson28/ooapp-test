# sum_value=5+3

# sum_2=6+sum_value
# print(sum_value)

# my_list = [1,2,3,4] # Initialize my_list

# my_list_2 = [5,6,7,8] # Initialize my_list_2

# my_list = my_list + my_list_2 # Take the current value of my_list and add my_list_2 to it

# print(my_list) # Prints: [1, 2, 3, 4, 5, 6, 7, 8]

# print(5 > 3) # Prints: True; since 5 is greater than 3

# result = 5 > 3 # You can store the result in a variable

# print(result) # Prints: True

# print(3 > 5) # Prints: False; since 3 is NOT greater than 5

# print(5 > 5) # Prints: False; since 5 is NOT greater than 5 (they are equal)

"""
    =========== Exercise 1 =============
    I have provided some starter code below
    that creates a result variable, and a number_1
    variable. Your goal is to make number_1 equal 11
    after the operations that have been done to it.
"""
result = 0
number_1 = 5
number_1 += 52
number_1 += 9
number_1 /=6
# Do more operations on number 1 until it equals eleven
result = number_1
print(result == 11)
"""
    =========== Exercise 2 =============
    Take input from the command line, and convert it to
    an int. Now pick a range (i.e. 0-10), and create a set
    of conditional statements that prints the string
    representation of the number input by the user.
    For example if someone put in 8, then it would print 'eight'.
    Hint: Use if, elif and else statements.
"""
"""
    =========== Exercise 3 =============
    Before running the code below try to
    figure out which print statement will
    execute and why. Then uncomment the code
    and check if you were right.
"""
# number = 0
# number += 15
# number //= 2
# number *= 6
# number -= 4
# if number < 10:
#     print("Less than 10")
# elif 10 <= number <= 20:
#     print("Between 10 and 20")
# elif 20 <= number <= 30:
#     print("Between 20 and 30")
# elif 30 <= number <= 40:
#     print("Between 30 and 40")
# else:
#     print("Â¯\_(ãƒ„)_/Â¯")