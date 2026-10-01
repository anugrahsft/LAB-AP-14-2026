def konversi(suhu, asal, tujuan):
    skala_valid = ("C", "F", "K")
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    # Langkah 1: ubah semua ke Celsius dulu
    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:
        celsius = suhu - 273.15

    # Langkah 2: ubah dari Celsius ke skala tujuan
    if tujuan == "C":
        return celsius
    elif tujuan == "F":
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15


print("=== Konversi Suhu ===")
while True:
    masukan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if masukan.strip().lower() == "selesai":
        break
    try:
        suhu = float(masukan)
    except ValueError:
        print("Error: Suhu harus berupa angka.")
        continue

    asal = input("Skala asal (C/F/K): ").strip().upper()
    tujuan = input("Skala tujuan (C/F/K): ").strip().upper()

    try:
        hasil = konversi(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
    except ValueError as e:
        print(f"Error: {e}")
