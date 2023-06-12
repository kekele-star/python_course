# the list of binary numbers
for i in range(17):
    print(f"{i:>2} in binary is {i:>08b}")


print("="*100)

# the list of hex numbers
for i in range(17):
    print(f"{i:>2} in binary is {i:>02x}")


x = 0x20
y = 0x0a
print(x)
print(y)
print(x * y)


print()

# challenge quiz.
# When converting a decimal to binary, you look for the higest power 
# of 2 smaller than the number and put a 1 in that column. You then take the 
# remainder and repeat the process with the next highest powe - putting a 1
# if it goes into the remainder and a zero  #