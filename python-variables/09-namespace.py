# The variable number is just  reference to the object 1001
number = 1001
print(id(number))
print(id(1001))

a1 = 2
print('a1: ', id(a1))
a2 = a1 + 1
print('a2: ', id(a2))
print('three: ', id(3))

b1 = 2
print('b1: ', id(b1))
print('Two: ', id(2))

# All bellow assignments to the 'something' variable is a valid code
something = 12
something = "Python"
something = ['a', 2, True]


def hello():
    print('Hello World')


something = hello
something()

print('\n*-----Functions-----*\n')


def outer():
    outer_number = 10
    print(id(outer_number))

    global_number = 55
    print('Global number = ', global_number)

    def inner():
        inner_number = 200
        print('Inner number = ', inner_number)
        inner_number = 'Belchior'
        print('Inner number = ', inner_number)

        outer_number = 500
        print(id(outer_number))
        print('Outer number = ', outer_number)

    inner()


global_number = 100

outer()
