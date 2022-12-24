# packages

# Each Script = module
# Specify function, metotds, type
# thousan of packages are available
# module in python called pip

# pip install <package>
# after install pakage, you can use it with import <package>

from numpy import array

fam = ['liz', 1.90, 'jane', 1.68, 'joe', 1.71, 'jim', 1.89]

fam_ext = fam + ['me', 1.79]

print(str(len(fam_ext)) + " elements in fam_ext")

np_fam = array(fam_ext)
