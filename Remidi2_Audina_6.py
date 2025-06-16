# Remidi2_Audina_6.py

def luas_persegi(sisi):
    return sisi * sisi

def luas_lingkaran(r):
    return 3.14 * r * r

print("Pilih Menu:")
print("1. Luas Persegi")
print("2. Luas Lingkaran")

pilih = int(input("Pilihan Anda: "))

if pilih == 1:
    sisi = float(input("Masukkan sisi: "))
    print(f"Luas persegi dengan sisi {sisi} adalah {luas_persegi(sisi)}")
elif pilih == 2:
    r = int(input("Masukkan jari-jari: "))
    print(f"Luas lingkaran dengan jari-jari {r} adalah {luas_lingkaran(r):.2f}")
else:
    print("Pilihan tidak valid.")