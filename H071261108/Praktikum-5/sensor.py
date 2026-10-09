ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    hasil = []

    if kata == "":
        return hasil

    teks_kecil = teks.lower()
    kata_kecil = kata.lower()   

    start = 0

    while True:
        i = teks_kecil.find(kata_kecil, start)

        if i == -1:
            break

        hasil.append(i)
        start = i + 1

    return hasil


def cek_batas_kata(teks, i, panjang):
    if i > 0:
        sebelum = teks[i - 1].lower()

        if sebelum in ALFABET:
            return False

    akhir = i + panjang

    if akhir < len(teks):
        sesudah = teks[akhir].lower()

        if sesudah in ALFABET:
            return False

    return True


def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    indeks_valid = []

    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang):
            indeks_valid.append(i)

    simbol = simbol[:1] or "*"
    pengganti = simbol * panjang

    hasil = ""
    posisi = 0

    for i in indeks_valid:
        hasil += teks[posisi:i] + pengganti
        posisi = i + panjang

    hasil += teks[posisi:]

    return (hasil, len(indeks_valid), indeks_valid)


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)
