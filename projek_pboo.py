# =========================
# Class Buku
# =========================
class Buku:
    def __init__(self, kode, judul, penulis):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        self.status = "tersedia"


# =========================
# Class Perpustakaan
# =========================
class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"\nBuku '{buku.judul}' berhasil ditambahkan")

    def tampilkan_buku(self):
        print("\nDaftar Buku:")
        if not self.daftar_buku:
            print("Belum ada buku")
        else:
            for b in self.daftar_buku:
                print(b.kode, "-", b.judul, "-", b.penulis, "-", b.status)


# =========================
# Program Utama
# =========================
perpus = Perpustakaan()

while True:
    print("\n=== MENU PERPUSTAKAAN ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Buku")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        kode = input("Kode Buku: ")
        judul = input("Judul Buku: ")
        penulis = input("Penulis: ")
        buku = Buku(kode, judul, penulis)
        perpus.tambah_buku(buku)

    elif pilihan == "2":
        perpus.tampilkan_buku()

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
