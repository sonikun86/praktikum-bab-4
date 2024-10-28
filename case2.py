# Input angka dengan penanganan kesalahan
try:
    angka = int(input("Masukkan angka: "))

    # Menentukan apakah angka positif, negatif, atau nol
    if angka > 0:
        hasil = "Angka tersebut adalah bilangan positif."
    elif angka < 0:
        hasil = "Angka tersebut adalah bilangan negatif."
    else:
        hasil = "Angka tersebut adalah nol."

    print(hasil)

except ValueError:
    print("lek lek masukan angka lek")
