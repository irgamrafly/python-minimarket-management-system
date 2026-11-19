import json
import random
import math
import datetime
import os

FILE_STOK = "stok_minimarket.json"


#--- FUNGSI DATABASE (BACA & TULIS JSON) ---
def muat_stok():
    if not os.path.exists(FILE_STOK):
        return []
    with open(FILE_STOK, "r") as file:
        return json.load(file)


def simpan_stok(data):
    with open(FILE_STOK, "w") as file:
        json.dump(data, file, indent=4)


#--- FUNGSI PENCARI (PRODUSEN SINYAL) ---
def cari_barang(data_stok, kode):
    i = 0
    while i < len(data_stok):
        if data_stok[i]["kode"] == kode:
            return i # kembalikan angka (indeks) kalau ketemu
        i += 1
    return "tidak ada" # sinyal gagal pengganti -1


#--- FUNGSI FITUR UTAMA ---
def lihat_barang():
    data = muat_stok()
    if len(data) == 0:
        print("\nStok masih kosong! silakan tambah barang dulu.")
        return

    print("\n--- KATALOG MINIMARKET ---")
    i = 0
    while i < len(data):
        brg = data[i]
        print(f"kode:{brg['kode']} | {brg['nama']} | stok: {brg['stok']} | harga: Rp{brg['harga']}")
        i += 1


def tambah_barang():
    data = muat_stok()
    kode = input("masukkan kode barang (ex: M01): ")

    # Cek dulu apakah kode sudah di pakai
    if cari_barang(data, kode) != "tidak ada":
        print("ERROR: Kode barang sudah ada di sistem!")
        return

    nama = input("nama barang: ")
    stok = int(input("jumlah stok: "))
    harga = int(input("harga satuan: "))

    barang_baru = {
        "kode": kode,
        "nama": nama,
        "stok": stok,
        "harga": harga
    }

    data.append(barang_baru)
    simpan_stok(data)
    print(f"Barang {nama} berhasil ditambahkan ke database JSON!")


def fitur_kasir():
    data = muat_stok()
    if len(data) == 0:
        print("Belum ada data barang.")
        return

    kode_beli = input("masukan kode barang yang ingin dibeli: ")
    i = cari_barang(data, kode_beli)
    if i == "tidak ada":
        print("Kode barang tidak ditemukan.")
        return

    jumlah_beli = int(input("Berapa banyak? "))
    if data[i]["stok"] < jumlah_beli:
        print(f"Stok tidak cukup. Stok tersedia: {data[i]['stok']}")
        return

    data[i]["stok"] -= jumlah_beli
    simpan_stok(data)
    subtotal = data[i]["harga"] * jumlah_beli
    pajak = subtotal * 0.11
    total_bayar = subtotal + math.ceil(pajak)
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    no_resi = random.randint(100000, 999999)

    print("==============================")
    print("\n---STRUK PEMBELIAN---")
    print("==============================")
    print(f"Waktu: {waktu}")
    print(f"No Resi: {no_resi}")
    print("------------------------------")
    print(f" {data[i]['nama']} x {jumlah_beli}")
    print(f"Subtotal: Rp{subtotal}")
    print(f"Pajak (11%): Rp{math.ceil(pajak)}")
    print("------------------------------")
    print(f"Total Bayar: Rp{total_bayar}")
    print("==============================")


#--- PROGRAM UTAMA ---
print("=== SELAMAT DATANG DI MINIMARKET ===")
while True:
    print("\nMenu kasir:")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Kasir (Beli barang)")
    print("4. Keluar")

    pilih = input("Pilih menu (1-4): ")

    if pilih == "1":
        lihat_barang()
    elif pilih == "2":
        tambah_barang()
    elif pilih == "3":
        fitur_kasir()
    elif pilih == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silahkan pilih menu yang tersedia.")
