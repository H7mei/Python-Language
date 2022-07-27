# penulisan data string

# 1. String standard
a = "Tere Liye"
b = 15
c = 2003
d = 32
ty = "standard".center(20,"=")
print(ty)
abcd = f"nama : {a} umur : {b} tahun : {c} sepatu : {d}"
print(abcd)
# ini biasa

# 2. multiple dengan enter
ty = "Multiple cara 1".center(20,"=")
print(ty)
abcd = f"nama : {a} \numur : {b} \ntahun : {c} \nsepatu : {d}"
print(abcd)

# 3. Multiple cara ke dua
ty = "Multiple cara 2".center(20,"=")
print(ty)
abcd = f"""nama   : {a}
umur   : {b}
Tahun  : {c}
sepatu : {d}"""

# mengatur lebar
ty = "Multiple mengatur lebar".center(20,"=")
print(ty)
abcd = f"""
nama   : {a:>5}
umur   : {b:>5}
Tahun  : {c:>5}
sepatu : {d:>5}
"""
# pake ini :>5
print(abcd)

