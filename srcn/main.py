from buku import Buku
from perpustakaan import Perpustakaan

perpus = Perpustakaan()

b1 = Buku("B001", "Python Dasar", "Guido")
perpus.tambah_buku(b1)

perpus.tampilkan_buku()
