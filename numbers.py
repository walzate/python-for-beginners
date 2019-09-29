first_number = input('Enter the first number: \n')
second_number = input('Enter the second number: \n')

print(first_number)
print(second_number)

total = first_number + second_number
print(f'Total in text: {total}')

# It is necessary to perform the data type conversion, because the input
# function always return a text
total = float(first_number) + float(second_number)
print(f'Total in numbers: {total}')
