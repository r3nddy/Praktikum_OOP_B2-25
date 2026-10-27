from .paket_hosting import PaketHosting


class VPSHosting(PaketHosting):
    """Subclass 2: paket Virtual Private Server dengan alokasi CPU core."""

    BIAYA_PER_CORE = 25000  # Biaya resource & lisensi per core

    def __init__(self, id_paket, nama, penyimpanan_gb, bandwidth_gb, harga,
                jumlah_core, sistem_operasi):
        # Inheritance: memanggil constructor superclass.
        super().__init__(id_paket, nama, penyimpanan_gb, bandwidth_gb, harga)
        # Atribut unik subclass.
        self.jumlah_core = jumlah_core
        self.sistem_operasi = sistem_operasi

    # Implementasi abstract method #1 dengan hitungan berbeda dari SharedHosting.
    def hitung_total_harga(self):
        # Override: tambah biaya core sebelum dikenakan pajak.
        biaya_core = self.jumlah_core * VPSHosting.BIAYA_PER_CORE
        subtotal = self.harga + biaya_core
        return subtotal * (1 + PaketHosting.tarif_pajak)

    # Implementasi abstract method #2.
    def deskripsi_layanan(self):
        return f"VPS {self.jumlah_core} Core ({self.sistem_operasi})"

    # Override: rincian khusus VPS.
    def tampilkan_info(self):
        biaya_core = self.jumlah_core * VPSHosting.BIAYA_PER_CORE
        print(f"\n{'-' * 42}")
        print(f"  PAKET HOSTING: {self._nama} (VPS)")
        print(f"{'-' * 42}")
        print(f"  ID           : {self._id_paket}")
        print(f"  Penyimpanan  : {PaketHosting.format_penyimpanan(self._penyimpanan_gb)}")
        print(f"  Bandwidth    : {PaketHosting.format_penyimpanan(self._bandwidth_gb)}")
        print(f"  CPU Core     : {self.jumlah_core} Core (+{PaketHosting.mata_uang} {biaya_core:,.0f})")
        print(f"  OS           : {self.sistem_operasi}")
        print(f"  Harga Dasar  : {PaketHosting.mata_uang} {self.harga:,.0f}/bulan")
        print(f"  Total        : {PaketHosting.mata_uang} {self.hitung_total_harga():,.0f}/bulan")
        print(f"{'-' * 42}")
