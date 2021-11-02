# len()
address = 'Japan'
print(len(address))

# [] index
print(address[0])
print(address[1])
print(address[-1])

# [] slice
print(address[:3])
print(address[2:])
print(address[:])

# Concatenation
country = 'RUS'
city = 'Moscow'
full_address = city + ', ' + country
print(full_address)

# String formatting
print('{}, {}'.format(city, country))
print('{1}, {0}'.format(country, city))
print('{}, {}, {}'.format(city, country, 'Russia'))

# upper()
print(address.upper())

# lower()
print(country.lower())

# title()
print(full_address.title())

# strip()
job = '          Programmer        '
print(job)
print(job.strip())
print(job.lstrip())
print(job.rstrip())

# find()
print(address.find('p'))

# replace()
print(address.replace('n', 'o'))

# in operator
print('p' in address)
print('o' in address)

# not operator
print('a' not in address)
print('b' not in address)
