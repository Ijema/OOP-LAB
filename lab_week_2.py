# I. Comparisons and Conditionals

# Exercise 1: Comparison Operators 

# Task: Follow this link and click on the Try It button for each of the comparison operators. Change the
# values for each x variable to make the comparisons false.
# After this, you should be able to build your comparisons successfully based on variable

# The == operator checks for equality.
x = 10
y = 4
print(x == y) # Returns False because 10 is not equals to 4

# The != operator checks for inequality.
x = 10
y = 10
print(x != y) # Returns False because 10 is equals to 10

# The > operator checks if the left operand is greater than the right operand.
x = 4
y = 10
print(x > y) # Returns False because 4 is not greater than 10

# The < operator checks if the left operand is less than the right operand.
x = 10
y = 4
print(x < y) # Returns False because 10 is not less than 4

# The >= operator checks if the left operand is greater than or equal to the right operand.
x = 4
y = 10
print(x >= y) # Returns False because 4 is not greater than or equal to 10

# The <= operator checks if the left operand is less than or equal to the right operand.
x = 10
y = 4
print(x <= y) # Returns False because 10 is not less than or equal to 4


# Exercise 2: Logical Operators

# Task: Follow this link and click on the Try It button for each of the comparison operators. Change the
# values for each x variable to make the comparisons false.
# After this, you should be able to build your comparisons successfully based on variable

# The AND operator returns True if both operands are true.
print("Enter your age and height to check the conditions.")
Age = int(input("Enter your age: "))
Height = int(input("Enter your Height: "))
print("Checking for the AND operator to see if the age is greater than 15 and height is greater than 5.5:")

print(Age > 15 and Height > 5.5)  # Returns False if Age is not greater than 15 or Height is not equal to 5.5

# The OR operator returns True if at least one of the operands is true.
print("Checking for the OR operator to see if the age is greater than 15 or height is greater than 5.5:")

print(Age > 15 or Height > 5.5)  # Returns True if Age is greater than 15 or Height is greater than 5.5

# The NOT operator negates the truth value of the operand.
print("Checking for the NOT operator to see if the age is not greater than 15 and height is not greater than 5.5:")

print("For the not operator in the and condition:")
print (not(Age > 15 and Height > 5.5))  # Returns True if Age is greater than 15 and Height is not greater than 5.5
print("For the not operator in the or condition:")
print (not(Age > 15 or Height > 5.5))  # Returns True if Age is not greater than 15 and Height is not greater than 5.5

# Exercise 3: If - Conditionals

# Task: Run this program twice, once with the given age and once when you change the age to something
# below 18. Observe the output and you will see that depending on the age, the age_group changes

# The code checks the age of the user and assigns them to an age group based on their age.
age = int(input("Enter your age: "))
age_group = "child"

if (age >= 18):
    age_group = "adult"
    print(f"You are {age} years old, you are an {age_group}, and you can vote")
else: 
    print(f"You are not eligible to vote yet, You are a {age_group}, please wait until you turn 18.")

# Exercise 4: if – else Conditionals

# Task: Run this program twice, once with the given wind speed and once when you change the speed to
# something below 10. Observe the output and you will see that depending on the wind speed, different
# parts will be executed. 

# Program 1
# Testing with a wind speed of above 11
wind_speed = 40

if wind_speed < 11: 
    print("The wind speed is low. It's a calm day, you can go outside and enjoy the weather.")
else: 
    print("The wind speed is high. It's a windy day, you should stay indoors or be cautious if you go outside.")

# Program 2
# Testing with a wind speed of below 11
wind_speed = 4

if wind_speed < 11: 
    print("The wind speed is low. It's a calm day, you can go outside and enjoy the weather.")
else: 
    print("The wind speed is high. It's a windy day, you should stay indoors or be cautious if you go outside.")

# Exercise 5: if – elif - else Conditionals

# Task Compare Temperatures:
    # 1) Create two variables, temperature1 and temperature2, and assign different values to them.
    # 2) Use an if statement to check if the temperatures are equal and print a corresponding message.
    # 3) Use an else statement to print a message if the temperatures are not equal.
    # 4) Run the code and see if your statement has been built correctly.

# 1) Create two variables, temperature1 and temperature2, and assign different values to them.
temperature1 = input("Enter the first temperature: ")
temperature2 = input("Enter the second temperature: ")

# 2) Use an if statement to check if the temperatures are equal and print a corresponding message.
if  temperature1 == temperature2:
    print("Yes!! The two Temperatures are the same")

# 3) Use an else statement to print a message if the temperatures are not equal.
else:
    print("No!! The two Temperatures are not the same")


# II. PYTHON LISTS

# Exercise 1: Creating a list

# Task: Create a list in the variable city_list. It should contain the following items in this order:
# "Glasgow", "London", "Edinburgh”.

city_list = ["Glasgow", "London", "Edinburgh"]

# Exercise 2: Accessing a list

