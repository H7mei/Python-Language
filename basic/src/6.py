# Aritmatika

a = 2
b = 4

# Operasi Penjumlahan +
hasil = a + b
print(a,'+',b,'=',hasil)

# Operasi Pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# Operasi Perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# Operasi Pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#operasi lain
# Operasi Eksponen **
# ini adalah hasil dari pangkat sebuah bilangan

# Operasi Eksponen **
hasil = a ** b
print(a,'**',b,'=',hasil)
#sama dengan 10 pangkat empat

# Operasi Modulus %
hasil = a % b
print(a,'%',b,'=',hasil)
# ini adalah sisa dari hasil pembagian

# Operasi Flour Division //
hasil = a // b
print(a,'//',b,'=',hasil)
#Flour division membulatkan pembagiann ke bawah

#prioritas Operasi bilangan

# 1. () kurungan
# 2. eksponen ** pangkat
# 3. perkalian dll *,/,%,//,
# 4. pertambahan +,-

#contoh

x = 1
y = 2
z = 3

hasil = x * x * z // y % z + y + x
print(x,'*',x,'*',z,'//',y,'%',z,'+',y,'+',x,'=',hasil)

# latihan

print('=================OPERASI BILANGAN=================')
print('=================MASUKKAN ANGKA MU=================')

a = int(input('  ANGKA PERTAMA     ='))
b = int(input("  ANGKA KEDUA       ="))

hasil = (a + b)
print('hasil dijumlahan     = ',hasil)

hasil = (a - b)
print('hasil dikurangan     = ',hasil)

hasil = (a * b)
print('hasil diperkalian    = ',hasil)

hasil = (a / b)
print('hasil dipembagian    = ',hasil)

hasil = (a ** b)
print('hasil dipangkatkan   = ',hasil)

hasil = (a % b)
print('hasil dari modulus   = ',hasil)

hasil = (a // b)
print('dari flour divisor   = ',hasil)



