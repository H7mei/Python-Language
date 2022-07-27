# build in function
fam = [1.72, 1.68, 1.71, 1.89]

# max return the highest value
print(max(fam))

# round return the nearest integer
print(round(fam[0]))

# min return the lowest value
print(min(fam))

# sum return the sum of all values
print(sum(fam))

# len return the length of the list
print(len(fam))

# pow return the power value of the string
print(pow(2,3))

# sorted return the sorted value of the string
print(sorted(fam))

# sorted descending return the sorted descending value of the string
print(sorted(fam, reverse=True))

# count return the count of the value
print(fam.count(1.72))

# index return the index of the value
print(fam.index(1.72))

# append add the value to the list
fam.append(1.72)

# reversed return the reversed value of the string
print(reversed(fam))

# reverse reverse the list
fam.reverse()

# print(help(sum)) # open the documentation

# Methods 
# Methods are functions that belong to a class.

# int return the integer value of the string
print(int('1'))

# str return the string value of the integer
print(str(1))

# bool return the boolean value of the string
print(bool(1))

# list return the list value of the string
print(list('abc'))

# tuple return the tuple value of the string
print(tuple('abc'))

# set return the set value of the string
print(set('abc'))

# type return type of the file
print(type(fam)) 

# list methods
fam=['liz', 1.72, 'jane', 1.68, 'joe', 1.71, 'jim', 1.89]

print(fam.index('jane')) # "call method of index() on fam"

print(fam.count('jane')) # "call method of count() on fam"

# str methods
sister = 'liz'
print(sister.capitalize()) # "call method of capitalize() on sister"
print(sister.replace('liz', 'jane')) # "call method of replace() on sister"

# Methods 
# Everything in Python is an object.
# Objects have methods. depending on the type of object, you can call different methods.

fam.append('me')
fam.append(1.79)
print(fam[-2:])



# Summary:
# 1. metots call function as an object