# Task: Print the third item in the city_list list. Then print the last two items in the city_list list as
# well using slicing.

# Printing the length of the list
city_length = len(city_list)
print(f"The number of city in the list is {city_length}.")

# Printing the last city in the list
city_list_third = city_list[2]
print(f"The the third city in the list is {city_list_third}.") # This will return "The third city in the list is Edinburgh"

# To achieve the above also, we could also do the following
city_list_third = city_list[-1]
print(f"The the third city in the list is {city_list_third}.") # This will return "The third city in the list is Edinburgh".
# But this is not ideal as the third city might not be the last. But in this case,
# we were able to get the same value because the third city was indeed the last city

# Printing the last two city in the list
last_two_city = city_list[1:3]
print(last_two_city)
print(f"The the last two city in the list is {last_two_city[0]} and {last_two_city[1]}.") # This will return "The last two city in the list is London and Edinburgh".

# Exercise 3: Modifying a list

# Task: Add the item "Manchester" to the end of the city_list list. Then change the second item in the
# city_list list to "Birmingham".

# Adding Machester to the end of the list
city_list.append("Manchester")
print(f"The updated city list is {city_list}.")

# Changing the second item in the list to Birmingham
city_list[1] = "Birmingham"
print(f"The updated city list is {city_list}.")

# Exercise 4: Summary Task
# Task Create, Access and Modify Lists:
    # • Write Python code to create a list named colours containing the names of three colours as strings.
    # • Print the entire list.
    # • Access the second element of the colours list and print it.
    # • Modify the first element of the list to a new colour of your choice.
    # • Print the modified list.
    # • Check and print the length of the colours list using the len() method. This is similar to using the similar to using the type() method from before.
    # • Use a conditional to check if "red" is in the colours list. If yes, print that “Red is in the list”.
    # • Use slicing to create a new list named selected_colours containing the second and third elements from the colours list.
    # • Print the selected_colours list

# Creating a list named colours
colours = ["red", "green", "red"]
# Printing the entire list
print(f"The colours list is {colours}.")
# Accessing the second element of the colours list
secound_colour = colours[1]
# Printing the second element
print(f"The second colour in the list is {secound_colour}.")
# Modifying the first element of the list to a new colour
colours[0] = ["purple"]
# Printing the modified list
print(f"The updated colours list is {colours}.")
# Checking the length of the colours list
colours_length = len(colours)
# Printing the length of the colours list
print(f"The number of colours in the list is {colours_length}")
# Checking if "red" is in the colours list
if "red" in colours:
    print("Red is in the list.")
else: 
    print("Red is not in the list.")
# Slicing to create a new list named selected_colours
selected_colours = colours[1:3]
# Printing the selected_colours list
print(f"The selected colours list is {selected_colours}.")


# III. PYTHON LOOPS
# Exercise 1: While Loops

# Exercise 2: For Loops
# Task: Create a for loop that prints each item in the city_list list.
print("The list contains the following city")
for city in city_list:
    print(city) # This will print each city in the city_list {Glasgow, Birmingham, Edinburgh, Manchester}

# Exercise 3: Loop Keywords: Range, break and continue
# Task: Modify the above code to print the numbers 0 through 4, but stop the loop when i is equal to 3.
for i in range(5):
    if i ==3:
        break
    print(i) # This will print 0, 1, 2

# Let us say we want to continue counting from 0 to 4, but skip the number 3.
for i in range(5):
    if i == 3:
        continue
    print(i) # This will print 0, 1, 2, 4

# Exercise 4: Summary Tasks
# Task – Even Numbers
    # 1. Create a list called numbers which contains the integers from 1 to 10.
    # 2. Use a for loop to iterate through the list and only print the even numbers. (Hint: use the modulo % operator)

# 1. Creating a list called numbers which contains the integers from 1 to 10
numbers = list(range(1, 11)) # This will create a range object from 1 to 10
print(f"The numbers in the list are {numbers}")

# 2. Using a for loop to iterate through the list and only print the even numbers
print("The even numbers in the list between 1 and 10 are:")
for i in numbers:
    if i % 2 == 0:
        print (i) # This will print 2, 4, 6, 8, 10

# Task – Sum of Squares
    # 1. Create a variable sum_of_squares and initialize it to 0.
    # 2. Use a for loop to iterate through the numbers from 1 to 5 (inclusive) using the range() function.
    # 3. Add the square of each number to sum_of_squares.
    # 4. Print the final value of sum_of_squares. (Hint: if you do it correctly, the result should be 55)

# 1. Creating a variable sum_of_squares and initializing it to 0
print("")
sum_of_squares = 0

# 2. Using a for loop to iterate through the numbers from 1 to 5 (inclusive) using the range() function
print ("The current number is:")
for i in range(1, 6):
    print(i) # This will print 1, 2, 3, 4, 5

# 3. Adding the square of each number to sum_of_squares
    sum_of_squares += i**2 # This will add the square of each number to sum_of_squares

