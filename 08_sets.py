"""Sets berbeda dengan list  meski sama sama mutable atau tuple karena sets tidak berurutan dan tidak mengizinkan duplikasi elemen, serta menggunakan kurung kurawal {}.
Sets bersifat mutable artinya isinya bisa diubah setelah dibuat, namun elemen di dalam sets haruslah tipe data yang immutable seperti string, angka, atau tuple.

Sets berguna ketika kita ingin menyimpan koleksi unik dari elemen dan melakukan operasi matematika seperti union, intersection, difference dan symmetric difference."""

# Membuat sets
hewan_darat = {"Kucing", "Anjing", "Katak", "Buaya", "Harimau"}
hewan_air = {"Ikan", "Hiu", "Katak", "Buaya", "Cumi-cumi"}

"""Union: Menggabungkan dua sets tanpa duplikasi elemen."""
union_hewan_darat_dan_air = hewan_darat.union(hewan_air)
print("Semua daftar hewan darat dan air: ", union_hewan_darat_dan_air)

"""Intersection: Mendapatkan elemen yang ada di kedua sets."""
intersection_hewan_dua_alam = hewan_darat.intersection(hewan_air)
print("Hewan yang bisa hidup di darat dan air: ", intersection_hewan_dua_alam)

"""Difference: Mendapatkan elemen yang ada di sets pertama tapi tidak ada di sets kedua."""
difference_hewan_darat = hewan_darat.difference(hewan_air)
print("Hewan darat yang tidak bisa hidup di air: ", difference_hewan_darat)
difference_hewan_air = hewan_air.difference(hewan_darat)
print("Hewan air yang tidak bisa hidup di darat: ", difference_hewan_air)

"""Symmetric Difference: Mendapatkan elemen yang ada di salah satu sets tapi tidak di kedua sets."""
symmetric_difference_hewan = hewan_darat.symmetric_difference(hewan_air)
print("Hewan yang hanya ada di darat atau air tapi tidak keduanya: ", symmetric_difference_hewan)