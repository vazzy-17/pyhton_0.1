import random

# ===== class dasar ====
class Player:
    def __init__(self,nama):
        self.nama = nama.strip().capitalize()
        self.level = 1 
        self.hp = 100
        self.inventory = []

    def naik_level(self):
        self.level += 1
        print(f"{self.nama} naik level {self.level}!")

    def tampilkan_status(self):
        print(f"\=== status pemain ===")
        print(f"nama : {self.nama}")
        print(f"level : {self.level}")
        print(f"hp : {self.hp}")
        print(f"inventory: {','.join(self.inventory) if self.inventory else 'kosong'}")

    def tambah_item(self, item):
        self.inventory.append(item.strip().lower())
        print(f"{item} telah di tambahkan ke inventory")

#=== fungsi ===
def buat_musuh(n):
        nama_musuh = ["goblin","dragon","orc","slime","bandit","ghost"]
        return [
            {"nama":random.choice(nama_musuh),"hp": random.randint(50,100),"aktif":True}
            for _ in range(n)
        ]

def tampilkan_musuh(musuh_list):
        print("\n=== daftar musuh ===")
        for idx, musuh in enumerate(musuh_list):
            status = "aktif" if musuh["aktif"] else "KO"
            print(f"{idx+1}. {musuh['nama']} | HP: {musuh['hp']} | Status: {status}")

def serang_musuh(musuh_list,index,damage):
        try:
            musuh = musuh_list[index]
            if not musuh["aktif"]:
                print("musuh sudah ko")
                return
            musuh["hp"] -= damage
            print(f"{musuh['nama']} terkena {damage} damage")

            if musuh["hp"] <= 0:
                musuh["hp"] =0
                musuh["aktif"] = False
                print(f"{musuh['nama']} KO") 
        except IndexError:
            print("nomor musuh tidak falid")       

# === progam utama ===
def main():
    print("=== game manager sederhana ===")
    nama = input("masukan nama pemain : ")
    player = Player(nama)

    musuh_list = buat_musuh(3)

    while True:
        print("\n--- menu ---")
        print("1. tampilkan status pemain")
        print("2. tambahkan item")
        print("3. lihat daftar musuh")
        print("4. serang musuh")
        print("5. naikan level")
        print("6. filter musuh aktif")
        print("0. keluar")

        pilihan = input("pilih aksi :")

        if pilihan =="1":
            player.tampilkan_status()
        elif pilihan =="2":
            item = input("masuk nama item :")
            player.tambah_item(item)
        elif pilihan =="3":
            tampilkan_musuh(musuh_list)
        elif pilihan =="4":
            tampilkan_musuh(musuh_list)
            try:
                idx = int(input("pilih musuh no:")) -1
                dmg = int(input("jumlah damage: "))
                serang_musuh(musuh_list,idx,dmg)
            except ValueError:
                print("masukan angka yang valid")
        elif pilihan =="5":
            player.naik_level()
        elif pilihan =="6":
            aktif = list(filter(lambda m: m["aktif"],musuh_list))
            print(f"\n musuh aktif : {[m['nama']for m in aktif]}")
        elif pilihan =="0":
            print("keluar dari game")
            break
        else:
            print("pilihan tidak di kenali")

if __name__ == "__main__":
    main()