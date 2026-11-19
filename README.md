# 🛒 Python Minimarket Management & Cashier System

### Sistem Manajemen Minimarket dan Kasir Berbasis Python

---

## 📌 Deskripsi Proyek

**Python Minimarket Management & Cashier System** merupakan program berbasis Python yang dirancang untuk membantu proses pengelolaan minimarket secara sederhana melalui sistem terminal.

Program ini menyediakan fitur untuk melihat katalog barang, menambahkan produk baru, serta melakukan transaksi pembelian melalui sistem kasir. Data inventaris disimpan menggunakan file JSON sehingga informasi barang dan perubahan stok tetap tersimpan meskipun program telah ditutup.

Selain itu, sistem kasir dilengkapi dengan perhitungan subtotal, pajak sebesar 11%, total pembayaran, nomor resi otomatis, dan pencetakan struk pembelian yang menampilkan waktu transaksi.

## ✨ Fitur Utama

- **📦 Lihat Katalog Barang**  
  Menampilkan seluruh data barang yang tersimpan, meliputi kode, nama, jumlah stok, dan harga satuan.

- **➕ Tambah Barang**  
  Memungkinkan pengguna menambahkan produk baru ke dalam database dengan validasi kode barang agar tidak terjadi duplikasi.

- **🛍️ Sistem Transaksi Kasir**  
  Memproses pembelian barang berdasarkan kode produk dan jumlah pembelian yang dimasukkan pengguna.

- **📉 Pembaruan Stok Otomatis**  
  Mengurangi stok barang setelah transaksi berhasil dilakukan dan menyimpan perubahan ke database JSON.

- **💰 Perhitungan Total Pembayaran**  
  Menghitung subtotal, pajak 11%, dan total pembayaran secara otomatis.

- **🧾 Cetak Struk Pembelian**  
  Menghasilkan informasi transaksi berupa waktu pembelian, nomor resi, nama barang, jumlah pembelian, subtotal, pajak, dan total pembayaran.

- **🔐 Validasi Data**  
  Memeriksa keberadaan barang, mencegah penggunaan kode duplikat, dan memastikan stok mencukupi sebelum transaksi diproses.

- **💾 Penyimpanan Database JSON**  
  Menyimpan dan membaca data inventaris menggunakan file JSON agar data tidak hilang ketika program ditutup.

## 🛠️ Teknologi dan Konsep Pemrograman

| Teknologi / Konsep | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| JSON | Penyimpanan data inventaris |
| List & Dictionary | Pengelolaan struktur data barang |
| Function | Membagi program menjadi beberapa fungsi |
| While Loop | Menjalankan menu dan proses pencarian |
| If-Else | Mengatur percabangan dan validasi |
| File Handling | Membaca dan menulis file JSON |
| Random | Menghasilkan nomor resi otomatis |
| Math | Menghitung dan membulatkan pajak |
| Datetime | Mengambil waktu transaksi |
| OS | Memeriksa keberadaan file database |

## 📂 Struktur File

```text
python-minimarket-management-system/
│
├── main.py
├── stok_minimarket.json
└── README.md
```

**Keterangan:**
- `main.py` : File utama yang berisi seluruh logika program.
- `stok_minimarket.json` : File database untuk menyimpan data barang.
- `README.md` : Dokumentasi dan panduan penggunaan program.

*Catatan: File JSON akan dibuat secara otomatis ketika data barang pertama kali disimpan.*

## ⚙️ Fungsi Utama Program

**1. `muat_stok()`**

Membaca data inventaris dari file JSON. Jika file belum tersedia, fungsi akan mengembalikan List kosong.

**2. `simpan_stok(data)`**

Menyimpan perubahan data inventaris ke dalam file JSON menggunakan format yang terstruktur.

**3. `cari_barang(data_stok, kode)`**

Mencari barang berdasarkan kode produk dan mengembalikan indeks apabila ditemukan.

**4. `lihat_barang()`**

Menampilkan seluruh katalog barang yang tersimpan dalam database.

**5. `tambah_barang()`**

Menambahkan barang baru dengan memeriksa apakah kode produk sudah digunakan sebelumnya.

**6. `fitur_kasir()`**

Memproses transaksi pembelian, memperbarui stok, menghitung pajak, menghasilkan nomor resi, dan menampilkan struk pembelian.

## 🚀 Cara Menjalankan Program

Pastikan Python sudah terinstal pada perangkat.

**1. Clone Repository**

```bash
git clone https://github.com/USERNAME/python-minimarket-management-system.git
```

**2. Masuk ke Folder Proyek**

```bash
cd python-minimarket-management-system
```

**3. Jalankan Program**

```bash
python main.py
```

Program menggunakan modul bawaan Python sehingga tidak memerlukan instalasi library eksternal tambahan.

## 🖥️ Tampilan Menu Program

```text
=== SELAMAT DATANG DI MINIMARKET ===

Menu kasir:
1. Lihat Barang
2. Tambah Barang
3. Kasir (Beli barang)
4. Keluar

Pilih menu (1-4):
```

| Menu | Fungsi |
|---|---|
| 1 | Melihat katalog barang |
| 2 | Menambahkan barang baru |
| 3 | Melakukan transaksi pembelian |
| 4 | Mengakhiri program |

## 🧾 Sistem Perhitungan Transaksi

Program menghitung pembayaran menggunakan tiga tahapan:

**1. Menghitung Subtotal**

Subtotal diperoleh dari harga satuan dikalikan jumlah barang yang dibeli.

**2. Menghitung Pajak**

Pajak dihitung sebesar 11% dari subtotal dan dibulatkan ke atas menggunakan `math.ceil()`.

**3. Menghitung Total Pembayaran**

Total pembayaran diperoleh dari penjumlahan subtotal dan pajak.

Rumus:

```text
Subtotal = Harga × Jumlah Pembelian

Pajak = Subtotal × 11%

Total Bayar = Subtotal + Pajak
```

## 🎯 Tujuan Pengembangan

Proyek ini dikembangkan sebagai implementasi konsep pemrograman Python dalam studi kasus pengelolaan minimarket sederhana.

Melalui proyek ini, pengembang mempelajari:

- Pengelolaan data menggunakan List dan Dictionary.
- Penerapan Function untuk membangun program modular.
- Penggunaan While Loop dan If-Else.
- Pengolahan file menggunakan JSON dan File Handling.
- Penerapan modul Random, Math, Datetime, dan OS.
- Pembuatan sistem transaksi dan pengelolaan stok barang.

## 👨‍💻 Identitas Pengembang

**Irga Mochamad Rafly**

- **NPM:** 267006111160
- **Kelas:** B
- **Program Studi:** Informatika
- **Fakultas:** Teknik
- **Universitas:** Universitas Siliwangi (UNSIL)

---

<p align="center">
  <b>Developed with Python 🐍</b><br>
  <i>Learning, Building, and Improving Through Code.</i>
</p>
