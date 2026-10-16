def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print("Lagu '" + judul + "' berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    print("\n==============================================")
    print("             PLAYLIST MUSIK PLAYTUNE")
    print("==============================================")

    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    total_durasi = 0

    print("No. Judul - Artis | Genre | Durasi")

    nomor = 1
    for lagu in playlist:
        menit = lagu[3] // 60
        detik = lagu[3] % 60

        if detik < 10:
            durasi = str(menit) + ":0" + str(detik)
        else:
            durasi = str(menit) + ":" + str(detik)

        print(str(nomor) + ". " + lagu[0] + " - " + lagu[1], "|", lagu[2], "|", durasi)

        total_durasi += lagu[3]
        nomor += 1

    menit_total = total_durasi // 60
    detik_total = total_durasi % 60

    if detik_total < 10:
        durasi_total = str(menit_total) + ":0" + str(detik_total)
    else:
        durasi_total = str(menit_total) + ":" + str(detik_total)

    print("----------------------------------------------")
    print("Total durasi playlist:", durasi_total)


def filter_genre(playlist, genre_target):
    hasil = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    return hasil


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid!")
    else:
        lagu = playlist.pop(nomor - 1)
        print("Lagu '" + lagu[0] + "' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    print("\n==============================================")
    print("           STATISTIK PLAYLIST PLAYTUNE")
    print("==============================================")

    print("Total lagu:", len(playlist))
    print("Jumlah genre unik:", len(genre_set))

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]

        if genre in distribusi:
            distribusi[genre] += 1
        else:
            distribusi[genre] = 1

    print("\nDistribusi lagu per genre:")
    for genre in distribusi:
        print(genre + ":", distribusi[genre], "lagu")

    if len(playlist) > 0:
        terpanjang = playlist[0]
        terpendek = playlist[0]

        for lagu in playlist:
            if lagu[3] > terpanjang[3]:
                terpanjang = lagu

            if lagu[3] < terpendek[3]:
                terpendek = lagu

        print("\nLagu terpanjang:", terpanjang[0], "-", terpanjang[3], "detik")
        print("Lagu terpendek:", terpendek[0], "-", terpendek[3], "detik")


playlist = []
genre_set = set()

print("==============================================")
print("       SISTEM MANAJEMEN PLAYLIST PLAYTUNE")
print("==============================================")

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        judul = input("Judul lagu: ")
        artis = input("Nama artis: ")
        genre = input("Genre lagu: ")

        try:
            durasi = int(input("Durasi lagu (detik): "))

            if durasi <= 0:
                print("Durasi harus lebih dari 0!")
            else:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Durasi harus berupa angka!")

    elif menu == "2":
        tampilkan_playlist(playlist)

    elif menu == "3":
        if len(genre_set) == 0:
            print("Belum ada genre tersedia.")
        else:
            print("Genre tersedia:", genre_set)
            genre_target = input("Masukkan genre yang dicari: ")
            hasil = filter_genre(playlist, genre_target)

            if len(hasil) == 0:
                print("Lagu dengan genre tersebut tidak ditemukan.")
            else:
                print("\nHasil filter genre:")
                for lagu in hasil:
                    print(lagu[0], "-", lagu[1], "|", lagu[2])

    elif menu == "4":
        tampilkan_playlist(playlist)

        if len(playlist) > 0:
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)

                genre_set = set()
                for lagu in playlist:
                    genre_set.add(lagu[2])
            except ValueError:
                print("Nomor harus berupa angka!")

    elif menu == "5":
        statistik_playlist(playlist, genre_set)

    elif menu == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan menu tidak valid!")
