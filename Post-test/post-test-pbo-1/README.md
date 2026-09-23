# Sistem Manajemen Hosting Server

Program Python berbasis OOP untuk mensimulasikan pengelolaan layanan hosting. Program mengelola paket hosting, server, klien, langganan, harga, alamat IP, dan validasi data.

Konsep OOP yang diterapkan:

- Class dan object
- Atribut kelas dan atribut instance
- Instance method
- Class method
- Static method
- Encapsulation
- Property, getter, dan setter
- Validasi input menggunakan `ValueError`

## 1. Struktur Folder

```text
pt1-pbo/
├── main.py
├── README.md
└── sistem_manajemen_hosting_server/
    ├── __init__.py
    └── models/
        ├── __init__.py
        ├── paket_hosting.py
        ├── server.py
        └── klien.py
```

`main.py` berisi demonstrasi penggunaan program. Folder `models` berisi tiga class utama.

## 2. Penjelasan Program

Program menjalankan alur berikut:

1. Membuat paket hosting `Starter` dan `Business`.
2. Membuat server Jakarta dan Bandung.
3. Menambahkan paket hosting ke server.
4. Membuat klien `lowlight` dan `Rendy`.
5. Menghubungkan klien dengan paket melalui proses berlangganan.
6. Menguji setter dengan data valid dan tidak valid.
7. Menghentikan langganan paket.
8. Membuat paket `Enterprise` menggunakan `dari_dict()`.
9. Menguji static method.
10. Mengubah tarif pajak dari 11% menjadi 12%.
11. Menampilkan ringkasan seluruh object yang dibuat.

Data utama yang digunakan di `main.py`:

| Jenis  | Data                                |
| ------ | ----------------------------------- |
| Paket  | Starter: 5 GB, 100 GB, IDR 25.000   |
| Paket  | Business: 1 TB, 2 TB, IDR 150.000   |
| Paket  | Enterprise: 2 TB, 5 TB, IDR 450.000 |
| Server | SRV-JKT-01, Jakarta, `192.168.1.10` |
| Server | SRV-BDG-01, Bandung, `192.168.1.11` |
| Klien  | `lowlight`, `lowlight@mail.com`     |
| Klien  | `Rendy`, `rendyren@mail.com`        |

## 3. Struktur Class

```text
PaketHosting
├── Menyimpan data paket hosting
├── Mengelola harga dan pajak
├── Menghitung harga setelah pajak
└── Memformat kapasitas penyimpanan

Server
├── Menyimpan data server
├── Menyimpan daftar paket
└── Memvalidasi alamat IPv4

Klien
├── Menyimpan data klien
├── Mengelola paket langganan
├── Menyembunyikan kata sandi
└── Memvalidasi email
```

### 3.1 Class `PaketHosting`

File: `sistem_manajemen_hosting_server/models/paket_hosting.py`

Class ini merepresentasikan paket layanan hosting.

#### Atribut kelas

| Atribut       | Keterangan                                   |
| ------------- | -------------------------------------------- |
| `mata_uang`   | Mata uang harga, yaitu `IDR`.                |
| `tarif_pajak` | Tarif pajak global, awalnya `0.11` atau 11%. |
| `total_paket` | Jumlah object `PaketHosting` yang dibuat.    |

#### Atribut instance

| Atribut          | Hak akses | Keterangan                                  |
| ---------------- | --------- | ------------------------------------------- |
| `id_paket`       | Public    | ID unik paket.                              |
| `nama`           | Public    | Nama paket hosting.                         |
| `penyimpanan_gb` | Public    | Kapasitas penyimpanan dalam GB.             |
| `bandwidth_gb`   | Public    | Kapasitas bandwidth dalam GB.               |
| `__harga`        | Private   | Harga dasar paket melalui property `harga`. |

#### Method

