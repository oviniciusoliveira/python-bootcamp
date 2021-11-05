def arithmetic_operations(x, y):
    print(f'{x} * {y} = {x * y}')
    print(f'{x} / {y} = {x / y}')
    print(f'{x} + {y} = {x + y}')
    print(f'{x} - {y} = {x - y}')


arithmetic_operations(10, 5)
arithmetic_operations(10, 10)

print("\n")


def legal_age(name, age, allowed_age):
    if age >= allowed_age:
        print(f'{name} is allowed to go to the movie')
    else:
        print(f'{name} is not allowed to go to the movie')


legal_age('Abra', 21, 18)
legal_age('Tiburcio', 11, 18)
