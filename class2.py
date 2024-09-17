class Tumbuhan :
    def __init__(self, nama, jenis, buah):
        self.nama = nama
        self.jenis = jenis
        self.buah = buah


    def berbuah(self):
        print(f"{self.nama} adalah tumbuhan {self.jenis} dan memiliki buah '{self.buah}'.")

#Objek
pisang = Tumbuhan ("Pisang", "Berbengkok", "Pisang")
kelapa = Tumbuhan ("Kelapa", "Berair", "Kelapa")
jeruk = Tumbuhan ("Jeruk", "berbiji", "Jeruk")

#print
pisang.berbuah()
kelapa.berbuah()
jeruk.berbuah()