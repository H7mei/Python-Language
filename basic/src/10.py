# membuat gabungan area dengan angka
# membuat gabungan rentang dari dua area

# +++++3-----10++++++
a = float(input("jangan masukin angka antara 3-10 : "))

kuurangdari = a < 3
lebihdari   = a > 10

antara = kuurangdari or lebihdari
print(antara)

# -----3++++++10------
a = float(input("masukin angka antara 3-10 : "))

kuurangdari = a > 3

lebihdari   = a < 10

antara = kuurangdari and lebihdari
print(antara)

#Latihan
print("------0+++++5-----8+++++11----")

x = float(input("Masukkan angka : "))
y = ((x > 0) and (x < 5))or((x > 8) and (x < 11))
print(y)

print("+++++++0-----5+++++8------11++++++")

a = float(input("masukin angka : "))
b = ((a < 0) or (a > 5)) and ((a < 8) or (a > 11))
print(b)

#done



 