class PaketHosting:
    mata_uang = "IDR"
    tarif_pajak = 0.11       # 11 %
    total_paket = 0

    def __init__(self, id_paket, nama, penyimpanan_gb, bandwidth_gb, harga):
        self.id_paket = id_paket               
        self.nama = nama                        
        self.penyimpanan_gb = penyimpanan_gb    
        self.bandwidth_gb = bandwidth_gb      
        self.__harga = 0.0                     
        self.harga = harga                  

        PaketHosting.total_paket += 1

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai):
        if not isinstance(nilai, (int, float)):
            raise ValueError("Harga harus berupa angka!")
        if nilai < 0:
            raise ValueError("Harga tidak boleh negatif!")
        self.__harga = float(nilai)

    def tampilkan_info(self):
        print(f"\n{'-' * 42}")
        print(f"  PAKET HOSTING: {self.nama}")
        print(f"{'-' * 42}")
        print(f"  ID           : {self.id_paket}")
        print(f"  Penyimpanan  : {PaketHosting.format_penyimpanan(self.penyimpanan_gb)}")
        print(f"  Bandwidth    : {PaketHosting.format_penyimpanan(self.bandwidth_gb)}")
        print(f"  Harga Dasar  : {PaketHosting.mata_uang} {self.harga:,.0f}/bulan")
        print(f"  Pajak ({PaketHosting.tarif_pajak * 100:.0f}%)  : {PaketHosting.mata_uang} {self.harga * PaketHosting.tarif_pajak:,.0f}")
        print(f"  Total Harga  : {PaketHosting.mata_uang} {self.hitung_total_harga():,.0f}/bulan")
        print(f"{'-' * 42}")

    def hitung_total_harga(self):
        return self.__harga * (1 + PaketHosting.tarif_pajak)

    @classmethod
    def dari_dict(cls, data):
        return cls(
            id_paket=data["id_paket"],
            nama=data["nama"],
            penyimpanan_gb=data["penyimpanan_gb"],
            bandwidth_gb=data["bandwidth_gb"],
            harga=data["harga"],
        )

    @classmethod
    def ubah_tarif_pajak(cls, tarif_baru):
        if not isinstance(tarif_baru, (int, float)) or tarif_baru < 0:
            print("[!] Tarif pajak tidak valid! Harus angka >= 0.")
            return
        cls.tarif_pajak = float(tarif_baru)
        print(f"[OK] Tarif pajak diperbarui menjadi {cls.tarif_pajak * 100:.0f}%.")

    @staticmethod
    def format_penyimpanan(gb):
        if gb >= 1024:
            return f"{gb / 1024:.0f} TB"
        return f"{gb} GB"

    def __str__(self):
        return f"[{self.id_paket}] {self.nama} - {PaketHosting.mata_uang} {self.harga:,.0f}/bulan"
