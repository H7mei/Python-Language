# operator bitwise, operasi biner, binary
# operasi dengan perhitungan biner
# operasi masing masing bit

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print("\n==========OR=======")
print('nilai : ',a,' , binary :',format(a,'08b'))
print('nilai : ',b,' , binary :',format(b,'08b'))
print("--------------------(|)")
print('nilai : ',c,' , binary :',format(c,'08b'))

# Bitwise AND (&)
c = a & b
print("\n==========AND=======")
print('nilai : ',a,' , binary :',format(a,'08b'))
print('nilai : ',b,' , binary :',format(b,'08b'))
print("--------------------(&)")
print('nilai : ',c,' , binary :',format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print("\n==========XOR=======")
print('nilai : ',a,' , binary :',format(a,'08b'))
print('nilai : ',b,' , binary :',format(b,'08b'))
print("--------------------(^)")
print('nilai : ',c,' , binary :',format(c,'08b'))

# Bitwise OR (~)
c = ~a
print("\n==========NOT=======")
print('nilai : ',a,' , binary :',format(a,'08b'))
print('----------------- (~)')
print('nilai : ',c,' , binary :',format(c,'08b'))
#mirorring

print('------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' , binary :',format(e^d,'08b'))

#shifting
#untuk menggerser angaka binary

# shift right (>>)
c = a >> 1
print('\n==============>>=======')
print('nilai : ',a,' , binary :',format(a,'08b'))
print('---------------- (>>)')
print('nilai : ',c,' , binary :',format(c,'08b'))

# shift right (<<)
c = a << 1
print('\n==============<<=======')
print('nilai : ',a,' , binary :',format(a,'08b'))
print('---------------- (<<)')
print('nilai : ',c,' , binary :',format(c,'08b'))

#menggeser angka binary