# 4. Printing the final value of sum_of_squares
print(f"The sum of squares from 1 to 5 is {sum_of_squares}.") # This will print "The sum of squares from 1 to 5 is 55"

# Task – Countdown:
    # 1. Create a variable countdown and initialize it to 10.
    # 2. Use a while loop to print a countdown from the value of countdown to 1.
    # 3. After the countdown, print "Liftoff!"

# 1. Creating a variable countdown and initializing it to 10
print("")
print("Let the countdown begin!")
countdown = 10

# 2. Using a while loop to print a countdown from the value of countdown to 1
while countdown > 0:
    print(countdown) # This will print the countdown from 10 to 1
    countdown -= 1 # This will decrement the countdown by 1 each time the loop runs

# 3. After the countdown, print "Liftoff!"
print("Liftoff!") # This will print "Liftoff!"



# IV. Obtaining User Input

# Task: User Input and Conditional Statements
    # Write a code that takes the user's age as input. If the age is less than 18, print "You are a minor." If the
    # age is between 18 and 65 (inclusive), print "You are an adult." If the age is greater than 65, print "You are
    # a senior citizen."

# Taking the user's age as input
users_age = input("Please enter your age: ")
users_age = int(users_age)  # Converting the input to an integer
# Using conditional statements to check the user's age
if users_age < 18:
    print("You are a minor.")
elif (users_age >= 18 and users_age <= 65):
    print("You are an adult.")
elif users_age > 65:
    print("You are a senior citizen.") 

# Task: Temperature Converter
    # Modify the temperature converter from last’s week lab class to also take a user input. The user should be able to enter a value in degrees Celsius and your converter should convert this to Fahrenheit and Kelvin.
    # As an extra task, (if you are finished before the class is over or want to practice a bit more Python) you
    # should allow the user of the program to enter what temperature they want to convert (C, K or F) and then
    # print out the conversions. Use conditionals for this. 

# Last week temperature converter task
    # The user stores the Celsius value as a number in a variable called celsius_input
    # - The Celsius value then gets converted to Fahrenheit and stored in a variable called degree_f
    # - The Celsius value then gets converted to Kelvin and stored in a variable called degree_k
    # (Note: Use the internet to find out the formulas on how to convert C to K and F and implement that using Python operators
    # - Generate and print an output that follows the following format:
    
choice = input("Do you to convert temperature from Celsius, Fahrenheit or Kelvin? (Y/N)").upper()
while choice == "Y":
    
    # Allow the user to select the temperature they want to convert
    user_temp_choice = input("Please enter the temperature you want to convert (C, K or F): ").upper()

    # Taking the user's input for the temperature
    if user_temp_choice == "C":
        celcius_input = float(input("Please enter the temperature in Celsius: "))
        # Converting Celsius to Fahrenheit
        degree_f = (celcius_input * 9/5) + 32
        # Converting Celsius to Kelvin
        degree_k = celcius_input + 273.15
        # Printing the output
        print(f"{celcius_input} degrees Celsius is equal to {degree_f} degrees Fahrenheit and {degree_k} Kelvin.")
        # Asking the user if they want to convert another temperature
        choice = input("Do you to convert temperature from Celsius, Fahrenheit or Kelvin? (Y/N)").upper()
        if choice == "N":
            print("Thank you for using the temperature converter. Goodbye!")
            break
    elif user_temp_choice == "F":
        fahrenheit_input = float(input("Please enter the temperature in Fahrenheit: "))
        # Converting Fahrenheit to Celsius
        degree_c = (fahrenheit_input - 32) * 5/9
        # Converting Fahrenheit to Kelvin
        degree_k = degree_c + 273.15
        # Printing the output
        print(f"{fahrenheit_input} degrees Fahrenheit is equal to {degree_c} degrees Celsius and {degree_k} Kelvin.")
        # Asking the user if they want to convert another temperature
        choice = input("Do you to convert temperature from Celsius, Fahrenheit or Kelvin? (Y/N)").upper()
        if choice == "N":
            print("Thank you for using the temperature converter. Goodbye!")
            break
    elif user_temp_choice == "K":
        kelvin_input = float(input("Please enter the temperature in Kelvin: "))
        # Converting Kelvin to Celsius
        degree_c = kelvin_input - 273.15
        # Converting Kelvin to Fahrenheit
        degree_f = (degree_c * 9/5) + 32
        # Printing the output
        print(f"{kelvin_input} Kelvin is equal to {degree_c} degrees Celsius and {degree_f} degrees Fahrenheit.")
        # Asking the user if they want to convert another temperature
        choice = input("Do you to convert temperature from Celsius, Fahrenheit or Kelvin? (Y/N)").upper()
        if choice == "N":
            print("Thank you for using the temperature converter. Goodbye!")
            break
    else: 
        print("Invalid input. Please enter C, F or K.")
