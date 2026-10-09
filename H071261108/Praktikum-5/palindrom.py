ALFABET = "abcdefghijklmnopqrstuvwxyz"


def bersihkan_teks(teks):
    hasil = ""

    for ch in teks:
        kecil = ch.lower()

        if kecil in ALFABET:
            hasil += kecil

    return hasil    


def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))

    if teks == terbalik:
        return (True, -1)

    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)


def inti_palinrome(teks):
    terbaik = {
        "teks": "",
        "panjang": 0,
        "indeks_awal": 0
    }

    n = len(teks)

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks[i:j]

            if len(sub) > terbaik["panjang"] and cek_palinrome(sub)[0]:
                terbaik = {
                    "teks": sub,
                    "panjang": len(sub),
                    "indeks_awal": i
                }

    return terbaik


teks = input("Masukkan teks prasasti: ")

bersih = bersihkan_teks(teks)

print()
print("Teks Bersih:", bersih)
print("Output Terharap:", inti_palinrome(bersih))