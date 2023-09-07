# for i in range(10):
#     print(f"i is now {i}")

# i = 0
# while i < 10:
#     print(f"i is now {i}")
#     i +=1

# available_exit = ""

# chosen_exit = ""
# while chosen_exit not in available_exit:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break

# else:
#     print("aren't you glad you got out of there!")



"""Modify the program below to use a while loop to allow as 
many guesses as necessary. 

The program should let the player know whether to guess higher
or lower, and should print a message when the guess is correct.
a correct guess will terminate the program.

As an optional extra, allow the player to quit by entering 
0 (zero) for their """

# import random

# higest = 10
# answer = random.randint(1, higest)

# print(f"Please guess a number between 1 and {higest}")
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input)
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it the first time")


'''solution below:'''

import random

higest = 10
answer = random.randint(1, higest)

print(f"Please guess a number between 1 and {higest}: ")
guess = 0  # initialize to any number outside of the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:  # guess must be bigger than number
        print("Please guess lower")
    else:
        print("Well done, you guessed it")