def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    jumlah = 0
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            jumlah += 1

    if jumlah == 0:
        print("Buku tidak ditemukan.")
    else:
        print("Ditemukan", jumlah, "buku:")
        nomor = 1
        for buku in inventaris:
            if kata_kunci.lower() in buku["judul"].lower():
                print(
                    nomor,
                    buku["judul"],
                    "-",
                    buku["penulis"],
                    "| Rp" + str(int(buku["harga"])),
                    "| Stok:",
                    buku["stok"],
                )
            nomor += 1


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            if buku["stok"] + jumlah < 0:
                print("Gagal! Stok tidak boleh negatif.")
            else:
                buku["stok"] += jumlah
                print("Stok sekarang:", buku["stok"])
            return
    print("Error! Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    total_stok = 0
    total_aset = 0

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

    print("\n=== RINGKASAN INVENTARIS BOOKNEST ===")
    print("Jumlah jenis buku :", len(inventaris))
    print("Total seluruh stok:", total_stok)
    print("Total nilai aset  : Rp", total_aset)

    if len(inventaris) > 0:
        termahal = inventaris[0]
        for buku in inventaris:
            if buku["harga"] > termahal["harga"]:
                termahal = buku
        print(
            "Buku termahal     :",
            termahal["judul"],
            "(Rp" + str(int(termahal["harga"])) + ")",
        )


inventaris = []

while True:
    print("\n=== BOOKNEST ===")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    menu = input("Pilih menu (1-5): ")

    if menu == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)
        except ValueError:
            print("Harga dan stok harus berupa angka.")

    elif menu == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif menu == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan stok: "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Jumlah perubahan harus berupa angka bulat.")

    elif menu == "4":
        ringkasan_inventaris(inventaris)

    elif menu == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan menu tidak valid.")
