# Meminta input bulan dari pengguna
try:
    bulan = int(input("Masukkan bulan (1-12): "))

    if 1 <= bulan <= 12:
        # Jumlah hari dalam setiap bulan
        if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
            hari = 31
        elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
            hari = 30
        else:  # bulan == 2
            hari = 28

        print(f"Jumlah hari di bulan {bulan} adalah {hari}.")
    else:
        print("Bulan yang Anda masukkan tidak valid. Silakan masukkan bulan antara 1 hingga 12.")
except ValueError:
    print("Input tidak valid. Pastikan Anda memasukkan angka untuk bulan.")