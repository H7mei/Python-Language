#jadi casting merupakan cara mengubah satu
#tipe data ke tipe data yang lain nya
#tipe data = int, float, str, bool,

#menngetes perubahan yang terjadi antar tipe data

## INTERGER
print("====INTEGER====")
data_int = 10;
print("data = ", data_int, ",type =",type(data_int))
#perubahan terhadap
data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) #ini akan false apabilla nilai int = 0
print("data = ", data_float,"type =",type(data_float))
print("data = ", data_str,"type =", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 0;
print("data = ", data_float, ",type =",type(data_float))
#perubahan terhadap
data_int   = int(data_float) #akan di bulatkan ke bawah
data_str   = str(data_float)
data_bool  = bool(data_float) #ini akan false apabilla nilai float = 0
print("data = ", data_int,"type =",type(data_int))
print("data = ", data_str,"type =", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = True;
print("data = ", data_bool, ",type =",type(data_bool))
#perubahan terhadap
data_int    = int(data_bool) #kalo false = 0, kalo true = 1
data_str    = str(data_bool) #tetap true
data_float  = float(data_bool) #kalo false = 0.0, kalo true = 1.0
print("data = ", data_int,"type =",type(data_int))
print("data = ", data_str,"type =", type(data_str))
print("data = ", data_float, "type =", type(data_float))

## STRING
print("====STRING====")
data_str = ""
print("data = ", data_str, ",type =",type(data_str))
#perubahan terhadap

 #data_int   = int(data_str) #sting nya harus angka
 #data_float = float(data_str) #string nya harusangka
data_bool  = bool(data_str)  #kalo mau false string nya harus kosong
 #print("data = ", data_int,"type =",type(data_int))
 #print("data = ", data_float,"type =", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))

#berikut perubahan beruban 