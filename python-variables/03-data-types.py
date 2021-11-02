# Integer
age = 22
print(age)
print(type(age))

# Float
grade = 9.8
print(grade)
print(type(grade))

# Boolean
is_published, offline = True, False
print(is_published, offline)
print(type(is_published), type(offline))

# String
movie_name = 'Nobody'
print(movie_name)
print(type(movie_name))

# List (Ordered)
mixed = [1, 2, 3.2, 4, 5.4, True, 'Hello', ['a', 'b', 'c']]
print(mixed)
print(type(mixed))

# Dictionary (python 3.7 > ordered)
movie_details = {
    'name': 'Nobody',
    'year': 2019,
    'director': 'Me',
    'cast': ['a', 'b', 'c']
}
print(movie_details)
print(type(movie_details))

# Tuple (unchangeable and ordered)
mixed_tuple = (1, 2, 3.2, 4, 5.4, True, 'Hello', ['a', 'b', 'c'])
print(mixed_tuple)
print(type(mixed_tuple))

# Set (unordered, unchangeable, unindexed)
mixed_set = {1, 2, 3.2, 4, 5.4, "Python", 'Hello'}
print(mixed_set)
print(type(mixed_set))
