"""Tuples Sederhannya adalah list yang sudah di cor menggunakan simbol ()
Tuples bersifat immutable artinya isinya tidak bisa diubah setelah dibuat."""

ini_tuple = (10, "Halo", 15.5, True) #Tuple bisa menyimpan berbagai tipe data sekaligus
ini_list = [10, "Halo", 15.5, True] #List bisa menyimpan berbagai tipe data sekaligus

#ini_tuple[1] = "World"  #Ini akan menghasilkan error karena tuple bersifat immutable
ini_list[1] = "World"  #Ini akan berhasil karena list bersifat mutable
print("Isi tuple: ", ini_tuple)
print("Isi list setelah diubah: ", ini_list)

"""Namun ada cara mengubah isi tuple dengan cara mengkonversi tuple ke list, mengubah isinya, lalu mengkonversi kembali ke tuple."""

# Mengubah isi tuple dengan cara konversi
temp_list = list(ini_tuple)  #Konversi tuple ke list
temp_list[1] = "World"  #Ubah isi list
ini_tuple = tuple(temp_list)  #Konversi kembali ke tuple
print("Isi tuple setelah diubah melalui konversi: ", ini_tuple)