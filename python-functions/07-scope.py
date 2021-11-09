def message(date):
    content = "Something inside the function"


message("November 09, 2021")

# print(date)  # Error: name 'date' is not defined
# print(content)  # Error: name 'content' is not defined

print('\n')

dog_name = 'Nou'


def animal_name():
    global dog_name  # This is a global variable. Do not use it.
    dog_name = "Georgie"


animal_name()

print(dog_name)
