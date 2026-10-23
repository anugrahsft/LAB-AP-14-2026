def namakm():
    nama = input("Nama: ")
    program = input("Program Studi: ")
    

    with open("biodata.txt", "w") as file:
        file.write(nama + "\n")
        file.write(program + "\n")
        


def baca_file():
    with open("biodata.txt", "r") as file:
        for baris in file:
            print(baris, end="")


namakm()
