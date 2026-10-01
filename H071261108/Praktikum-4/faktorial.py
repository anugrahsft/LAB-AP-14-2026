def faktorial(n):
    hasil = 1

    for i in range(1, n + 1):
        hasil = hasil * i

    return hasil


angka = int(input("Masukkan angka: "))

print("Faktorial dari", angka, "adalah", faktorial(angka))
