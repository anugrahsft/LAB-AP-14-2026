
class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective, level):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective
        self.level = level

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"
    
    def tentukan_level(self):
        if self.hitung_skor_akhir() >= 85:
            return "Diamond"
        elif self.hitung_skor_akhir() >= 70:
            return "Platinum"
        elif self.hitung_skor_akhir() >= 60:
            return "Gold"
        else:
            return "Bronze"

    def tampilkan_data(self, nomor):
        print(f"| {nomor:<3} | {self.nama:<15} | {self.id_pemain:<12} | {self.role:<12} | {self.hitung_skor_akhir():<12.2f} | {self.status_performa():<16} | {self.tentukan_level():<10} |")


# Program Utama
daftar_pemain = []

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))

# Input Data Pemain
for i in range(jumlah_pemain):
    print(f"\n-- Data Pemain ke-{i + 1} --")

    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = float(input("Nilai Kill: "))
    nilai_assist = float(input("Nilai Assist: "))
    nilai_objective = float(input("Nilai Objective: "))
    level = None  

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective, level)

    daftar_pemain.append(pemain)


# Menampilkan Rekapitulasi
print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("-" * 91)
print(f"| {'No':<3} | {'Nama':<15} | {'ID Pemain':<12} | {'Role':<12} | {'Skor Akhir':<12} | {'Status':<16} | {'Level':<10} |")
print("-" * 91)

for i, pemain in enumerate(daftar_pemain, start=1):
    pemain.tampilkan_data(i)

print("-" * 91)
