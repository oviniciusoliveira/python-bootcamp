numbers = [1, 2, 3]
number1, number2, number3 = numbers
print(number1)
print(number2)
print(number3)

print('\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number1, number2, *other_numbers = numbers
print(number1)
print(number2)
print(other_numbers)

print('\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_number, *other_number, last_number = numbers
print(first_number)
print(other_number)
print(last_number)

print('\n')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_number, second_number, * \
    other_numbers, antepenultimate_number, last_number = numbers
print(first_number)
print(second_number)
print(other_numbers)
print(antepenultimate_number)
print(last_number)
