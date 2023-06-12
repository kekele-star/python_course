# Write a small program to ask for a name and age.
# When both values have been entered, check if the person
# is the right age to go on an 18-39 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a polite message refusing them entry. 

name = input("What is your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Enjoy you holidays")
elif age < 18: 
    print("Soryy try again in {} years time".format(18- age))
else:    
    print("Sorry, our holidays are only for seriously cool people")