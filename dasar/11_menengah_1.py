# handling eror ( try/except )
# fokus menangani input pengguna atau eror runtime

try:
    angka = int(input("masukan angka: "))
    print(100/angka)
except ValueError:
    print("bukan angka")
except ZeroDivisionError:
    print("tidak bisa di bagi 0")

# latihan
# buat program input angka terus menurs sampai valid
# tangani pembagian angka dengan validasi