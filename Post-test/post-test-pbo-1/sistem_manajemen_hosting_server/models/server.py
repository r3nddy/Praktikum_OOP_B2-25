class Server:
    nama_perusahaan = "RenCorp"
    total_server = 0
    kapasitas_maks_per_server = 50

    def __init__(self, id_server, nama, lokasi, alamat_ip, status="active"):
        self.id_server = id_server      
        self.nama = nama                
        self.lokasi = lokasi            
        self.status = status           
        self.paket = []                 
        self.__alamat_ip = ""           
        self.alamat_ip = alamat_ip   

        Server.total_server += 1

    @property
    def alamat_ip(self):
        return self.__alamat_ip

    @alamat_ip.setter
    def alamat_ip(self, nilai):
        if not Server.validasi_ip(nilai):
            raise ValueError(f"Format IP tidak valid: '{nilai}'. Gunakan format x.x.x.x (0-255).")
        self.__alamat_ip = nilai

    def tampilkan_info(self):
        print(f"\n{'=' * 44}")
        print(f"  SERVER: {self.nama}")
        print(f"{'=' * 44}")
        print(f"  ID         : {self.id_server}")
        print(f"  Lokasi     : {self.lokasi}")
        print(f"  Alamat IP  : {self.alamat_ip}")
        print(f"  Status     : {self.status.upper()}")
        print(f"  Kapasitas  : {len(self.paket)}/{Server.kapasitas_maks_per_server} paket")
        if self.paket:
            print(f"  Paket Aktif:")
            for p in self.paket:
                print(f"    - {p}")
        print(f"{'=' * 44}")

    def tambah_paket(self, paket):
        if len(self.paket) >= Server.kapasitas_maks_per_server:
            print(f"[!] Server {self.nama} sudah penuh! (maks {Server.kapasitas_maks_per_server} paket)")
            return
        self.paket.append(paket)
        print(f"[OK] Paket '{paket.nama}' berhasil ditambahkan ke server {self.nama}.")

    @classmethod
    def dari_dict(cls, data):
        return cls(
            id_server=data["id_server"],
            nama=data["nama"],
            lokasi=data["lokasi"],
            alamat_ip=data["alamat_ip"],
            status=data.get("status", "active"),
        )

    @staticmethod
    def validasi_ip(ip):
        try:
            oktet = ip.split(".")
            return (
                len(oktet) == 4
                and all(0 <= int(nilai) <= 255 for nilai in oktet)
            )
        except (ValueError, TypeError):
            return False

    def __str__(self):
        return f"[{self.id_server}] {self.nama} ({self.lokasi}) - {self.status}"
