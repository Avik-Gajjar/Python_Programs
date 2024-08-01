# DAY ONE - BAND NAME GENERATOR

# print("Welcome to Band Name Generator")
# city_name = input("What's the name of the city you grew up in?\n")
# pet_name = input("What's the name of your pet?\n")
# print("Your Band name could be: " + city_name + " " + pet_name)

# DAY TWO - TIP CALCULATOR [PEMDAS ** exponential // flow - +=]

# print("Welcome to the tip calculator")
# total_bill = float(input("What was the total bill? "))
# tip_perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# members = int(input("How many people to split the bill? "))
#
# tip_conv = (tip_perc / total_bill) * 100
#
# gross_bill = total_bill + tip_conv
#
# final_pay = gross_bill / members
#
# total_pay = round(final_pay, 2)
#
# print(f"Each person have to pay {total_pay}")

# DAY THREE - Pizza Order

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25
#
# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
#
# if extra_cheese == "Y":
#   bill += 1
#
# print(f"Your final bill is: ${bill}.")

# DAY THREE - Love Calculator

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# combined_name = name1 + name2
# lower_name = combined_name.lower()
#
# t = lower_name.count("t")
# r = lower_name.count("r")
# u = lower_name.count("u")
# e = lower_name.count("e")
# first_digit = t + r + u + e
#
# l = lower_name.count("l")
# o = lower_name.count("o")
# v = lower_name.count("v")
# e = lower_name.count("e")
# second_digit = l + o + v + e
#
# love_score = int(str(first_digit) + str(second_digit))
#
# if (love_score < 10) or (love_score > 90):
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) and (love_score <=50):
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")

# DAY THREE - Treasure Island

# print("Welcome to Treasure Island!")
# print("Your Mission is to find the treasure.")
#
# user_input_1 = input("You are at a cross road. Where do you want to go? Type left or right.\n").lower()
# if user_input_1 == "right":
#   print("Fall into a hole. Game Over.")
# elif user_input_1 == "left":
#   user_input_2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
#   if user_input_2 == "swim":
#     print("Attacked by Crocodile. Game Over.")
#   elif user_input_2 == "wait":
#     user_input_3 = input("You arrive at  the island unharmed. There is house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
#     if user_input_3 == "red":
#       print("Burned by Fire. Game Over.")
#     elif user_input_3 == "yellow":
#       print("You found the Treasure! YOU WIN!!")
#     elif user_input_3 == "blue":
#       print("Eaten by beast. Game Over.")
#     else:
#       print("You can't choose anything else. Game Over.")
#   else:
#     print("Sorry, Wrong Input.")
# else:
#   print("Sorry, Wrong Input.")

# DAY FOUR - Treasure Map

# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "️⬜️"]
# line3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input()  # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
#
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")
#
# DAY FOUR - Rock, Paper, Scissors
#
# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors] # Images list
#
# user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
# if user_input >= 3 or user_input < 0: # Checking invalid input
#     print("Incorrect Input. Try Again.")
# else:
#     print(game_images[user_input])
#
#     comp_input = random.randint(0, 2)
#     print("Computer Chose:")
#     print(game_images[comp_input])
#
#     if user_input == 0 and comp_input == 2: # User winning conditions
#         print("You Win!")
#     elif comp_input == 0 and user_input == 2: # Computer winning conditions
#         print("You Lose!")
#     elif comp_input > user_input: # Computer winning conditions
#         print("You Lose!")
#     elif user_input > comp_input: # User winning conditions
#         print("You Win!")
#     elif comp_input == user_input: # Draw Conditions
#         print("It's a Draw")

# DAY FIVE - Average height - without len and sum function

# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# sum_of_height = 0
# for height_1 in student_heights:
#     sum_of_height += height_1
# print(f"total height = {sum_of_height}")
#
# number_of_student = 0
# for students in student_heights:
#     number_of_student += 1
# print(f"number of students = {number_of_student}")
#
# avg_height = round(sum_of_height / number_of_student)
# print(f"average height = {avg_height}")

# DAY FIVE - Max Score
# Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# # Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#     if score >= highest_score:
#       highest_score = score
# print(f"The highest score in the class is: {highest_score}")

# DAY FIVE - FizzBuzz Program

# for fizzbuzz in range(1, 101):
#   if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#     print("FizzBuzz")
#   elif fizzbuzz % 3 == 0:
#     print("Fizz")
#   elif fizzbuzz % 5 == 0:
#     print("Buzz")
#   else:
#     print(fizzbuzz)

# DAY FIVE - PyPASSWORD GENERATOR
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# user_password_list = []  # empty list to add random letter, numbers and symbols
#
# for x in range(0, nr_letters):
#     user_password_list += random.choice(letters)  # random choice will pick up random item from list
#
# for y in range(0, nr_symbols):
#     user_password_list += random.choice(numbers)
#
# for z in range(0, nr_numbers):
#     user_password_list += random.choice(symbols)
#
# random.shuffle(user_password_list)  # will shuffle the input from different list
#
# final_user_password = ""
# for char in user_password_list:
#     final_user_password += char
#
# print(final_user_password)

