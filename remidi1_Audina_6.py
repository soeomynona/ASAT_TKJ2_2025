# Remidi1_Audina_6.py
jumlah_genap = 0
for i in range(5):
    angka = int(input(f"Masukkan bilangan ke-{i+1}: "))
    if angka % 2 == 0:
        jumlah_genap += 1

print(f"Jumlah bilangan genap: {jumlah_genap}")