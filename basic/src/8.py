#operasi komparasi 
#hasil dari operasi komparasi ini boolean(true/false)

# contoh alatnya >,<,>=,<=,==,!=,is,is not

a = 12
b = 12

# fungsi lebih besar dari >
print('======Lebih besar dari (>)')
hasil = a > b
print(a,'>',b,'=',hasil)
#ini kurang dari walau pun beda 0,1

# fungsi lebih besar dari <
print('======Kurang dari (<)')
hasil = a < b
print(a,'<',b,'=',hasil)
#sama ama atas

# fungsi lebih besar sama dengan >=
print('======Lebih besar sama dengan (>=)')
hasil = a >= b
print(a,'>=',b,'=',hasil)
#ini baru fungsi yang mendukung sama dengan beda ama atas

# fungsi kurang dari sama dengan <=
print('======Kurang dari sama dengan (<=)')
hasil = a <= b
print(a,'<=',b,'=',hasil)
#sama ama lebih dari sama dengan

## fungsi sama dengan dengan ==
print('======Lebih besar sama dengan (==)')
hasil = a == b
print(a,'==',b,'=',hasil)
#ini apa bila garis nya satu beda lagi

# fungsi tidak sama dengan !=
print('======Lebih besar sama dengan (!=)')
hasil = a != b
print(a,'!=',b,'=',hasil)
# tidak sama dengan


# is, is not ini membandingkan object dengan 
# melalui memory nya sama apa tidak

# contoh is 
# ini sama aja kaa sama dengan tapi melihatnya dari memory
x = 31
y = 31
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

#contoh is not
# tidak sama dengan
x = 12
y = 12
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ',hasil)

# Latihan
a = int(input('bandingkan angka : '))
b = int(input('dengan angka : '))

print('nilai x = ',a,',id = ',hex(id(a)))
print('nilai y = ',b,',id = ',hex(id(b)))

hasil = a > b
print(a,'lebih besar',b,'=',hasil)

hasil = a < b
print(a,'kurang dari',b,'=',hasil)
hasil = a >= b
print(a,'lebih dari/sama dengan',b,'=',hasil)
hasil = a <= b
print(a,'kurang dari/sama dengan',b,'=',hasil)
hasil = a == b
print(a,'sama dengan',b,'=',hasil)
hasil = a != b
print(a,'tidak sama dengan',b,'=',hasil)

hasil = a is b
print(a,'is',b,'=',hasil)
hasil = a is not b
print(a,'is not',b,'=',hasil)