# end="" will show multiple for loop output on same line
# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# DAY SIX - Robot Hurdle 1, 2, 3, and 4(hard)
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while at_goal() == False:
#     if front_is_clear():
#         move()
#     if wall_in_front():
#         jump()

# DAY SIX - Escaping the Maze Need to try the endless loop scenario after Day 15
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while at_goal() == False:
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# DAY SEVEN - Hangman Game

# import random
# import hangman_word_list
# import hangman_art
#
# chosen_word = random.choice(hangman_word_list.word_list)
# word_length = len(chosen_word)
# end_of_user_input = False
# lives = 6
# guess_letter = " "
#
# print(hangman_art.logo)
#
# display = []
# for _ in range(word_length):
#     display += "_"
# # print(display)
#
# # Testing code
# # print(f"Pssst, the solution is {chosen_word}.")
#
# while not end_of_user_input:
#     guess = input("Guess a letter to begin the game: ").lower()
#
#     if guess in display:
#         print(f"You already guessed this letter: {guess}")
#
#     for position in range(word_length):  # Code from Udemy
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     if guess not in chosen_word:
#         print("Chosen letter is not in the Word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             end_of_user_input = True
#             print("You Lose.")
#
#     print(display)
#
#     if "_" not in display:
#         end_of_user_input = True
#         print("Yay! You Won!")
#
#     print(hangman_art.stages[lives])

# MY ACTUAL CODE LOGIC
# for letter in chosen_word:
#     display = "_"
#     if letter == guess:
#         print(guess + " ", end="")  # Prints vertical instead of horizontal
#     else:
#         print(display + " ", end="")

# DAY EIGHT - PAINT AREA CALCULATOR

# Write your code below this line 👇
# import math
#
#
# def paint_calc(height, width, cover):
#   no_of_cans = (height * width) / 5
#   print(f"You'll need {math.ceil(no_of_cans)} cans of paint.") # math/ceil() rounds up the decimal to next whole number


# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# DAY EIGHT - PRIME NUMBER

# Write your code below this line 👇
# def prime_checker(number):
#     is_prime = True
#     for num in range(2, number):
#         if number % num == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
# n = int(input())  # Check this number
# prime_checker(number=n)

# DAY EIGHT - Digital Caesar Cipher - TOUGHEST ONE AND SOLVED W/O HELP

# def encrypt(user_message, no_of_shift):
#     cipher_message = ""
#
#     for counter in text:
#         letter_index = alphabet.index(counter) + shift
#
#         cipher_message += alphabet[letter_index]
#
#     print(f"The encoded message is {cipher_message}")
#
#
# def decrypt(user_message, no_of_shift):
#     decipher_message = ""
#
#     for counter in text:
#         letter_index = alphabet.index(counter) - shift
#
#         decipher_message += alphabet[letter_index]
#
#     print(f"The decoded message is {decipher_message}")
#
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e',
#             'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z',]
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#
# if direction == "encode":
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     encrypt(text, shift)
# elif direction == "decode":
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     decrypt(text, shift)
# else:
#     print("Please enter 'encode' or 'decode' to proceed.")

# My First actual logic
# count = 0
# letter_counter = 0
# while count < len(text):
#   first_letter = text[letter_counter]
#   letter_index = alphabet.index(first_letter) + shift
#   letter_counter += 1
#   count += 1
#   cipher_message += alphabet[letter_index]

# DAY NINE - STUDENT GRADES
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
#
# student_grades = {}  # Empty Dictionary
#
# for items in student_scores:
#   if student_scores[items] >= 91 and student_scores[items] <= 100:
#     student_grades[items] = "Outstanding"
#   elif student_scores[items] >= 81 and student_scores[items] <= 90:
#     student_grades[items] = "Exceeds Expectations"
#   elif student_scores[items] >= 71 and student_scores[items] <= 80:
#     student_grades[items] = "Acceptable"
#   else:
#     student_grades[items] = "Fail"
#
# print(student_grades)

# DAY NINE - Dictionary and List Function
# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string
#
# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
#
# # TODO: Write the function that will allow new countries
# # to be added to the travel_log.
# def add_new_country(country_name, no_of_visits, cities):
#     new_visit = {}
#     new_visit["country"] = country_name
#     new_visit["visits"] = no_of_visits
#     new_visit["cities"] = cities
#     travel_log.append(new_visit)
#
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# DAY NINE - Secret Auction Program

