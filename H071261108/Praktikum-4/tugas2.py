def rekap(*nilai):
    rata = sum(nilai) / len(nilai)
    return rata, max(nilai), min(nilai)


def ke_angka(teks):
    try:
        return int(teks)
    except ValueError:
        return float(teks)


daftar = []
while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
        break
    daftar.append(ke_angka(masukan))

if len(daftar) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = rekap(*daftar)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
