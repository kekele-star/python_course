
first_name = 'klenam'
last_name = 'marrison'
# different formate used in printing instead of using concatenation(+)
output = 'hello, {1} {0},'.format(first_name, last_name)
print(output)

# spaceout out the results in the terminal output
print()

x = 43
y = 0

print()
# Error handling
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
print()


print()

country = input('what province do you live in: ')
tax = 0 


if country.lower() == 'Ghana':
    province = input('what province or state do you live in?')
    if province in ('Accra', 'Ho', 'Kumasi'):
        tax = 0.05
    elif province == 'Kofidua':
        tax = 0.13
    else:
        tax = 0.15
else:
    print(tax)