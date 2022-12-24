# operasi logika atau bolean
# tipe not,or,and,xor

#conton not(tidak)
print('=======NOt')
a = True
c = not a
print('a is not',c)

#contoh dari or
print('=======OR')
a = True
b = True
c = a or b
print(a,' or',b,' =',c)
a = True
b = False
c = a or b
print(a,' or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,' =',c)
a = False
b = False
c = a or b
print(a,'or',b,'=',c)

#contoh dari AND
print('=======AND')
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

#contoh dari xor
print('=======XOR')
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

