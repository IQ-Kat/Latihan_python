#Contoh data Immutable dan Mutable di Python
"""Data Immutable adalah data yang tidak bisa diubah setelah dibuat, jadi Identitas atau alamat memorinya berubah saat isinya diubah.
Contoh data immutable di Python adalah : int, float, string, dan tuple"""
Nama_Dev = "Ikbal" #String adalah data immutable
print("Sebelum diubah, Nama_Dev : ", Nama_Dev, " dengan id : ", id(Nama_Dev))
Nama_Dev = "Ikbal Katili" #Mengubah isi string akan membuat alamat memori baru
print("Setelah diubah, Nama_Dev : ", Nama_Dev, " dengan id : ", id(Nama_Dev))

"""Data Mutable adalah data yang bisa diubah setelah dibuat, jadi Identitas atau alamat memorinya tetap sama walaupun isinya diubah.
Contoh data mutable di Python adalah : list, dictionary, dan set"""
Data_Project = ["AI", "Web Development", "Mobile App"] #List adalah data mutable
print("Sebelum diubah, Data_Project : ", Data_Project, " dengan id : ", id(Data_Project))
Data_Project.append("Game Development") #Mengubah isi list tidak akan membuat alamat memori baru
print("Setelah diubah, Data_Project : ", Data_Project, " dengan id : ", id(Data_Project))