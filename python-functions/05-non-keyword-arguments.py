def num(*numbers):
    return numbers


print(num(1, 2, 3, 4, 5))

print('\n')


def subtract(*nums):
    number = 100
    for num in nums:
        number -= num
    return number


print(subtract(1, 2, 3, 4, 5))
