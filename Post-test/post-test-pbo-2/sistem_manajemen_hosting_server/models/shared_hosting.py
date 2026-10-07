from .paket_hosting import PaketHosting


class SharedHosting(PaketHosting):
    def __init__(self, id_paket, nama, penyimpanan_gb, bandwidth_gb, harga, maks_domain):
        super().__init__(id_paket, nama, penyimpanan_gb, bandwidth_gb, harga)
        self.maks_domain = maks_domain 

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"  Tipe Hosting : Shared Hosting")
        print(f"  Maks Domain  : {self.maks_domain} domain")
        print(f"{'-' * 42}")
