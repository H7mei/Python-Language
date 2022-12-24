# Python list is using zero indexing.
rumah=[["kamar1",20000],["kamar2",30000],["kamar3",40000]]

print(type(rumah))

# indexing -1 dari belakang
print(rumah[-1])

# Subsetting list
print(rumah[0][1])

# list slicing [start : end] inclusive | exclusive
print(rumah[1:2])

# siplfy list sclinging
print(rumah[1:])
print(rumah[:1])

# manipulating list
kantor=['kantor1','10000','kantor2','20000','kantor3','30000']

# replace value
kantor[0:2]=['rumah','40000']

# Adding list
kantor.append(['kantor4', '40000'])
kantor + ['kantor5', '40000']

# remove list
del(kantor[0:4])

# list function
y = list(kantor)

print(y)