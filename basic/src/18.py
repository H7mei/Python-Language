# IF dan Else Statment

# if (jika)

# cara pertama
# 1. program if inline
print("=======program if inline=====")
a = "merdeka"
if a=="merdeka" :print("kamu bisa")
print(f"terima kasi {a}")
# ini satu baris

# if kedua 
# 2. program if indentation
print("======program if indentation=====")
b = "kar"
if b=="kara":
    print("kamu menang") # jeda yang di depan itu yang dinamakan identation
    print("kamu pasti bisa")
    print("its not the end")
print(f"Terimakasi {b}")
# ini yang banyak di gunakan programer

# 3. Else Statment
# Else = jika tidak
print("=======Else Statment======")
c = "naution"
if c=="nasution": # jika menang
    print(f"kamu menang lomba ini {c}")
    print("ambil hadiah di administrasi")
else: # jika tidak
    print("Terima kasih telah berpartisipasi")
    print("jangan menyerah")
print("===-=-=-=-=-====")
print("stay asome")

# ELIF = else if statment

# elif = untuk cabang lain 

a = str(input("Masukkan nama : "))

if a =="bomer": #kondisi satu
     print("home horse")

     print("SAVE")
elif a =="kabum": #kondisi true 1
    print("kara kara")

    print("back")
elif a =="kura": #kondis true 2
    print("memory")

    print("juara")
else:           #kondisi false
    print("hv nice day")

print("you reach the end")