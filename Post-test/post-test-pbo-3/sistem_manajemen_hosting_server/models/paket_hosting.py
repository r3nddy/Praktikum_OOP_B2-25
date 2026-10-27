from abc import ABC, abstractmethod


# Kelas abstrak: tidak bisa dibuat objeknya secara langsung (akan raise TypeError).
# Semua jenis paket hosting wajib mewarisi kelas ini dan mengimplementasikan
# kedua abstract method di bawah.

class PaketHosting(ABC):
    mata_uang = "IDR"
    tarif_pajak = 0.11
    total_paket = 0

    def __init__(self, id_paket, nama, penyimpanan_gb, bandwidth_gb, harga):
        # Protected (_atribut): boleh diakses oleh subclass.
        self._id_paket = id_paket
        self._nama = nama
        self._penyimpanan_gb = penyimpanan_gb
        self._bandwidth_gb = bandwidth_gb

        # Private (__atribut): hanya bisa diubah lewat setter yang memvalidasi.
        self.__harga = 0.0
        self.harga = harga

        PaketHosting.total_paket += 1

    # ---------- Property (Enkapsulasi) ----------
    @property
    def id_paket(self):
        return self._id_paket

    @property
    def nama(self):
        return self._nama

    @property
    def penyimpanan_gb(self):
        return self._penyimpanan_gb

    @property
    def bandwidth_gb(self):
        return self._bandwidth_gb

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

    # ---------- Abstract method ----------
    # Wajib di-override oleh setiap subclass (SharedHosting, VPSHosting, dst.).
    @abstractmethod
    def hitung_total_harga(self):
        """Menghitung total harga per bulan (sudah termasuk pajak)."""
        ...

    @abstractmethod
    def deskripsi_layanan(self):
        """Mengembalikan ringkasan singkat ciri khas layanan paket ini."""
        ...

    # ---------- Method konkret ----------
    # Method konkret yang dipakai bersama oleh semua subclass.
    def jalankan(self):
        """Menjalankan proses aktivasi paket. Perilaku dipilih oleh tiap subclass."""
        print(
            f"[JALAN] Paket '{self._nama}' diaktifkan -> "
            f"{self.deskripsi_layanan()} | "
            f"Biaya: {PaketHosting.mata_uang} {self.hitung_total_harga():,.0f}/bulan"
        )

    # Method konkret: memakai abstract method hitung_total_harga(),
    # sehingga subclass tidak perlu menulis ulang bagian tampilan dasar.
    def tampilkan_info(self):
        print(f"\n{'-' * 42}")
        print(f"  PAKET HOSTING: {self._nama} ({self.deskripsi_layanan()})")
        print(f"{'-' * 42}")
        print(f"  ID           : {self._id_paket}")
        print(f"  Penyimpanan  : {PaketHosting.format_penyimpanan(self._penyimpanan_gb)}")
        print(f"  Bandwidth    : {PaketHosting.format_penyimpanan(self._bandwidth_gb)}")
        print(f"  Harga Dasar  : {PaketHosting.mata_uang} {self.harga:,.0f}/bulan")
        print(f"{'-' * 42}")

    # ---------- Operator overloading ----------
    # __lt__ membuat objek paket bisa dibandingkan dan diurutkan berdasarkan harga total.
    def __lt__(self, other):
        return self.hitung_total_harga() < other.hitung_total_harga()

    def __str__(self):
        return (
            f"[{self._id_paket}] {self._nama} - "
            f"{PaketHosting.mata_uang} {self.harga:,.0f}/bulan"
        )

    # ---------- Class & static method ----------
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
