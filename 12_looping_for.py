"""Looping adalah sebuah perulangan untuk logika yang sama"""

usia_mahasiswa_baru = [19, 21, 20] #List Usia Mahasiswa Baru
lama_kuliah = 4

for usia in usia_mahasiswa_baru: #Logikanya ambil data 1 per 1 dari "usia_mahasiswa_baru" dan simpan di variable sementara bernama "usia"
    usia_lulus = usia + lama_kuliah #buat data baru bernama "usia_lulus" dengan isi dengan data sementara "usia" + "lama_kuliah"
    print(usia_lulus) #print akan di jalankan sebanyak for(kecuali print tidak menjorok ke dalam) dimana for di jalankan sebanyak data rujukan dalam hal ini "usia_mahasiswa_baru"

"""Namun hasil dari di atas berupa data copotan list bukan list(jika menggunakan list), namun jika ingin hasil akhir tetap list bisa gunakan Comprehension pada listnya(compresion tidak terbatas hanya pada list)"""
#List Comprehension
list_usia_lulus = [usia + lama_kuliah for usia in usia_mahasiswa_baru]
print (list_usia_lulus)

#range format isinya adalah range (nilai awal, nilai akhir, lompatan/opsional)
#range langsung di for
usia_mahasiswa_teknik = [20, 21, 22, 23]

for usia_acak in range(1, 10): #buat usia acak dengan value dari 1 hingga 9
    hasil = usia_acak + 5
    print (hasil)

#jika data cukup kompleks bisa gunakan
daftar_mahasiswa = ["Ikbal", "Alan", "Yunus"]
daftar_index = range(1, len(daftar_mahasiswa) + 1) #ini membuat index mulai dari 1 karena defauld 0, lalu +1 karena list akan berhenti 1 sebelum tujuan akhir
daftar_usia_mahasiswa = range(20, 25)

for no, nama_mahasiswa, usia_mahasiswa in zip(daftar_index, daftar_mahasiswa, daftar_usia_mahasiswa):
    print (f"{no} {nama_mahasiswa} berusia {usia_mahasiswa}")

#Tentu di atas jika kita tidak ingin membuat data bantuan seperti "daftar_index" tapi butuh index dan nama data kita bisa gunakan Enumerate ini juga cocok jika data banyak karena dia memberi index nanti saat di butuhkan
daftar_mahasiswa_teknik = ["alan", "ikbal", "yunus", "faujan"]

#kenapa harus ada variable "no" alasanya karena enumarate menghasilkan tuple (0, alan) sehingga harus di bongkar, dan 0 di isi ke "no", namun karena kita pakai start=1 maka index di mulai dari 1 bukan 0
for no , nama_mahasiswa_teknik in enumerate(daftar_mahasiswa_teknik, start=1):  
    print(f"{no} {nama_mahasiswa_teknik}")