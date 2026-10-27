from sistem_manajemen_hosting_server import (
    PaketHosting,
    SharedHosting,
    VPSHosting,
    Server,
    Klien,
    LayananTagihan,
)


def garis(karakter="-", panjang=100):
    print(karakter * panjang)


# Duck typing: fungsi ini hanya peduli bahwa objek punya method tampilkan_info().
# Server dan Klien TIDAK saling mewarisi, tetapi bisa dipakai di fungsi yang sama.
def cetak_entitas(entitas):
    entitas.tampilkan_info()


def main():
    print("=" * 100)
    print("   POSTTEST PBO: ABSTRAKSI, POLIMORFISME, DAN RELASI UML")
    print("   Tema: Sistem Manajemen Hosting Server")
    print("=" * 100)

    # ==================================================================
    # 1. ABSTRAKSI: BUKTI ABSTRACT CLASS TIDAK BISA DIINSTANSIASI
    # ==================================================================
    print("\n[1] ABSTRAKSI - BUKTI PaketHosting (ABC) TIDAK BISA DIINSTANSIASI")
    garis()
    try:
        PaketHosting("ABS-01", "Paket Abstrak", 10, 100, 50000)
    except TypeError as error:
        print(f"[BUKTI] TypeError: {error}")

    # ==================================================================
    # 2. OBJECT DARI SUBCLASS (PEWARISAN)
    # ==================================================================
    print("\n[2] OBJECT SUBCLASS (INHERITANCE + super().__init__())")
    garis()

    shared_pkg = SharedHosting(
        id_paket="SH-01",
        nama="Starter Web",
        penyimpanan_gb=10,
        bandwidth_gb=100,
        harga=25000,
        maks_domain=3,
    )
    vps_pkg = VPSHosting(
        id_paket="VPS-01",
        nama="Cloud Compute Pro",
        penyimpanan_gb=80,
        bandwidth_gb=1000,
        harga=150000,
        jumlah_core=4,
        sistem_operasi="Ubuntu 22.04 LTS",
    )

    daftar_paket = [shared_pkg, vps_pkg]

    # Auto-call tampilkan_info() versi masing-masing subclass.
    print("\n>> POLIMORFISME PEWARISAN: satu loop, objek berbeda, perilaku berbeda")
    garis()
    for paket in daftar_paket:
        paket.tampilkan_info()

    # Method konkret milik abstract class, dipakai semua subclass.
    # Perilaku tetap berbeda karena memanggil abstract method masing-masing.
    print("\n>> METHOD KONKRET BERSAMA: PaketHosting.jalankan()")
    garis()
    for paket in daftar_paket:
        paket.jalankan()

    # ==================================================================
    # 3. OPERATOR OVERLOADING (__lt__ dan __str__)
    # ==================================================================
    print("\n[3] OPERATOR OVERLOADING (__lt__ dan __str__)")
    garis()
    print(f"str(shared_pkg) : {shared_pkg}")
    print(f"str(vps_pkg)    : {vps_pkg}")
    print(f"vps_pkg < shared_pkg ? {vps_pkg < shared_pkg}")
    print("Urutkan paket dari termurah (memakai __lt__):")
    for paket in sorted(daftar_paket):
        print(f"  - {paket.nama}: Rp {paket.hitung_total_harga():,.0f}")

    # ==================================================================
    # 4. RELASI KOMPOSISI: Server *-- SpesifikasiHardware
    # ==================================================================
    print("\n[4] RELASI KOMPOSISI (Server *-- SpesifikasiHardware)")
    garis()
    print("SpesifikasiHardware dibuat otomatis di dalam Server.__init__(),")
    print("jadi tidak bisa berdiri sendiri tanpa Server.")

    server_jkt = Server(
        id_server="SRV-01",
        nama="Server-Jakarta-01",
        lokasi="Jakarta Cyber DC",
        alamat_ip="192.168.1.10",
        cpu="AMD EPYC 7763 16-Core",
        ram_gb=64,
        tipe_storage="NVMe Gen4 SSD",
    )
    server_bdg = Server(
        id_server="SRV-02",
        nama="Server-Bandung-01",
        lokasi="Bandung DC",
        alamat_ip="192.168.1.11",
        cpu="Intel Xeon Silver 8-Core",
        ram_gb=32,
        tipe_storage="Enterprise SATA SSD",
    )
    print(f">> hardware milik {server_jkt.nama}: {server_jkt.hardware}")

    # ==================================================================
    # 5. RELASI AGREGASI: Server o-- PaketHosting, Klien o-- PaketHosting
    # ==================================================================
    print("\n[5] RELASI AGREGASI (Server o-- PaketHosting, Klien o-- PaketHosting)")
    garis()
    print(">> Paket dibuat di luar Server, lalu dimasukkan lewat tambah_paket():")
    server_jkt.tambah_paket(shared_pkg)
    server_jkt.tambah_paket(vps_pkg)
    server_jkt.tampilkan_info()

    klien = Klien(
        id_klien="CL-001",
        nama="Rendy",
        email="rendy@mail.com",
        kata_sandi="secretpass123",
    )
    print("\n>> Paket yang sama juga disimpan oleh Klien lewat berlangganan():")
    klien.berlangganan(shared_pkg)
    klien.berlangganan(vps_pkg)

    # ==================================================================
    # 6. RELASI ASOSIASI: Klien --> Server
    # ==================================================================
    print("\n[6] RELASI ASOSIASI (Klien --> Server)")
    garis()
    print("Server dikirim sebagai parameter method, tidak disimpan sebagai atribut:")
    klien.ping_server(server_jkt)
    klien.ping_server(server_bdg)

    # ==================================================================
    # 7. DUCK TYPING: Server dan Klien tidak berwarisan, method sama
    # ==================================================================
    print("\n[7] DUCK TYPING - cetak_entitas() untuk Server dan Klien")
    garis()
    print(">> cetak_entitas(server_jkt):")
    cetak_entitas(server_jkt)
    print(">> cetak_entitas(klien):")
    cetak_entitas(klien)

    # ==================================================================
    # 8. SOLID: DIP - LayananTagihan bergantung pada abstraksi PaketHosting
    # ==================================================================
    print("\n[8] SOLID: DIP - LayananTagihan menerima abstraksi PaketHosting")
    garis()
    # SOLID: DIP - daftar berisi objek bertipe PaketHosting (subclass apa pun),
    # bukan bergantung pada SharedHosting atau VPSHosting secara langsung.
    layanan_tagihan = LayananTagihan()
    layanan_tagihan.cetak_tagihan(klien.nama, klien.paket_langganan)

    # ==================================================================
    # 9. RINGKASAN
    # ==================================================================
    print("\n[9] RINGKASAN TOTAL OBJEK")
    garis()
    print(f"  Total Server Terdaftar : {Server.total_server}")
    print(f"  Total Paket Hosting    : {PaketHosting.total_paket}")
    print(f"  Total Klien Aktif      : {Klien.total_klien}")
    print("=" * 100)


if __name__ == "__main__":
    main()