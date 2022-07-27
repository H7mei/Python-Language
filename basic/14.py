# Operasi manipulasi string

# 1. menyambung string (concatenate)
a = "alex"
b = "bonex"
c = "maret"
# kalo mau tambahin spasi mengunakan kutipdua
abc = a +" "+ b +" "+ c
print(abc)

# 2. Menghitung panjang string
d = len(abc)
# mengunakan len
print("panjang huruf : "+abc+" = "+str(d))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string
# mengunakan in/not in
#========= (in) ada
e = "x"
status = e in abc
print(e + " ada di "+ abc + " = "+ str(status))
A = "a"
status = A in abc
print(A + " ada di "+ abc + " = "+ str(status))
#========= (not in) tidak ada
e = "x"
status = e not in abc
print(e + " ada di "+ abc + " = "+ str(status))
A = "a"
status = A not in abc
print(A + " ada di "+ abc + " = "+ str(status))

# mengulang string
# menggunakan kali '*'

print("hahaha"*2)
print(2*"hahaha")

# indexing menggunakan ([])
print ("index ke-0 : " + abc[0])
print ("index ke-9 : " + abc[9])
print ("index ke-[-1] : " + abc[-1])
print ("index ke-[-9] : " + abc[-9])
# titik dua artinya samapi
print ("index ke-[1:9] : " + abc[1:9])
print ("index ke-[9:15] : " + abc[9:15])

# item paling kecil
print("paling kecil : ", min(abc))
# item paling besar
print("paling besar : ", max(abc))

# ngitungnya dari jumlah binary nya
# ASCII code
n = ("b")
x = ord(n)
print("jumlah ASCII code dari",n,"adalah :",str(x))
# chr itu character
m = 121
print("jumlah ASCII code dari",m,"adalah :",chr(m))

# 4. operator dalam bentuk method
data = abc
c = ("a")
x = data.count(c)
print("jumlah huruf", c ,"pada", abc,"ada = ",x)

# bagian ini akan menjelaskan tentang bagaimana
# fungsi membesarkan dan mengecilan string

# membesarkan (<object>.upper)
a = "ahah"*4
print(a.upper())

# mengecilkan huruf
b = "HAHAA"
print(b.lower())

## contoh pengecekan lower case (tambahin is)
# ini mengecek dengan hasil bolean
a = "b"
c = b.islower()
print(b,"memiliki lowercase :",str(c))
d = b.isupper()
print(b,"memiliki uppercase :",str(d))

#lainnya
a = "Merdeka Atau Mati"
b = a.isalpha()
print("apakah semuanya huruf :",b)
b = a.isalnum()
print("apakah semuanya huruf dan angka :",b)
b = a.isdecimal()
print("apakah semuanya angka :",b)
b = a.isspace()
print("apakah semuanya spasi :",b)
b = a.istitle()
print("apakah semuanya dimualai kapital :",b)

#"Mengubah Kata yang huruf depannya lowercase jadi uppercase"
#Contoh :
text = 'kelas terbuka'.capitalize()
print(text)

# contoh
a = ("kolaaa kola kolaaa")
b = a.isupper() or a.islower() ^ a.isalpha() or a.isalnum()
c = str(a).capitalize()
print(b)

print(c)
## mengecek komponen startswith() endswith()
# output nya true or false
m = a.startswith(a)
print(a,"diawali kolaaa",str(m))
f = a.endswith("kolaaa")
print(a,"di akhiri kolaaa ",str(f))


## pengabungan komponen join() split()
# contoh menggabungakan
a = "aku","mau","makan"
b = " ".join(a) # menambahkan spasi
print(b)

a = 'aku90mau90mandi'
b = (a.split('90'))
b = " ".join(b)
print(b)

## alokasi karakter rjust(), ljust(), center()

# 1. rata kanan (.rjust())
a = "kanan".rjust(15,"=")
print("'",a,"'")

# 2. rata kiri (.ljust())
a = "kiri".ljust(15,"=")
print("'",a,"'")

# 3. tengah (.center)
a = "tengah".center(21,"=")
print("'",a,"'")

# kebalikanlikanya -> strip()
b = a.strip("=")
print(b)
# jadi ini menghilangkan
