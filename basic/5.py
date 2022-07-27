#tentang input data dari user

#contoh pertama
data = input("who are you : ")

print("welcome",data,"have fun","type data",type(data))
#contoh di atas ini type data pasti sring
#input apapun

#contoh kedua int, float
#kalo contoh kedua di casting dulu ke dalan float/int
#input yang di massukan anggka int
angka = int(input("TTL :"))
print("kaar",angka,"have fun",type(angka))
#input yang di masukkan anggak float .
floatt = float(input("Bulan:"))
print("kaar",floatt,"have fun",type(floatt))

#jadi seperti itu dia harus di casting agar data dapat
#terbaca dengan type int/float

""""kalu boleaan berbeda lagi dia harus dicasting ke
int agar terdeteksi False"""

#ex BOLEAN
boleean = bool(int(input("0/1 =")))
#jawaban nya 0 untuk false 1 untuk true

print("by",boleean,type(boleean))

# Latihan
#string
data    = input("nama :")
data2   = input("domisili : ")

print("salam kenal",data,"dari",data2)

#float/int
angka   = int(input("Tahun berapa kamu lahir : "))
age     = 2021 - angka
print("kamu berumur",age,"tahun")

print("===SELAMAT DATANG===")
#bolean

boolean = bool(int(input("ingin melanjutkan 0/1 ?")))

print("selamat",boolean,("kamu lolos"))




