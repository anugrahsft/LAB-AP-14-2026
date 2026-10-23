import os
import random
from datetime import datetime


# Membuat folder invoices jika belum ada
if not os.path.exists("invoices"):
    os.makedirs("invoices")


def buat_invoice():
    nama_kasir = input("Masukkan nama kasir: ")
    inisial = "".join(nama[0] for nama in nama_kasir.split()).upper()

    daftar_produk = []
    total = 0

    while True:
        nama_produk = input("Nama produk: ")
        harga = int(input("Harga produk: Rp "))
        jumlah = int(input("Jumlah produk: "))

        subtotal = harga * jumlah
        total += subtotal

        daftar_produk.append([nama_produk, harga, jumlah, subtotal])

        lagi = input("Tambah produk lagi? (y/n): ").lower()
        if lagi != "y":
            break

    waktu = datetime.now()
    id_transaksi = (
        inisial + waktu.strftime("%y%m%d%H%M") + str(random.randint(100, 999))
    )

    nama_file = "invoices/" + id_transaksi + ".txt"

    # Membuat invoice
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("========== INVOICE ==========\n")
        file.write("Nama kasir: " + nama_kasir + "\n")
        file.write("Waktu: " + waktu.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write("ID Transaksi: " + id_transaksi + "\n")
        file.write("-----------------------------\n")

        for produk in daftar_produk:
            file.write("Produk: " + produk[0] + "\n")
            file.write("Harga: Rp " + str(produk[1]) + "\n")
            file.write("Jumlah: " + str(produk[2]) + "\n")
            file.write("Subtotal: Rp " + str(produk[3]) + "\n")
            file.write("-----------------------------\n")

        file.write("TOTAL: Rp " + str(total) + "\n")
        file.write("=============================\n")

    # Mencatat transaksi ke riwayat
    file_baru = (
        not os.path.exists("trx_history.txt") or os.path.getsize("trx_history.txt") == 0
    )

    with open("trx_history.txt", "a", encoding="utf-8") as file:
        if file_baru:
            file.write("Waktu | ID Transaksi | Nominal Transaksi\n")
            file.write("-" * 60 + "\n")

        file.write(
            waktu.strftime("%Y-%m-%d %H:%M:%S")
            + " | "
            + id_transaksi
            + " | Rp "
            + str(total)
            + "\n"
        )

    print("\nTransaksi berhasil!")
    print("ID Transaksi:", id_transaksi)
    print("Total belanja: Rp", total)
    print("Invoice tersimpan di:", nama_file)


def cari_invoice():
    id_transaksi = input("Masukkan ID transaksi: ").strip()
    nama_file = "invoices/" + id_transaksi + ".txt"

    if os.path.exists(nama_file):
        with open(nama_file, "r", encoding="utf-8") as file:
            print("\n" + file.read())
    else:
        print("Invoice tidak ditemukan.")


def lihat_riwayat():
    if os.path.exists("trx_history.txt"):
        with open("trx_history.txt", "r", encoding="utf-8") as file:
            data = file.readlines()

        print("\n================ RIWAYAT TRANSAKSI ================")
        print("Waktu               | ID Transaksi   | Nominal")
        print("-" * 60)

        for baris in data:
            baris = baris.strip()

            if not baris:
                continue

            if baris.startswith("Waktu |") or baris.startswith("---"):
                continue

            # Membersihkan data lama yang memiliki teks \n
            baris = baris.replace("\\n", "")
            bagian = baris.split("|")

            if len(bagian) == 3:
                waktu = bagian[0].strip()
                id_transaksi = bagian[1].strip()
                nominal = bagian[2].strip()

                print(waktu + " | " + id_transaksi + " | " + nominal)

        print("=" * 60)
    else:
        print("Belum ada riwayat transaksi.")




while True:
    print("\n===== APLIKASI KASIR =====")
    print("1. Buat transaksi dan invoice")
    print("2. Cari invoice")
    print("3. Lihat riwayat transaksi")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        buat_invoice()
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        lihat_riwayat()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
