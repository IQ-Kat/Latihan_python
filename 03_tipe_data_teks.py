"""semua yang di bungkus dengan " " atau ' ' adalah tipe data teks (string) di python dan tidak bisa di gunakan untuk operasi matematika secara langsung"""
tipe_data_teks = "Teks, Angka 1234 dan simbol !@#$%" 
print("tipe_data_teks : ", tipe_data_teks, ", type : ", type(tipe_data_teks))

# contoh operasi matematika yang salah
string_tambah_string = "10" + "5"  # ini adalah operasi penggabungan teks (concatenate) bukan penjumlahan angka
print("hasil_jadi_teks (penggabungan teks) : ", string_tambah_string, ", type : ", type(string_tambah_string))
numerik_tambah_numerik = 10 + 5  # ini adalah operasi penjumlahan angka
print("numerik_tambah_numerik (penjumlahan angka) : ", numerik_tambah_numerik, ", type : ", type(numerik_tambah_numerik))
#string_tambah_numerik = "10" + 5  (ini akan menimbulkan error karena tidak bisa menjumlahkan teks dengan angka secara langsung)

"""Untuk Mengubah Tipe Data Teks (string) ke Numerik bisa menggunakan fungsi bawaan python seperti int(), float()"""
string_ke_integer = int("10")  # mengubah teks "10" menjadi integer
string_ke_float = float("10.5")  # mengubah teks "10.5" menjadi float
string_ke_numerik_salah = int("10.5")  # ini akan menimbulkan error karena tidak bisa mengubah teks "10.5" langsung ke integer karena 10.5 adalah float bukan integer
string_teks_ke_numerik_salah = int("sepuluh")  # ini akan menimbulkan error karena teks "sepuluh" tidak bisa diubah ke numerik secara langsung

"""Teks atau Strings itu immutable artinya tidak bisa di ubah setelah di buat, jadi untuk mengubahnya harus membuat teks baru"""
teks_asli = "Halo Dunia"
teks_baru = "Halo Semua"
pengucapan = 2

print(teks_asli + teks_baru)  # menggabungkan dua teks, ini sebenarnanya di belakang layar membuat teks baru
print(f"{pengucapan} {teks_asli}")  # menggunakan f-string untuk format teks dengan variabel
#print(teks_asli + pengucapan)  #ini akan menimbulkan error karena tidak bisa menggabungkan teks dengan numerik secara langsung, kecuali mengubah numerik ke teks dulu menggunakan str()