# fungsi lambda &map,filter
# fokus fungsi singkat dan efisien untuk memproses data

kuadrat = lambda x: x ** 2
print(kuadrat(5)) #25

data = [1,2,3,4]
hasil = list(map(lambda x: x*10,data))
genap = list(filter(lambda x: x % 2 == 0, data))

# latihan 
# gunakan filter untuk memisahkan skor tinggi dari list
# ubah semua nama item menjadi huruf kapital