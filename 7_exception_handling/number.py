def main():
    # Get an integer from the user using the get_int function.
    x = get_int("What's x? ")
    # Print the value of x.
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            # Attempt to convert user input to an integer.
            return int(input(prompt))
        except ValueError:
            # Inform the user if the input is not a valid integer.
            # print("x is not an integer")
            pass
        else:
            # If the input is a valid integer, return it.
            return x

# Call the main function to start the program.
main()
