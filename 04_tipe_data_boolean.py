#Aturan penulisan tipe data boolean diawali dengan huruf kapital
tipe_data_boolean_true = True
tipe_data_boolean_false = False

#operator perbandingan menghasilkan tipe data boolean
lebih_besar = 10 > 5  # True
lebih_besar_sama_dengan = 10 >= 10  # True
lebih_kecil = 10 < 5  # False
lebih_kecil_sama_dengan = 10 <= 10  # True
sama_dengan = 10 == 10  # True
tidak_sama_dengan = 10 != 5  # True

#gerbang logika menghasilkan tipe data boolean
dan_operator = True and False  # False
atau_operator = True or False  # True
bukan_operator = not True  # False

print ("Tipe data dari {tipe_data_boolean_true} adalah ", type(tipe_data_boolean_true))
print ("Tipe data dari {tipe_data_boolean_false} adalah ", type(tipe_data_boolean_false))
print ("Tipe data dari {lebih_besar} adalah ", type(lebih_besar))
print ("Tipe data dari {lebih_kecil} adalah ", type(lebih_kecil))
print ("Tipe data dari {sama_dengan} adalah ", type(sama_dengan))
print ("Tipe data dari {tidak_sama_dengan} adalah ", type(tidak_sama_dengan))
print ("Tipe data dari {dan_operator} adalah ", type(dan_operator))
print ("Tipe data dari {atau_operator} adalah ", type(atau_operator))
print ("Tipe data dari {bukan_operator} adalah ", type(bukan_operator))

#fakta unik

tipe_int = 10
tipe_float = 10.0
print("Apakah tipe_data_integer sama dengan tipe_data_float? ", tipe_int == tipe_float)  # True karena nilai keduanya sama meskipun tipe berbeda