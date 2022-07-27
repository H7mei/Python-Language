# latihan percabangan kalkulator

# percobaan latihan kalkulator sederhana

print(5*"====","Kalkulator 0.1","="*20)

a = int(input("Angka Pertama : "))
xyz = str(input("   (x,+,-,/)  : "))
b = int(input("Angka Kedua   : "))

if xyz== "x": 
    tz = (a * b)
    print (f"""
    {a:,}
    {b:,}
    --x
    {tz:,}""")
if xyz== "+":
    tz = (a + b)
    print (f"""
    {a:,}
    {b:,}
    --+
    {tz:,}""")
if xyz== "-":
    tz = (a - b)
    print (f"""
    {a:,}
    {b:,}
    -- -
    {tz:,}""")
if xyz== "/":
    tz = (a / b)
    print (f"""
    {a:,}
    {b:,}
    -- :
    {tz:,}""")

else :
    print("\n""coba lagi ? ")

