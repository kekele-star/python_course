# A function is simply a 'chunk' of code that you can use
# over and over again, rather than writing it out multiple time.

# Functions enable programmers to break down or decompose a problem
# into smaller chuns, each of which performs a particular task.

# Funcitons make your code more readable and easier to maintain
# Always add comments to explain the purpose of your functions
# Functions must be declared before the line of code where the function is called.

from datetime import datetime
# print the current time
def print_time():
    print('task completed')
    print(datetime.now())
    print()

print_time()

for x in range(0,10):
    print(x)
print_time()

print()
 # here's another example wehre the code looks different but we are doing the same logic
 # over and over
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_inital = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_inital + last_name_initial)
