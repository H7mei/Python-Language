a = "contoh sederhana string"
print(a)
print(type(a))
#memerupakan contoh string sederhana


# 1. cara membuat stinng

"""
    1. dengan menggunakan single quote '...'
    2. dengan mengunakan double qoute  "..."
""" 

#contoh
a = 'single quote'
print(a)
a = "double quote"
print(a)
# keduanya sama aja
# kalau mau tambahin kutip dalam kalimat
print("'kutipnya ada dua'")
# sebaliknya juga samaa

# 2. mengunakan tanda \'

#tanda koma dengan menambahkan (\')
print("ini hari jum\'at")
print("ini hari jum'at")

#blackslash (\\)
print("C:\\home\\file")
#slash nya dua

# tab (\t)
print("ini\tmengunakan tab")

# backspace (\b)
print("menjauh     \b  \b \b kan")

# newline/enter (\n)
"""
ada cara 1. \n 2. \r 3. \r\n
yang pertama di gunakan di unix seperti macbook/linux
yang kedua perangkat perangkat lama
yang ketiga di gunakan di windows
"""
print("baris pertama\nbaris kedua")

# 3. String literal atau raw

# mengunakan raw string 
print(r'C:\new folder')
# ini terbebas dari funsi tanda

# multiline literal string
print(r""" 
Nama : Axel
Jurusan : komputer
domisili : texas
website : www\capm
""")