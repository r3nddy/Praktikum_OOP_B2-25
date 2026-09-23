from sistem_manajemen_hosting_server import PaketHosting, Server, Klien

def garis():
    print("-" * 48)

def main():

    # 1. Membuat paket hosting
    print("\n1. Membuat paket hosting")
    starter = PaketHosting("PKG-01", "Starter", 5, 100, 25000)
    bisnis = PaketHosting("PKG-02", "Business", 1024, 2000, 150000)

    starter.tampilkan_info()
    bisnis.tampilkan_info()

    # 2. Membuat server 
    print("\n2. Membuat server")
    server_1 = Server("SRV-01", "SRV-JKT-01", "Jakarta", "192.168.1.10")
    server_2 = Server.dari_dict({
        "id_server": "SRV-02",
        "nama": "SRV-BDG-01",
        "lokasi": "Bandung",
        "alamat_ip": "192.168.1.11",
    })
    server_1.tampilkan_info()
    server_2.tampilkan_info()

    # 3. Memasukkan paket ke server
    print("\n3. Menambahkan paket ke server")
    server_1.tambah_paket(starter)
    server_2.tambah_paket(bisnis)
    server_1.tampilkan_info()
    server_2.tampilkan_info()

    # 4. Membuat klien
    print("\n4. Membuat klien")
    klien_1 = Klien("CL-01", "lowlight", "lowlight@mail.com", "secret123")
    klien_2 = Klien.dari_dict({
        "id_klien": "CL-02",
        "nama": "Rendy",
        "email": "rendyren@mail.com",
        "kata_sandi": "password069",
    })
    klien_1.tampilkan_info()
    klien_2.tampilkan_info()

    # 5. Klien berlangganan paket
    print("\n5. Klien berlangganan paket")
    klien_1.berlangganan(starter)
    klien_2.berlangganan(bisnis)
    klien_1.berlangganan(starter)  
    klien_1.tampilkan_info()
    klien_2.tampilkan_info()

    # 5a. Pengujian setter valid dan tidak valid
    print("\n5a. Pengujian setter")
    klien_1.kata_sandi = "sandi_baru123"
    print(f"  Kata sandi baru klien 1: {klien_1.kata_sandi}")
    try:
        klien_1.kata_sandi = "abc"
    except ValueError as error:
        print(f"  Data kata sandi ditolak: {error}")

    server_1.alamat_ip = "10.0.0.5"
    print(f"  IP baru server 1: {server_1.alamat_ip}")
    try:
        server_1.alamat_ip = "999.1.1.1"
    except ValueError as error:
        print(f"  Data IP ditolak: {error}")

    bisnis.harga = 175000
    print(f"  Harga baru paket Business: {bisnis.harga:,.0f}")
    try:
        bisnis.harga = -5000
    except ValueError as error:
        print(f"  Data harga ditolak: {error}")

    # 6. Klien berhenti berlangganan
    print("\n6. Klien berhenti berlangganan paket 'PKG-01'")
    klien_1.berhenti_berlangganan("PKG-01")
    klien_1.tampilkan_info()

    # 7. Class method (dari_dict)
    print("\n7. Membuat objek dari dictionary (dari_dict)")
    data_paket = {
        "id_paket": "PKG-03",
        "nama": "Enterprise",
        "penyimpanan_gb": 2048,
        "bandwidth_gb": 5000,
        "harga": 450000,
    }
    enterprise = PaketHosting.dari_dict(data_paket)
    print(f"  {enterprise}")

    # 8. Static method
    print("\n8. Static method")
    print(f"  format_penyimpanan(2048)            = {PaketHosting.format_penyimpanan(2048)}")
    print(f"  Server.validasi_ip('10.0.0.1')      = {Server.validasi_ip('10.0.0.1')}")
    print(f"  Server.validasi_ip('999.1.1.1')     = {Server.validasi_ip('999.1.1.1')}")
    print(f"  Klien.validasi_email('a@b.com')     = {Klien.validasi_email('a@b.com')}")
    print(f"  Klien.validasi_email('salah')       = {Klien.validasi_email('salah')}")

    # 9. Update tarif pajak (atribut kelas)
    print("\n9. Mengubah tarif pajak menjadi 12%")
    PaketHosting.ubah_tarif_pajak(0.12)
    print(f"  Total harga '{bisnis.nama}': "
        f"{PaketHosting.mata_uang} {bisnis.hitung_total_harga():,.0f}/bulan")

    # 10. Ringkasan sistem
    print("\n\n" + "=" * 48)
    print("   RINGKASAN SISTEM")
    garis()
    print(f"  Perusahaan   : {Server.nama_perusahaan}")
    print(f"  Platform     : {Klien.nama_platform}")
    print(f"  Mata Uang    : {PaketHosting.mata_uang}")
    print(f"  Tarif Pajak  : {PaketHosting.tarif_pajak * 100:.0f}%")
    garis()
    print(f"  Total Server : {Server.total_server}")
    print(f"  Total Paket  : {PaketHosting.total_paket}")
    print(f"  Total Klien  : {Klien.total_klien}")
    garis()
    print(f"\n  Daftar Server :")
    for s in (server_1, server_2):
        print(f"    - {s}")
    print(f"\n  Daftar Paket  :")
    for p in (starter, bisnis, enterprise):
        print(f"    - {p}")
    print(f"\n  Daftar Klien  :")
    for k in (klien_1, klien_2):
        print(f"    - {k}")
    print("=" * 48)


if __name__ == "__main__":
    main()
