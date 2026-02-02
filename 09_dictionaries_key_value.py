"""Dictionry atau di sebut dict adalah tipe data mutable yang menyimpan pasangan key dan value, Key harus unik dan immutable (tidak bisa diubah), sedangkan value bisa berupa tipe data apapun dan bisa diubah.
Dictionary berguna ketika kita ingin menyimpan data yang memiliki hubungan key-value, seperti data pengguna dengan username sebagai key dan informasi pengguna sebagai value. gunakan kurung kurawal {} untuk membuat dictionary, dan pisahkan key dan value dengan tanda titik dua :."""

# Membuat dictionary : bagus jika datanya sedikit dan sudah tahu apa isinya minus jika datanya banyak dan dinamis sulit untuk di atur
data_hewan_kucing = {"Nama": "Kucing Persia", "Berkaki": 4, "Habitat": "Rumah"}
data_hewan_anjing = {"Nama": "Anjing Chihuahua", "Berkaki": 4, "Habitat": "Rumah"}
data_hewan_burung = {} # Membuat dictionary kosong yang bisa kita isi nanti

#Mengisi dictionary kosong
data_hewan_burung["Nama_Burung"] = "Burung Merpati" #Menambahkan key "Name_Burung" dengan value "Burung Merpati"
data_hewan_burung["Berkaki"] = 2 #Menambahkan key "Berkaki" dengan value 2
data_hewan_burung["Habitat"] = "Sarang" #Menambahkan key "Habitat" dengan value "Sarang"

#Mengubah value pada dictionary (key harus tetap sama kalau beda ya buat key baru)
data_hewan_burung["Nama_Burung"] = "Burung Flaminggo" #Mengubah value pada key nama burung menjadi Burung Flaminggo sementara key "Nama" tetap karena sudah ada di dictionary
data_hewan_kucing.update({"Nama": "Kucing Hutan", "Habitat": "Hutan"}) #Mengubah value pada key nama dan habitat kucing menjadi kucing hutan dengan fungsi update()

#Fakta unik : Assigmen langsung itu cepat dan spesifik, sedangkan update() itu lebih fleksibel karena bisa mengubah banyak key sekaligus namun sedikit lebih lambat

#Mengubah key pada dictionary kita harus membuat key baru dan menghapus key lama dengan del, namun bisa juga dengan cara pop() untuk menghapus key lama dan menambahkan key baru dalam satu baris
data_hewan_burung["Nama"] = data_hewan_burung.pop("Nama_Burung")  #Mengubah key "Nama_Burung" menjadi "Nama" dengan cara menghapus key lama dan menambahkan key baru
#Ada juga menggunakan sistem bulk namun akan kita bahas di materi lanjutan

#Menghapus dictionary atau isinya
#del data_hewan_burung #untuk menghapus seluruh dictionary
#data_hewan_burung.clear() #untuk menghapus isi dictionary tanpa menghapus dictionarynya
#data_hewan_burung.pop("Habitat") #untuk menghapus key "Habitat" dari dictionary bisa juga menggunakan del data_hewan_burung["Habitat"]

data_dict_hewan = data_hewan_kucing, data_hewan_anjing, data_hewan_burung
print("Hasil Data Hewan Berbagai Dictionary : ", data_dict_hewan)

"""Namun membuat satu demi satu dictionary bisa merepotkan, terutama jika kita memiliki banyak data. 
Oleh karena itu, kita bisa menggunakan list, Dictionary of Dictionaries untuk menyimpan beberapa dictionary sekaligus, 
menggunakan zip() jika memiliki data untuk di pasangkan, atau menggunakan fromkeys() untuk menetapkan nilai defauld pada sebuah keys. tentu setiap metode punya kelebihan dan kekurangan masing masing """

# Membuat list of dictionaries : Bagus jika datanya banyak dan memiliki banyak atribut yang sama minusnya agak ribet saat mengakses isinya karena banyak index bahkan keys yang harus di ingat karena ada yang sama
data_hewan_list = [
    {"Nama": "Kucing Persia", "Berkaki": 4, "Habitat": "Rumah"},
    {"Nama": "Anjing Chihuahua", "Berkaki": 4, "Habitat": "Rumah"},
]

""" Dengan mengguanakan list yang membungkus dictionary membuat kita bisa menggunakan fungsi list seperti 
append(), remove(), pop() dll untuk mengelola data hewan kita tapi bukan mengelola isi dictionarynya langsung."""

#Menambahkan dictionary baru ke dalam list
data_hewan_list.append({"Nama_Burung": "Burung Flaminggo", "Berkaki": 2, "Habitat": "Sarang"}) #Menambahkan dictionary baru ke dalam list
data_hewan_list.insert(0, {"Nama_Ikan": "Ikan Mas Koki", "Berkaki": 0, "Habitat": "Air"}) #Menambahkan dictionary baru di index ke 0

#Mengubah isi dictionary di dalam list
data_hewan_list[1].update({"Nama": "Kucing Hutan", "Habitat": "Hutan"}) #Mengubah value pada key nama dan habitat kucing menjadi kucing hutan dengan fungsi update() namun harus mengakses index listnya dulu
data_hewan_list[3]["Nama"] = data_hewan_list[3].pop("Nama_Burung")  #Mengubah key "Nama_Burung" menjadi "Nama" pada dictionary burung di dalam list
#Secara sederhanana list of dictionaries itu adalah list yang isinya dictionary, jadi append() itu untuk menambah atau menghapus dictionary dari listnya, sedangkan update() itu untuk mengubah isi dictionarynya

