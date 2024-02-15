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
# # print(f'Pssst, the solution is {chosen_word}.')
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

# DAY EIGHT - Digital Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(user_message):
    user_message_index = []
    user_message_index = text
    text_replace = []
    for num in enumerate(user_message_index):

        text_replace.append()
    print(text_replace)

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(user_message=text)