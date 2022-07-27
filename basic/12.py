# operator assingnment merupakan operator penyingkatan

# contoh

a = 5
print('nilai a = ',a)
#contoh assingnment biasa
a += 1 #di tambah
print('nilai a + 1 = ',a)
a -= 1 #di kurang
print('nilai a - 1 = ',a)
a *= 9 #di kali
print('nilai a * 9 = ',a)
a /= 1 #di bagi
print('nilai a / 1 = ',a)
# modulus dan floour division
a %= 1 #operasi modulus
print('nilai a % 1 = ',a)
a //= 1 #operasi flour divisor
print('nilai a // 1 = ',a)
# pangkat/ eksponen
a **= 10 #di pangkatkan
print('nilai a ** 10 = ',a)

# operasi bitwise
# OR(|)
b = True
print("\nnilai b =",b)
b |= False
print("nilai c |= False, nilai b menjadi",b)
b = False
print("nilai b =",b)
b |= False
print("nilai c |= True, nilai b menjadi",b)

# AND(&)
b = True
print("\nnilai b =",b)
b &= False
print("nilai c &= False, nilai b menjadi",b)
b = True
print("nilai b =",b)
b &= True
print("nilai c &= True, nilai b menjadi",b)

# XOR(^)
b = True
print("\nnilai b =",b)
b ^= False
print("nilai c ^= False, nilai b menjadi",b)
b = True
print("nilai b =",b)
b ^= True
print("nilai c ^= True, nilai b menjadi",b)

# shifting
c  = 0b00000100
print("\nnilai d =", format(c,'08b'))
c >>= 2
print(c)
print(format(c,'08b'))
c <<= 5
print(format(c,'08b'))
print(c)