- `tampilkan_info()` — menampilkan detail paket, pajak, dan total harga.
- `hitung_total_harga()` — menghitung harga dasar ditambah pajak.
- `dari_dict(data)` — class method untuk membuat object dari dictionary.
- `ubah_tarif_pajak(tarif_baru)` — mengubah tarif pajak global.
- `format_penyimpanan(gb)` — mengubah kapasitas GB menjadi format GB atau TB.
- `__str__()` — menghasilkan representasi singkat object.

#### Property `harga`

Setter `harga` menolak nilai yang bukan angka atau bernilai negatif.

```python
paket = PaketHosting("PKG-01", "Starter", 5, 100, 25000)
paket.harga = 30000       # Valid
paket.harga = -1000       # ValueError
```

### 3.2 Class `Server`

File: `sistem_manajemen_hosting_server/models/server.py`

Class ini merepresentasikan server hosting.

#### Atribut kelas

| Atribut                     | Keterangan                                |
| --------------------------- | ----------------------------------------- |
| `nama_perusahaan`           | Nama perusahaan hosting, yaitu `RenCorp`. |
| `total_server`              | Jumlah object `Server` yang dibuat.       |
| `kapasitas_maks_per_server` | Batas paket pada satu server, yaitu 50.   |

#### Atribut instance

| Atribut       | Hak akses | Keterangan                              |
| ------------- | --------- | --------------------------------------- |
| `id_server`   | Public    | ID unik server.                         |
| `nama`        | Public    | Nama server.                            |
| `lokasi`      | Public    | Lokasi data center.                     |
| `status`      | Public    | Status server, default `active`.        |
| `paket`       | Public    | Daftar paket pada server.               |
| `__alamat_ip` | Private   | Alamat IP melalui property `alamat_ip`. |

#### Method

- `tampilkan_info()` — menampilkan detail server dan paket aktif.
- `tambah_paket(paket)` — menambahkan paket selama kapasitas belum penuh.
- `dari_dict(data)` — class method untuk membuat object dari dictionary.
- `validasi_ip(ip)` — static method untuk memvalidasi alamat IPv4.
- `__str__()` — menghasilkan representasi singkat object.

#### Property `alamat_ip`

Setter memvalidasi alamat IPv4 dengan memisahkan string menggunakan `split(".")`. Alamat harus memiliki empat bagian dan setiap bagian harus berada pada rentang `0` sampai `255`. Nilai tidak valid menghasilkan `ValueError`.

```python
server.alamat_ip = "10.0.0.5"     # Valid
server.alamat_ip = "999.1.1.1"    # ValueError
```

### 3.3 Class `Klien`

File: `sistem_manajemen_hosting_server/models/klien.py`

Class ini merepresentasikan pelanggan layanan hosting.

#### Atribut kelas

| Atribut          | Keterangan                              |
| ---------------- | --------------------------------------- |
| `nama_platform`  | Nama platform hosting.                  |
| `total_klien`    | Jumlah object `Klien` yang dibuat.      |
| `status_default` | Status awal klien baru, yaitu `active`. |

#### Atribut instance

| Atribut           | Hak akses | Keterangan                                       |
| ----------------- | --------- | ------------------------------------------------ |
| `id_klien`        | Public    | ID unik klien.                                   |
| `nama`            | Public    | Nama klien.                                      |
| `email`           | Public    | Alamat email klien.                              |
| `status`          | Public    | Status akun klien.                               |
| `paket_langganan` | Public    | Daftar paket yang dilanggani.                    |
| `__kata_sandi`    | Private   | Kata sandi asli yang tidak ditampilkan langsung. |

#### Method

- `tampilkan_info()` — menampilkan profil klien.
- `berlangganan(paket)` — menambahkan paket ke langganan dan menolak duplikasi.
- `berhenti_berlangganan(id_paket)` — menghapus paket dari langganan berdasarkan ID.
- `dari_dict(data)` — class method untuk membuat object dari dictionary.
- `validasi_email(email)` — static method untuk memeriksa format email sederhana.
- `__str__()` — menghasilkan representasi singkat object.

