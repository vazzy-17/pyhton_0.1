# error handling (try/except)
# fokus membuat game lebih stabil saat ada kesalahan input/user

try:
    damage=int(input("masukan damage:"))
except ValueError:
    print("harus berupa angka!")

# latihan
# tangani input non-angka untuk damage dan pilihan menu
# tangani file tidak di temukan saat load_game()