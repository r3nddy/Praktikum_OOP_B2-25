from sistem_manajemen_hosting_server import (
    PaketHosting,
    SharedHosting,
    VPSHosting,
    Server,
    Klien,
)

def garis():
    print("-" * 100)

def main():
    print("=" * 100)
    print("   DEMONSTRASI POSTTEST PBO: RELASI UML & INHERITANCE")
    print("=" * 100)

    # 1. INHERITANCE & METHOD OVERRIDING (Subclass & Superclass)
    print("\n[1] INHERITANCE & METHOD OVERRIDING")
    garis()

    # Subclass 1: SharedHosting (Parent: PaketHosting)
    shared_pkg = SharedHosting(
        id_paket="SH-01",
        nama="Starter Web",
        penyimpanan_gb=10,
        bandwidth_gb=100,
        harga=25000,
        maks_domain=3,
    )

    # Subclass 2: VPSHosting (Parent: PaketHosting)
    vps_pkg = VPSHosting(
        id_paket="VPS-01",
        nama="Cloud Compute Pro",
        penyimpanan_gb=80,
        bandwidth_gb=1000,
        harga=150000,
        jumlah_core=4,
        sistem_operasi="Ubuntu 22.04 LTS",
    )

    # Menampilkan info paket (demonstrasi method overriding)
    print(">> Menampilkan info SharedHosting (Overriding tampilkan_info):")
    shared_pkg.tampilkan_info()

    print(">> Menampilkan info VPSHosting (Overriding tampilkan_info & hitung_total_harga):")
    vps_pkg.tampilkan_info()

    # 2. ENKAPSULASI: TINGKAT AKSES PROTECTED & PRIVATE
    print("\n[2] ENKAPSULASI: PROTECTED (_nama) & PRIVATE (__harga)")
    garis()
    print(f"Akses Protected via Subclass (_nama)  : {shared_pkg._nama}")
    print(f"Akses Protected via Subclass (_id_paket): {shared_pkg._id_paket}")
    print(f"Akses Private via Getter (harga)      : {PaketHosting.mata_uang} {shared_pkg.harga:,.0f}")
    try:
        # Coba akses private secara langsung (harus gagal / AttributeError)
        print(shared_pkg.__harga)
    except AttributeError:
        print("Akses Private langsung (__harga)      : GAGAL (AttributeError - Data Terlindungi)")

    # 3. RELASI KOMPOSISI: Server memiliki SpesifikasiHardware
    print("\n[3] RELASI UML: KOMPOSISI (Server ◆── SpesifikasiHardware)")
    garis()
    print("SpesifikasiHardware dibuat otomatis di dalam konstruktor Server:")
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
    server_jkt.tampilkan_info()

    # 4. RELASI AGREGASI: Server menampung PaketHosting
    print("\n[4] RELASI UML: AGREGASI (Server ◇── PaketHosting)")
    garis()
    print(">> Menambahkan paket independen ke dalam server:")
    server_jkt.tambah_paket(shared_pkg)
    server_jkt.tambah_paket(vps_pkg)
    server_jkt.tampilkan_info()

    # 5. RELASI ASOSIASI: Klien menggunakan PaketHosting & Server
    print("\n[5] RELASI UML: ASOSIASI (Klien ───> PaketHosting & Server)")
    garis()
    klien = Klien(
        id_klien="CL-001",
        nama="Rendy",
        email="rendy@mail.com",
        kata_sandi="secretpass123",
    )
    klien.tampilkan_info()

    print("\n>> Klien berasosiasi dengan paket (berlangganan):")
    klien.berlangganan(shared_pkg)
    klien.berlangganan(vps_pkg)

    print("\n>> Klien berasosiasi dengan server (melakukan ping/akses layanan):")
    klien.ping_server(server_jkt)
    klien.ping_server(server_bdg)

    # 6. RINGKASAN DATA
    print("\n\n" + "=" * 50)
    print("   RINGKASAN TOTAL OBJEK")
    garis()
    print(f"  Total Server Terdaftar : {Server.total_server}")
    print(f"  Total Paket Hosting    : {PaketHosting.total_paket}")
    print(f"  Total Klien Aktif      : {Klien.total_klien}")
    print("=" * 50)


if __name__ == "__main__":
    main()
