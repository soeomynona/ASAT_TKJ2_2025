# remidi1_nama_absen.py

# Inisialisasi penghitung bilangan genap
jumlah_genap = 0

# Input 5 bilangan dan langsung cek apakah genap
for i in range(5):
    angka = int(input(f"Masukkan bilangan ke-{i+1}: "))
    if angka % 2 == 0:
        jumlah_genap += 1

# Tampilkan hasil
print(f"\nJumlah bilangan genap: {jumlah_genap}")