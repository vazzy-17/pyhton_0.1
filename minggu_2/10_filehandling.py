# file handling(open(),read(),write())
# fokus menyimpan data game ke file eksternal(save/load)

# simpan
with open("save.txt","w") as f:
    f.write(f"{player['nama']},{player['level']},{player['hp']}")

# baca
with open("save.txt","r") as f:
    data = f.read().split(',')
    print(data)

# latihan
# buat fungsi save_game(player) dan load_game()