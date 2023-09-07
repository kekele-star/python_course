# strings: ordered, immutable, text representation
# strings cannot be changed or altered after it has been created
# two or more strings can be concatenated with a plus sign +


first_name = input("What is your name: ")
age = int(input("how old are you: "))
print(age)

if age >= 18:
    print("You are old enough to vote")
else:
    print("please come back in {} years".format(18 - age))

my_string = "Hello night studies"
print(my_string.find("n"))
print(my_string.replace("night studies", "world"))

# spliting a string into a list
my_list = my_string.split(" ")
print(my_list)


# converting a list back to a string
new_string = " ".join(my_list)
print(new_string)

print(' ')

# formating strings: %, .format(), f-Strings
# where %s is string %d is double %f is float
var = "Charity"
string1 = "the variable is %s" % var # this is the old formating style
print(string1)

string1 = "the new formating style is {}".format(var)
print(string1) 

var2 = 3.147869
var3 = 5
string2 = "the new formating style is {:.2f} and {}".format(var2, var3)
print(string2) 


# using the latest formating
string3 = f"the latest formating style is {var *2} and {var2}"
print(string3)


# using the + concatenation method
greetings = "Hello"
name = input("Please enter your name: ")
answer = f"{greetings} {name}"
print(answer)
# print(greetings + " " + name)


greeting = "hello"
tim_was_57 = "bruce"
result = f"{greeting} {tim_was_57}"
print(result)