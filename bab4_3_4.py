# Input ukuran benda dengan penanganan kesalahan
try:
    ukuran1 = float(input("Masukkan ukuran benda 1: "))
    ukuran2 = float(input("Masukkan ukuran benda 2: "))
    ukuran3 = float(input("Masukkan ukuran benda 3: "))
    
    # Mengumpulkan ukuran ke dalam list
    benda = [ukuran1, ukuran2, ukuran3]

    # Menghitung jumlah ukuran yang unik
    unik = set(benda)

    # Menentukan hasil berdasarkan jumlah ukuran unik
    if len(unik) == 1:
        hasil = "3 benda sama"
    elif len(unik) == 2:
        hasil = "2 benda sama"
    else:
        hasil = "Tidak ada yang sama"

    # Mencetak hasil
    print(hasil)

except ValueError:
    print("lek masukan angka lek.")
