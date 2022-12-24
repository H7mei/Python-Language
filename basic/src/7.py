# perhitungan suhu sederhana 

# konfensi celcius ke satuan lainnya
print("\nPROGRAM KONFENSI TEMPERATUR\n")
# input data suhu ke celcius

celcius = float(input('input dalam celcius : '))
print("suhu dalam celcius adalah ",celcius,"celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur,"reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ",fahrenheit,"fahrenheit")

#kelvin
kelvin = celcius + 273.15
print("suhu dalam kelvin adalah ",kelvin,"kelvin")

data = float(input("perubahan kelvin/varenheit : "))

lat = ((data - 32) * 5/9) + 273.15
#ini perubahan dari farenheit ke kelvin
lat2= ((data - 273.15)* 9/5) + 32
#ini perubahan kelvin ke varen heit

print("hasil nya : ",lat,"kelvin")
print("hasil nya : ",lat2, "farenheit")


