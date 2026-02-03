akuarium = "ikan" # = artinya mengisikan nilai, isi akuarium dengan ikan (Perintah)

akuarium == "ikan"  # == artinya membandingkan nilai, apakah isi akuarium sama dengan "ikan"? (Pertanyaan)
akuarium != "ikan"  # != artinya membandingkan nilai, apakah isi akuarium tidak sama dengan "ikan"? (Pertanyaan)

usia_ikan_nemo = 2
usia_ikan_koi = 5

# > Lebih dari, < Kurang dari, >= Lebih dari atau sama dengan, <= Kurang dari atau sama dengan
siapa_yang_lebih_tua = usia_ikan_nemo < usia_ikan_koi  
siapa_yang_lebih_muda = usia_ikan_nemo > usia_ikan_koi  
apakah_nemo_lebih_muda_atau_sama_dengan_koi = usia_ikan_nemo <= usia_ikan_koi  
apakah_koi_lebih_tua_atau_sama_dengan_nemo = usia_ikan_koi >= usia_ikan_nemo  

""" (and) artinya DAN, membandingkan apakah usia ikan nemo dan koi lebih dari 1, Jika kedua kondisi benar maka hasilnya True, namun jika salah satu atau kedua kondisi salah maka hasilnya False"""
hasil_and_true = (usia_ikan_nemo > 1) and (usia_ikan_koi > 1) #True
hasil_and_false = (usia_ikan_nemo > 3) and (usia_ikan_koi > 1) #False

""" (or) artinya ATAU, membandingkan apakah usia ikan nemo atau koi lebih dari 3, Jika salah satu atau kedua kondisi benar maka hasilnya True, namun jika kedua kondisi salah maka hasilnya False"""
hasil_or_true = (usia_ikan_nemo > 3) or (usia_ikan_koi > 1) #True, karena usia kedua ikan lebih dari 1
hasil_or_false = (usia_ikan_nemo > 6) or (usia_ikan_koi > 6) #False, karena usia kedua ikan tidak ada yang lebih dari 6
hasil_or_true_one = (usia_ikan_nemo > 3) or (usia_ikan_koi > 3) #True, karena usia ikan koi lebih dari 3, meski usia ikan nemo tidak lebih dari 3

""" (not) artinya BUKAN, membalikkan nilai boolean dari kondisi yang di bandingkan jadi True = False dan sebaliknya"""
usia_ikan_nemo_sudah_tiga_tahun = True
usia_ikan_nemo_sudah_tiga_tahun = not usia_ikan_nemo_sudah_tiga_tahun #false karena di balik, lalu kenapa harus not jika bisa pakai !=, alasannya adalah karena not bukan membandingkan tapi mengecek menggunakan kata "Tidak" jadi dia bisa mengecek data kosong [] tidak seperti !=

#if, else, elf
if akuarium == "ikan":
    print ("Akuarium Berisi Ikan")
if akuarium == "sampah":
    print ("Akuarium Berisi Sampah")
"""Cara di atas bisa-bisa saja di jalankan namun boros sumber daya jika yang kita cari adalah satu atau sebuah kondisi pada 1 objek yang sama, selain boros jika semua kondisi tidak di penuhi hasilnya tidak ada, ini cocok jika kamu ingin > 1 kondisi tercapai maka akan menerima > 1 output, jadi jika kondisi yang kita cari cuma 1 pada 1 objek yang sama disarankan menggunakan if,elif,else"""

if akuarium == "kosong": #Jika akuarium kosong maka kode berhenti di sini dan melakukan print, namun jika kondisi ini tidak di penuhi maka lanjut ke elif
    print ("Akuarium Kosong")
elif akuarium == "ikan": #jika kondisi ini terpenuhi maka kode berhenti di sini, jika tidak maka kode lanjut ke else
    print ("Akuarium berisi ikan")
else : #Hanya akan di eksekusi jika kondisi if dan elif tidak terpenuhi, jadi kita akan tetap mendapatkan output meski hasilnya kosong
    print ("Tidak ada akuarium")
#Tips, selalu taruh kondisi yang paling kemungkinan True di If bukan elif, karena komputer sekarang cukup cerdas bahwa yang di inginkan oleh dev adalah True

#Nested if, atau kondisi di dalam kondisi
if akuarium == "ikan": #mengecek apakah di dalam akuarium ada ikan? jika iya(true) maka lanjut ke kondisi lagi di dalam if
    if usia_ikan_koi == 5 and usia_ikan_nemo == 2:
        print (f"Di Akuarium berisi ikan koi berusia {usia_ikan_koi} bulan, dan ikan nemo berusia {usia_ikan_nemo}")
    else :
        print ("Akuarium berisi ikan dengan usia yang tidak di ketahui")
elif akuarium == "kosong":
    print ("Akuarium Kosong")
else: #di elif maupun else bisa aja ada nested namun akan lebih bagus semua nested hanya di if atau elif sementara else jadi output default jika semua kondisi tidak tercapai
    print ("Tidak ada akuarium")
#Tips: jangan buat nested lebih dari 3 kedalam, karena akan sulit di baca

#Kekosongan
list_kosong = [] #Falsy atau di anggap salah jadi False
angka_kosong = 0 #Falsy atau di anggap salah jadi False
string_kosong = "" #Falsy atau di anggap salah jadi False
#Jadi kalau kita isi list, angka selain 0, ada sesuatu di dalam "" maka hasilnya akan Truthy atau di anggap benar