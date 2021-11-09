def working_condition(device, status="working"):
    return f"The {device} is {status}"


print(working_condition("printer"))
print(working_condition("coffe machine", "out of order"))

print('\n')

# Optional params should be at the end of the function definition


def subtract(x, z, y=15):
    return x - y - z


print(subtract(10, 5))
print(subtract(10, 5, 10))