# from auction_art import logo
#
# print(logo)
#
# print("Welcome to the Bidding Auction. Let's begin!")
#
# user_bid_data = {}
# while_loop = False
#
#
# def winning_bidder(bid):
#     highest_bid = 0
#     winner = ""
#     for bidder in bid:
#        a_bid_amt = bid[bidder]
#        if a_bid_amt > highest_bid:
#            highest_bid = a_bid_amt
#            winner = bidder
#     print(f"The winner is {winner} with highest bid of ${highest_bid}")
#
#
# while not while_loop:
#     user_name = input("Please enter your name:\n")
#     user_bid = int(input("Please enter your bid:\n$"))
#
#     user_bid_data[user_name] = user_bid
#
#     loop_decision = input("Is there anymore Bids? Enter 'Yes' or 'No'. :\n").lower()
#     if loop_decision == "no":
#         while_loop = True
#         winning_bidder(user_bid_data)

# DAY TEN - Functions with Output

# def format_name(f_name, l_name):
#    full_name = f_name + " " + l_name
#    return full_name.title()
#
#
# print(format_name("EVaaN", "gaJJar"))
#
# # DAY TEN - Days in a Month
#
#
# def is_leap(year):
#    """This function will check that the given year is a Leap year or not."""
#    if year % 4 == 0:
#       if year % 100 == 0:
#          if year % 400 == 0:
#             return True
#          else:
#             return False
#       else:
#          return True
#    else:
#       return False
#
#
# def days_in_month(a_year, a_month):
#    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#    a_year = is_leap(a_year)
#    if a_year: # this way it is by default True
#       return 29
#    else:
#       return month_days[a_month - 1]
#
#
# year = int(input())  # Enter a year
# month = int(input())  # Enter a month
# days = days_in_month(year, month)
# print(days)

# DAY TEN - Calculator Program

# from Calculator_art import logo
#
#
# def add(n1, n2):
#    return n1 + n2
#
#
# def subtract(n1, n2):
#    return n1 - n2
#
#
# def multiply(n1, n2):
#    return n1 * n2
#
#
# def divide(n1, n2):
#    return n1 / n2
#
#
# operations = {
#    "+": add,
#    "-": subtract,
#    "*": multiply,
#    "/": divide
# }
#
#
# def calculator():
#    print(logo)
#
#    num1 = float(input("+"))
#    for symbol in operations:
#       print(symbol)
#    should_continue = True
#
#    while should_continue:
#       operation_symbol = input("Pick an operation: ")
#       num2 = float(input("What's the next number?: "))
#       calculation_function = operations[operation_symbol]
#       answer = calculation_function(num1, num2)
#       print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#       if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#          num1 = answer
#       else:
#          should_continue = False
#          calculator()
#
#
# calculator()

# DAY TWELVE Number guessing game
# import random
#
#
# def guessing_game():
#     print("Welcome to the Number Guessing Game!")
#     print("Choose a difficulty level:")
#     print("1. Easy (10 chances)")
#     print("2. Hard (5 chances)")
#
#     difficulty = input("Enter difficulty (1 for Easy, 2 for Hard): ").strip()
#
#     if difficulty == '1':
#         max_attempts = 10
#         print("You have chosen Easy difficulty. You have 10 chances to guess the number.")
#     elif difficulty == '2':
#         max_attempts = 5
#         print("You have chosen Hard difficulty. You have 5 chances to guess the number.")
#     else:
#         print("Invalid choice. Please restart the game and choose a valid difficulty level.")
#         return
#
#     number_to_guess = random.randint(1, 100)
#     attempts = 0
#
#     while attempts<max_attempts:
#         try:
#             guess = int(input(f"Attempt {attempts + 1}: Guess a number between 1 and 100: "))
#             attempts += 1
#
#             if guess<number_to_guess:
#                 print("Too low!")
#             elif guess>number_to_guess:
#                 print("Too high!")
#             else:
#                 print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
#                 break
#         except ValueError:
#             print("Please enter a valid number.")
#
#     if attempts == max_attempts and guess != number_to_guess:
#         print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
#
#
# if __name__ == "__main__":
#     guessing_game()

#DAY FOURTEEN - HIGHER LOWER Game
# import random
#
# from replit import clear
#
# from art import logo, vs
# from game_data import data
#
#
# def get_random_account():
#     """Get data from random account"""
#     return random.choice(data)
#
#
# def format_data(account):
#     """Format account into printable format: name, description and country"""
#     name = account["name"]
#     description = account["description"]
#     country = account["country"]
#     # print(f'{name}: {account["follower_count"]}')
#     return f"{name}, a {description}, from {country}"
#
#
# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess
#     and returns True if they got it right.
#     Or False if they got it wrong."""
#     if a_followers>b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
#
#
# def game():
#     print(logo)
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
#
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {format_data(account_a)}.")
#         print(vs)
#         print(f"Against B: {format_data(account_b)}.")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         a_follower_count = account_a["follower_count"]
#         b_follower_count = account_b["follower_count"]
#         is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#         clear()
#         print(logo)
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
#
#
# game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers?

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''

# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.
