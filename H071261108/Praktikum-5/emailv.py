DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email, daftar_terdaftar=None):
    if daftar_terdaftar is None:
        daftar_terdaftar = []

    error = []

    if email.count("@") != 1:
        return ["Harus memiliki tepat satu karakter @."]

    pos = email.find("@")
    local = email[:pos]
    domain = email[pos + 1 :]

    if local == "" or domain == "":
        error.append("Local dan domain tidak boleh kosong.")

    if " " in email:
        error.append("Tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Local tidak boleh diawali/diakhiri titik atau memiliki '..'.")

    if "." not in domain:
        error.append("Domain wajib memiliki minimal satu titik.")

    if ".." in domain or domain.endswith("."):
        error.append("Domain tidak boleh memiliki '..' atau diakhiri titik.")

    for e in daftar_terdaftar:
        if email.lower() == e.lower():
            error.append("Email  sudah terdaftar (Duplikat).")
            break

    if not email.lower().endswith(DOMAIN_RESMI):
        error.append("Wajib berakhiran .com, .id, atau .ac.id.")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = 0

    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + karakter_border * (terpanjang + 2) + "+"

    hasil = garis + "\n"

    for email in daftar_email_valid:
        hasil += "| " + email + " |\n"

    hasil += garis

    return hasil


print("--- Sistem Pencatatan Email Valid ---")
print("Ketik 'tutup' untuk mengakhiri input email.")

border = input("Masukkan border: ")
border = border[:1] or "="

daftar_valid = []

while True:
    email = input("Masukkan email: ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email, daftar_valid)

    if error:
        print(">> Email DITOLAK karena:")

        for e in error:
            print("   -", e)
    else:
        print(">> Email VALID!")
        daftar_valid.append(email)


print()
print("--- HASIL EMAIL VALID ---")

if daftar_valid:
    print(cetak_daftar(daftar_valid, border))
else:
    print("(belum ada email valid)")
