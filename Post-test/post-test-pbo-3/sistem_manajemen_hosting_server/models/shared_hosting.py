from .paket_hosting import PaketHosting


class SharedHosting(PaketHosting):
    """Subclass 1: paket hosting bersama satu server."""

    def __init__(self, id_paket, nama, penyimpanan_gb, bandwidth_gb, harga, maks_domain):
        # Inheritance: memanggil constructor superclass.
        super().__init__(id_paket, nama, penyimpanan_gb, bandwidth_gb, harga)
        # Atribut unik subclass.
        self.maks_domain = maks_domain

    # Implementasi abstract method #1.
    def hitung_total_harga(self):
        # Shared hosting hanya dikenakan pajak tanpa biaya tambahan.
        return self.harga * (1 + PaketHosting.tarif_pajak)

    # Implementasi abstract method #2.
    def deskripsi_layanan(self):
        return f"Shared Hosting (maks {self.maks_domain} domain)"

    # Override: menambah baris khusus Shared Hosting setelah info dasar.
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"  Tipe         : Shared Hosting")
        print(f"  Maks Domain  : {self.maks_domain} domain")
        print(f"  Total        : {PaketHosting.mata_uang} {self.hitung_total_harga():,.0f}/bulan")
        print(f"{'-' * 42}")
