daftar_akurasi = [0.85, 0.90, 0.75]
daftar_akurasi[0] = 0.99
daftar_akurasi.append(0.92)

input_user = "0.88"
akurasi_baru = float(input_user) #Konversi input ke float untuk menseragamkan data kedalam list agar mudah di ola
daftar_akurasi.append(akurasi_baru)

print(daftar_akurasi)