# fungsi(def,parameter,return)
# fokus membuat program lebih modular, reusable dan terstruktur

def serang(player,musuh):
    damage = 10
    musuh['hp'] -= damage
    print(f"{player} menyerang {musuh['nama']} sebesar {damage} HP.")
    return musuh

# latihan
# buat fungsi heal(pemain,jumlah)
# buat fungsi pilih_aksi() yang mengembalikan pilihan pemain