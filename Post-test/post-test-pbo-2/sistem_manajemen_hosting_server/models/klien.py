import re


class Klien:
    nama_platform = "Sistem Manajemen Hosting Server"
    total_klien = 0
    status_default = "active"

    def __init__(self, id_klien, nama, email, kata_sandi):
        self.id_klien = id_klien                     
        self.nama = nama                             
        self.email = email                           
        self.status = Klien.status_default           
        self.paket_langganan = []                   
        self.__kata_sandi = ""                        # Private (di-set lewat setter)
        self.kata_sandi = kata_sandi                

        Klien.total_klien += 1

    @property
    def kata_sandi(self):
        return "*" * len(self.__kata_sandi)

    @kata_sandi.setter
    def kata_sandi(self, nilai):
        if not isinstance(nilai, str) or len(nilai.strip()) == 0:
            raise ValueError("Kata sandi tidak boleh kosong!")
        if len(nilai) < 8:
            raise ValueError("Kata sandi harus minimal 8 karakter!")
        self.__kata_sandi = nilai

    # Instance Methods
    def tampilkan_info(self):
        print(f"  KLIEN: {self.nama}")
        print(f"  ID         : {self.id_klien}")
        print(f"  Email      : {self.email}")
        print(f"  Kata Sandi : {self.kata_sandi}")
        print(f"  Status     : {self.status.upper()}")
        print(f"  Platform   : {Klien.nama_platform}")
        if self.paket_langganan:
            print(f"  Paket Langganan:")
            for p in self.paket_langganan:
                print(f"    - {p}")
        else:
            print(f"  Paket Langganan: (belum ada)")
        print(f"{'-' * 44}")

    def berlangganan(self, paket):
        """Berlangganan sebuah paket hosting (Asosiasi)."""
        for p in self.paket_langganan:
            if p.id_paket == paket.id_paket:
                print(f"[!] Klien '{self.nama}' sudah berlangganan paket '{paket.nama}'.")
                return
        self.paket_langganan.append(paket)
        print(f"[OK] Klien '{self.nama}' berhasil berlangganan paket '{paket.nama}'.")

    def ping_server(self, server):
        """Relasi Asosiasi: Klien berinteraksi/mengakses objek Server."""
        print(f"[PING] Klien '{self.nama}' melakukan ping ke Server '{server.nama}' ({server.alamat_ip})... Status: SUCCESS (200 OK)")

    def berhenti_berlangganan(self, id_paket):
        for p in self.paket_langganan:
            if p.id_paket == id_paket:
                self.paket_langganan.remove(p)
                print(f"[OK] Klien '{self.nama}' berhenti berlangganan paket '{p.nama}'.")
                return
        print(f"[!] Paket dengan ID '{id_paket}' tidak ditemukan di langganan klien '{self.nama}'.")


    @classmethod
    def dari_dict(cls, data):
        return cls(
            id_klien=data["id_klien"],
            nama=data["nama"],
            email=data["email"],
            kata_sandi=data["kata_sandi"],
        )

    @staticmethod
    def validasi_email(email):
        """True jika format `lokal@domain`, domain minimal 3 karakter dan punya titik."""
        if not isinstance(email, str):
            return False
        lokal, _, domain = email.partition("@")
        return bool(lokal) and len(domain) >= 3 and "." in domain


    def __str__(self):
        return f"[{self.id_klien}] {self.nama} ({self.email}) - {self.status}"
