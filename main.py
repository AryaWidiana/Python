def tambah (a, b):
    return a + b

def kurang (a, b):
    return a - b

def kali (a, b):
    return a * b

def bagi (a, b):
    if b != 0:
        return a / b
    else: 
        return "Error! Pembagian tidak dapat dilakukan dengan angka 0"
    
def hasil(hasil):
    if hasil.integer():
        return int(hasil)
    else:
        return hasil

def kakulator():
    print("Pilih Operasi: ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
