campuran_list = [10, "Halo", 15.5, True] #List bisa menyimpan berbagai tipe data sekaligus
"""List adalah tipe data yang bisa menyimpan banyak nilai dalam satu variable, dan setiap nilai di dalam list bisa diakses menggunakan index, dimana index pertama adalah 0, index kedua adalah 1, dan seterusnya. List juga bersifat mutable artinya isinya bisa diubah setelah dibuat."""

latihan_list = [1,2,3,4,5, "apel", "jeruk", "mangga", 10.5, 20.5, True, False]

#operasi dasar pada list
latihan_list.append("pisang")  #menambahkan nilai di akhir list
print("Hasil append pisang : ", latihan_list)
latihan_list.insert(2, "anggur")  #menambahkan nilai di index ke 2
print("Hasil insert anggur di index 2 : ", latihan_list)
latihan_list.remove("jeruk")  #menghapus nilai "jeruk" dari list
print("Hasil remove jeruk : ", latihan_list)
latihan_list.pop()  #menghapus nilai terakhir dari list, ingat pop itu sistem ambil, hapus, simpan nilai yang di pop ke variable lain jika di perlukan
print("Hasil pop() : ", latihan_list)
latihan_list[0] = 10  #mengambil dan mengubah nilai di index ke 0 menjadi 10
print("Hasil ubah index 0 menjadi 10 : ", latihan_list)
latihan_list.sort(key=str)  #mengurutkan list, gunakan key=str untuk menghindari error saat ada tipe data campuran
print("Hasil sort() : ", latihan_list)
latihan_list.reverse()  #membalik urutan list
print("Hasil reverse() : ", latihan_list)
latihan_list.extend(campuran_list)  #menggabungkan dua list
print("Hasil extend dengan campuran_list : ", latihan_list)
latihan_list.clear()  #menghapus semua isi list
print("Hasil clear() : ", latihan_list)

"""Catatan Penting :
1. List bersifat mutable, artinya isinya bisa diubah setelah dibuat.
2. List bisa menyimpan berbagai tipe data sekaligus.
3. Gunakan fungsi bawaan python seperti append(), insert(), remove(), pop(), sort(), reverse(), extend(), clear() untuk operasi pada list.
4. Saat mengurutkan list dengan tipe data campuran, gunakan parameter key=str pada fungsi sort() untuk menghindari error.
5. Index pada list dimulai dari 0.
6. List bisa diakses menggunakan index, misal: list[0] untuk mengakses nilai pertama.
Fakta Unik : ada fitur for, in, dan not in yang akan di pelajari di materi lanjutan"""