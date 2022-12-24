""""tipe data standar pada python ada 4 :
integer
float
string
boolean
"""

#tipe data pertama : Angka satuan
# Ga ada koma nya 
data_integer = 123
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#tipe kedua : angka dengan koma (float)
data_float = 1.3
print("data : ", data_float)
print("- bertipe : ", type(data_float))

#ketiga : kumpulan karakter (string)
data_string = "we can"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

#ke empat tipe data : biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## ada lagi tipe data khusus

# Bilangan kompleks
data_complex = complex(5,4)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

"""karna pthon dasarnya di buat dengan bahas C
jasi kita bisa menggunakannya"""

# tipe data dari bahasa C
# kita harus import dulu

from ctypes import c_double

data_c_double = c_double(90.0)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))

#ini dari bahaca C jadi kita dapat menggunakan nya
 