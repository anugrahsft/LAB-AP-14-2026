def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print("Kandidat sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print("'" + nama + "' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_asli = nama_pemilih
    nama_pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()
    
    if nama_pemilih in kandidat_set:
        print("error")
    elif nama_pemilih in rekap_suara:
        print("'" + nama_asli + "' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print("Error! Kandidat tidak ditemukan.")
    else:
        rekap_suara[nama_pemilih] = pilihan
        print("Suara '" + nama_asli + "' untuk '" + pilihan + "' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        jumlah = 0

        for nama_pemilih in rekap_suara:
            if rekap_suara[nama_pemilih] == kandidat:
             jumlah += 1

        perolehan[kandidat] = jumlah

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n========================================")
    print("  HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    total_suara = 0
    suara_tertinggi = 0

    for kandidat in perolehan:
        print(" ", kandidat + ":", perolehan[kandidat], "suara")
        total_suara += perolehan[kandidat]

        if perolehan[kandidat] > suara_tertinggi:
            suara_tertinggi = perolehan[kandidat]

    print("\nTotal suara masuk:", total_suara)

    pemenang = []

    for kandidat in perolehan:
        if perolehan[kandidat] == suara_tertinggi:
            pemenang.append(kandidat)

    if len(pemenang) > 1:
        print("Hasil SERI antara:", ", ".join(pemenang))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print("PEMENANG:", pemenang[0], "dengan", suara_tertinggi, "suara!")

    print("========================================")


kandidat_set = set()
rekap_suara = {}

print("========================================")
print("  SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

print("\nKandidat terdaftar:", kandidat_set)

if len(kandidat_set) < 2:
    print("Kandidat minimal harus 2 orang!")
else:
    print("\n--- FASE PEMUNGUTAN SUARA ---")

    while True:
        nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ")

        if nama_pemilih == "":
            break

        print("Kandidat yang tersedia:", kandidat_set)
        pilihan = input("Pilih kandidat: ")

        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)
