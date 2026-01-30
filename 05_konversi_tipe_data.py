data_int = 10 #Data tipe integer
data_float = 10.9 #Data tipe float
data_string_int = "10" #Data tipe string yang berisi angka integer
data_string_float = "10.9" #Data tipe string yang berisi angka float
data_string = "Sepuluh" #Data tipe string yang berisi teks

#Konversi Tipe Data
int_ke_float = float(10)
float_ke_int = int(10.9) #akan dibulatkan ke bawah = 10
string_ke_int = int("10")
string_ke_float = float("10.9")
data_string_float_ke_int = int(float(data_string_float)) #mengubah string "10.9" ke float dulu baru ke int, hasilnya 10
#string_ke_int_salah = int("Sepuluh") #ini akan menimbulkan error karena teks "Sepuluh" tidak bisa diubah ke numerik secara langsung
#string_ke_float_salah = float("Sepuluh") #ini akan menimbulkan error karena teks "Sepuluh" tidak bisa diubah ke numerik secara langsung

#Tips : Jangan melakukan melakukan casting berkali kali pada data yang sama karena akan membuang resource komputer secara percuma, casting saja sekali dan hasilnya simpan di variable baru