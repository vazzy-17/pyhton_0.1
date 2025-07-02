# oop dasar untuk game
# fokus buat class sederhana: player,musuh dll

class player:
    def __init__(self,nama,level):
        self.nama=nama
        self.level = level

    def naik_level(self):
        self.level +=1

pl = player("raka",1)
pl.naik_level()
print(pl.level)

# latihan
# buat class enemy dengan atribut nama,hp
# tambahkan method diserang(damage)