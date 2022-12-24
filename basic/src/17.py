# latihan mengunaka date and time

import datetime as dt

print("""
===========Masukkan Tanggal Lahir=====
""")

tanggal = int(input("tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun \t\t:"))
print(tanggal,bulan,tahun)
print()
xyz = dt.date(tahun,bulan,tanggal)
print(xyz)
print(f"Tanggal Lahir anda adalah : {xyz}")
print(f"pada hari \t\t  : {xyz:%A}\n")
today = dt.date.today()          #hari ini
umur = today - xyz               # pengurangan input dengan parameter hari in
print("kamu hidup selama",umur)
tahun = umur.days // 365         # hari di bagi ke 365
bulan = (umur.days % 365) //30
print("kamu berumur",tahun,"tahun",bulan,"bulan")

# sederhana untuk menghitung umur
