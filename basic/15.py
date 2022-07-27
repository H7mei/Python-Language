# format string

# contohnya
# sting
name ="kara"
a = f"hello {name}" # seperti ini dengan bantuan {}
print(a)

# boolean
a = True
b = f"status {a}"
print(b)

# angka
a = 21
b = f"number {a}"
print(b)

# bilangan bulat
a = 90
b =f"baris ke {a:d}" # tambahan (:d) untuk khusus bilangan bulat
print(b)

# bilangan dengan ordo ribuan
a = 120000
b = f"harga mobil : ${a:,}" #(:,)
print(b)

# bilangan desimal
a = 12.72361358125835218
b = f"desimal = {a:.1f}" # (:.1f) = satu angkka di belakang kom
print(b)

# menampilkan leading zero
a = 213.90
b = f"nambahin nol = {a:010.2f}" # menambahkan no di depan
# {<object>:0<banyak nol>.<jumlah angka di belakang koma>f}
print(b)

# menampilkan tanda + atau minus -
# minus
a = -10
p = +10
hasil = f"minus = {a:+d}"
hasil2 = f"pluss = {p:+.2f}"
print(hasil)
print(hasil2)

# memformat persen
presentase = 0.045
a = f"persen = {presentase:.2%}" 
# ngambilnya dari depan 2 angka
print(a)

# melakukan operasi aritmatik adalam {}
cabe = 12000
bawang = 6000
toge = 4000

harga = f"total harga belanja : Rp.{cabe+bawang+toge:,}"

print(harga)

# format angka lain (binary, octal, hexadesimal)

angka = 225
a = f"binary : {bin(angka)}"
b = f"octal : {oct(angka)}"
c = f"hexadesimal : {hex(angka)}"

print(a,b,c)

# one
