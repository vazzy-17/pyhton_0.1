# dasar oop (class,__init__,self)
# fokus representasi objek nyata seperti pemain dan musuh

class Karakter:
    def __init__(self,nama,hp):
        self.nama = nama
        self.hp = hp
    def serang(self,target,damage):
        target.hp -= damage

# latihan
# buat class Player dan musuh dengan method tampil_status(),diserang(damage)