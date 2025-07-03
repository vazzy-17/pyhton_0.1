# struktur game 2d (game loop & event)
# fokus simulasi game dengan loop utama

running = True
while running:
    aksi = input("aksi(serang/heal/keluar):")
    if aksi == "keluar":
        running = False
    else:
        print(f"aksi: {aksi}")

# latihan 
# tambahkan sistem hp:jika 0, game over
# tambahkan musuh dengan status dan response