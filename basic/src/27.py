# dictionary

pop = [30.55, 2.77, 39.21]
countries = ['China', 'India', 'United States']

# create a dictionary
world = {'China': 30.55, 'India': 2.77, 'United States': 39.21}
print(world['China'])

# keys have immutable objects
# world['China'] = 30.55

# add a new key-value pair
world['Sealand'] = 0.23
print('Sealand' in world)  # True (case sensitive)

# remove a key-value pair
del world['Sealand']
print('Sealand' in world)  # False

# update a key-value pair
world['India'] = 2.99
print(world['India'])

# List vs Dictionary
# List: mutable, ordered, indexed
# Dictionary: mutable, unordered, indexed
