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

# DAY FIVE
