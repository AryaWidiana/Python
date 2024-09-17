# Membuat class Hewan
class Hewan:
    def __init__(self, nama, jenis, suara):
        self.nama = nama   # Atribut nama
        self.jenis = jenis # Atribut jenis
        self.suara = suara # Atribut suara

    def berbicara(self):
        print(f"{self.nama} adalah seekor {self.jenis} dan bersuara '{self.suara}'.")

# Membuat objek dari class Hewan
kucing = Hewan("Kucing", "Mamalia", "Meong")
anjing = Hewan("Anjing", "Mamalia", "Guk-guk")

# Memanggil metode berbicara untuk setiap objek
kucing.berbicara()
anjing.berbicara()