#Mengahapus dictionary dari list
data_hewan_list.pop(0)  #Menghapus dictionary pertama (index 0) ikan dari list, bisa menggunakan del jika tahu indexnya dan ingin menghapus lebih dari satu jangan lupa apa itu .pop() ambil, hapus, simpan nilai yang di pop ke variable lain jika di perlukan

data_dict_list_hewan = data_hewan_list
print("Hasil Data Hewan List of Dictionaries : ", data_dict_list_hewan)

# Membuat dictionary of dictionaries : Bagus jika datanya banyak dan ingin mengakses data berdasarkan key unik minusnya agak ribet saat menambahkan data baru karena harus memastikan key uniknya tidak sama
data_hewan_dict = {
    "kucing": {"Nama": "Kucing Persia", "Berkaki": 4, "Habitat": "Rumah"},
    "anjing": {"Nama": "Anjing Chihuahua", "Berkaki": 4, "Habitat": "Rumah"},
}

#Menambahkan dictionary baru ke dalam dictionary of dictionaries
data_hewan_dict["burung"] = {"Nama_Burung": "Burung Flaminggo", "Berkaki": 2, "Habitat": "Sarang"} #Menambahkan dictionary baru dengan key "burung"
data_hewan_dict.update({"ikan": {"Nama_Ikan": "Ikan Mas Koki", "Berkaki": 0, "Habitat": "Air"}, "beruang": {"Nama_Beruang": "Beruang Kutub", "Berkaki": 4, "Habitat": "Kutub"}}) #Menambahkan dictionary baru dengan key "ikan" dan "beruang" menggunakan fungsi update()

#Mengubah isi dictionary di dalam dictionary of dictionaries
data_hewan_dict["kucing"].update({"Nama": "Kucing Hutan", "Habitat": "Hutan"}) #Mengubah value pada key nama dan habitat kucing menjadi kucing hutan dengan fungsi update()
data_hewan_dict["burung"]["Nama"] = data_hewan_dict["burung"].pop("Nama_Burung") #Mengubah key "Nama_Burung" menjadi "Nama" pada dictionary burung di dalam dictionary of dictionaries

#Menghapus dictionary dari dictionary of dictionaries
del data_hewan_dict["ikan"]  #Menghapus dictionary dengan key "ikan" dari dictionary of dictionaries
data_hewan_dict["beruang"].pop("Habitat")  #Menghapus key "Habitat" dari dictionary beruang dari dictionary of dictionaries
data_hewan_dict.pop("beruang")  #Menghapus dictionary dengan key "beruang" dari dictionary of dictionaries

data_dict_of_dict_hewan = data_hewan_dict
print("Hasil Data Hewan Dictionary of Dictionaries : ", data_dict_of_dict_hewan)

#tips membuat dictionary dengan zip() : Bagus jika memiliki dua list yang ingin di pasangkan menjadi dictionary minusnya harus memastikan kedua list memiliki panjang yang sama
keys = ["Nama", "Berkaki", "Habitat"]
values_kucing = ["Kucing Persia", 4, "Rumah"]
data_defauld = ["Belum ada data"] #Gunakan ini jika ingin membuat dictionary dengan nilai defauld menggunakan fromkeys()

data_hewan_kucing_zip = dict(zip(keys, values_kucing)) #Membuat dictionary dengan menggabungkan dua list menggunakan zip()
print("Hasil Data Hewan Kucing dengan zip() : ", data_hewan_kucing_zip)

data_hewan_fromkeys = dict.fromkeys(keys, data_defauld) #Membuat dictionary dengan keys dari list keys dan nilai defauld dari data_defauld menggunakan fromkeys()
print("Hasil Data Hewan dengan fromkeys() : ", data_hewan_fromkeys)

#Merge dictionary : Bagus jika ingin menggabungkan dua dictionary minusnya harus memastikan tidak ada key yang sama jika ada yang sama maka value dari dictionary kedua akan menggantikan value dari dictionary pertama
data_hewan_lain = {"ular": {"Nama_Ular": "Ular Sanca", "Berkaki": 0, "Habitat": "Hutan"}, "katak": {"Nama_Katak": "Katak Pohon", "Berkaki": 4, "Habitat": "Air"}}
data_hewan_dict.update(data_hewan_lain) #Menggabungkan dua dictionary menggunakan update()
print("Hasil Merge Data Hewan Dictionary : ", data_hewan_dict)

"""Catatan Penting : gunakan .keys(), .values(), dan .items() untuk mengakses keys, values, dan pasangan key-value dari dictionary.
Gunakan perulangan for untuk mengiterasi dictionary."""

#Contoh Penggunaan .keys() hanya mengambil keys dari dictionary
keys_hewan = data_hewan_dict.keys()
print("Keys dari data_hewan_dict : ", keys_hewan)
#Contoh Penggunaan .values() hanya mengambil values dari dictionary
values_hewan = data_hewan_dict.values()
print("Values dari data_hewan_dict : ", values_hewan)
#Contoh Penggunaan .items() mengambil pasangan key-value dari dictionary
items_hewan = data_hewan_dict.items()
print("Items dari data_hewan_dict : ", items_hewan)