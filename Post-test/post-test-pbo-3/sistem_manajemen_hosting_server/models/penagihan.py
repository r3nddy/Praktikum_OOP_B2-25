# SOLID: DIP (Dependency Inversion Principle) - LayananTagihan tidak bergantung
# pada SharedHosting/VPSHosting secara langsung, melainkan pada abstraksi
# PaketHosting. Kelas paket baru bisa ditambahkan tanpa mengubah kelas ini.
class LayananTagihan:
    """Layanan yang menghitung total tagihan dari kumpulan paket hosting."""

    def __init__(self, nama_layanan="Layanan Tagihan Hosting"):
        self.nama_layanan = nama_layanan

    def total(self, daftar_paket):
        return sum(paket.hitung_total_harga() for paket in daftar_paket)

    def cetak_tagihan(self, nama_klien, daftar_paket):
        print(f"\n{'_' * 48}")
        for paket in daftar_paket:
            print(f"  {paket}")
        print(f"{'_' * 48}")
        print(
            f"  {self.nama_layanan} - {nama_klien}\n"
            f"  TOTAL TAGIHAN: Rp {self.total(daftar_paket):,.0f}"
        )
        print(f"{'_' * 48}")
