from .paket_hosting import PaketHosting


class VPSHosting(PaketHosting):
    BIAYA_PER_CORE = 25000  # Biaya lisensi & resource per core

    def __init__(self, id_paket, nama, penyimpanan_gb, bandwidth_gb, harga, jumlah_core, sistem_operasi):
        super().__init__(id_paket, nama, penyimpanan_gb, bandwidth_gb, harga)
        self.jumlah_core = jumlah_core        
        self.sistem_operasi = sistem_operasi   

    def hitung_total_harga(self):
        # Method Overriding: tambah biaya core sebelum pajak
        biaya_core = self.jumlah_core * VPSHosting.BIAYA_PER_CORE
        subtotal = self.harga + biaya_core
        return subtotal * (1 + PaketHosting.tarif_pajak)

    def tampilkan_info(self):
        # Method Overriding
        biaya_core = self.jumlah_core * VPSHosting.BIAYA_PER_CORE
        subtotal = self.harga + biaya_core
        pajak = subtotal * PaketHosting.tarif_pajak

        print(f"\n{'-' * 42}")
        print(f"  PAKET HOSTING: {self._nama} (VPS)")
        print(f"{'-' * 42}")
        print(f"  ID           : {self._id_paket}")
        print(f"  Penyimpanan  : {PaketHosting.format_penyimpanan(self._penyimpanan_gb)}")
        print(f"  Bandwidth    : {PaketHosting.format_penyimpanan(self._bandwidth_gb)}")
        print(f"  CPU Core     : {self.jumlah_core} Core (+{PaketHosting.mata_uang} {biaya_core:,.0f})")
        print(f"  OS           : {self.sistem_operasi}")
        print(f"  Harga Dasar  : {PaketHosting.mata_uang} {self.harga:,.0f}/bulan")
        print(f"  Pajak ({PaketHosting.tarif_pajak * 100:.0f}%)  : {PaketHosting.mata_uang} {pajak:,.0f}")
        print(f"  Total Harga  : {PaketHosting.mata_uang} {self.hitung_total_harga():,.0f}/bulan")
        print(f"{'-' * 42}")
