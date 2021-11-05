def facebook(name, status):
    return f"{name} is {status}"


abra_status = facebook("Abra", "online")
tiburcio_status = facebook("Tiburcio", "offline")

print(abra_status)
print(tiburcio_status)

print('\n')


def divide(number1, number2):
    return number1 / number2


result = divide(21, 3)
print(result)

# Keyword arguments
result = divide(number2=21, number1=3)
print(result)
