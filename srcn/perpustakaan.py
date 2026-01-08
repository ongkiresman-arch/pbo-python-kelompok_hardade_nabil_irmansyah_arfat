from buku import Buku

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        for b in self.daftar_buku:
            print(b.kode, b.judul, b.status)
