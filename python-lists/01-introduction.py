print("Simple list")
names = ["John", "Bob", "Mary", "Sue", "Sally", "Joe"]
print(names)

print("\nList of lists")
likes = [['tv', 'gamming'], ["pizza", "pasta"]]
print(likes)

print("\nList of identical values")
animal = ["spider"] * 5
print(animal)

print('\nList merging/concatenation')
animals = ["spider", "bear", "lion"]
cities = ["London", "Paris", "Berlin"]
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
boolean = [True, False]
mixed_data = animals + cities + even_numbers + odd_numbers + boolean
print(mixed_data)
