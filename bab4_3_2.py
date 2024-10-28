# Meminta input bilangan dari pengguna
bilangan = float(input("Masukkan sebuah bilangan: "))

# Menggunakan ternary operator untuk menentukan kategori bilangan
hasil = "Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "Nol"

# Menampilkan hasil
print(hasil)