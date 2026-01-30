daftar_usia = (10, 20, 30, 40, 50)
daftar_usia_list = list(daftar_usia)
daftar_usia_list[0] = 15
daftar_usia = tuple(daftar_usia_list)

print(daftar_usia)
print(type(daftar_usia))