#### Property `kata_sandi`

- Getter menampilkan kata sandi dalam bentuk mask.
- Setter menolak kata sandi kosong atau kurang dari 8 karakter.

```python
klien.kata_sandi = "sandi_baru123"  # Valid
klien.kata_sandi = "abc"            # ValueError
```

## 4. Penerapan Konsep OOP

### Class dan object

Tiga class didefinisikan di folder `models`. Object dibuat di `main.py`.

```python
starter = PaketHosting("PKG-01", "Starter", 5, 100, 25000)
server_1 = Server("SRV-01", "SRV-JKT-01", "Jakarta", "192.168.1.10")
klien_1 = Klien("CL-01", "lowlight", "lowlight@mail.com", "secret123")
```

### Instance method

Instance method menerima `self` dan bekerja menggunakan data object.

```python
server_1.tampilkan_info()
klien_1.berlangganan(starter)
```

### Class method

Class method menerima `cls`. Program menggunakannya untuk membuat object dari dictionary.

```python
server_2 = Server.dari_dict(data_server)
klien_2 = Klien.dari_dict(data_klien)
enterprise = PaketHosting.dari_dict(data_paket)
```

### Static method

Static method tidak menerima `self` atau `cls`. Method ini digunakan sebagai utility yang tidak bergantung pada object tertentu.

```python
Server.validasi_ip("10.0.0.1")
Klien.validasi_email("a@b.com")
PaketHosting.format_penyimpanan(2048)
```

### Encapsulation dan property

Data penting seperti harga, alamat IP, dan kata sandi disimpan dalam atribut private menggunakan awalan `__`. Akses dilakukan melalui property dan setter. Setter memvalidasi nilai sebelum disimpan.

## 5. Panduan Menjalankan Program

Pastikan Python sudah terpasang. Buka terminal pada folder project, lalu jalankan:

```bash
python main.py
```

Jika perintah `python` tidak tersedia, gunakan:

```bash
python3 main.py
```

Program akan menampilkan informasi paket, server, klien, proses langganan, hasil validasi, dan ringkasan sistem.

## 6. Panduan Pengujian

### 6.1 Pemeriksaan sintaks

Jalankan perintah berikut dari folder project:

```bash
python -m py_compile main.py sistem_manajemen_hosting_server/models/paket_hosting.py sistem_manajemen_hosting_server/models/server.py sistem_manajemen_hosting_server/models/klien.py
```

Jika berhasil, Python tidak menampilkan pesan error.

### 6.2 Pengujian program utama

```bash
python main.py
```

### 6.3 Pengujian setter valid

Bagian `[5a] Pengujian setter` di `main.py` menguji perubahan berikut:

```python
klien_1.kata_sandi = "sandi_baru123"
server_1.alamat_ip = "10.0.0.5"
bisnis.harga = 175000
```

Ketiga perubahan harus berhasil.

### 6.4 Pengujian setter tidak valid

Program menggunakan `try-except` untuk menguji data berikut:

```python
klien_1.kata_sandi = "abc"
server_1.alamat_ip = "999.1.1.1"
bisnis.harga = -5000
```

Ketiga data harus ditolak dan menghasilkan `ValueError`.

### 6.5 Pengujian class method

Program membuat object dari dictionary menggunakan:

```python
server_2 = Server.dari_dict({...})
klien_2 = Klien.dari_dict({...})
enterprise = PaketHosting.dari_dict({...})
```

Program juga menguji perubahan atribut kelas:

```python
PaketHosting.ubah_tarif_pajak(0.12)
```

### 6.6 Pengujian static method

Output yang diharapkan:

```text
format_penyimpanan(2048)        = 2 TB
Server.validasi_ip('10.0.0.1')  = True
Server.validasi_ip('999.1.1.1') = False
Klien.validasi_email('a@b.com') = True
Klien.validasi_email('salah')   = False
```
