# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
# 
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    vowels = [ "A", "E", "I", "O", "U" , "a", "e", "i", "o", "u" ]

    # ask the user for their letter
    letter = input("Select your letter! ")
    
    # Check whether the input contains a letter or not
    if letter.isalpha():
        print("Input confirmed!")
    elif letter.isalnum():
        print("No numbers allowed")
    else:
        print("Please provide a value")
    # check whether the letter is a vowel or not
    if letter in vowels:
    # print if the value is a consonant or vowel 
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is not a vowel")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here

    # Ask for the users age
    age_input = input("Please provide your age ")
    # Error handling if the input isnt a valid number
    age = int(age_input)
    while not age:
        print("Your selection isnt valid")
        # give them another attempt
        age_input = input("Please provide your age ")
    # If the input is a number

    if age >= 18:
        print(f"This person is {age}, which makes them eligible to vote.")
    elif 0 < age < 18:
        print("This person needs to wait until they are at least 18 years old.")
    else:
        print("This person hasn't been born yet.")

    # if this input age is valid print a message stating so


# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here

    # input a dogs age
    while True:
        original_age = (input("How old is your dog? "))
        #check the number
        if original_age.isdigit():
            dog_age = int(original_age)
            break
        else:
            print("Please input a number")
    # if age <= 2 *math for n years
    if dog_age <= 2:
        human_years = dog_age * 10
    # if age > 2 *math for first n years
    else:
        human_years = 20 + (dog_age - 2) * 7
    # return the pets age in dog years
    print(f"The dog's age in dog years is {human_years}.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here

    # is it cold?
    # in FL? lol
    # but by FL standards ... 
    is_cold = input("Is it cold today? (yes/no)").strip().lower() == "yes"
    #is it raining?
    # in FL? duh
    is_raining = input("Is it raining today? (yes/no)").strip().lower() == "yes"

    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella")
    else:
        print("Wear light clothing")
# Call the function
weather_advice()
