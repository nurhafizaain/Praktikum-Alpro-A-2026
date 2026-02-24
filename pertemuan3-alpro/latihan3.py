class Laptop:
    def __init__(self, merek, warna, harga):
        self.merek = merek
        self.warna = warna
        self.harga = harga

    def hidupkan(self):
        print(f"Laptop {self.merek} sedang dihidupkan")

    def matikan(self):
        print(f"Laptop {self.merek} matikan")  

p1 = Laptop("Lenovo", "Putih", 5000000)
p2 = Laptop("Asus", "Silver", 4000000)
p3 = Laptop("Acer", "Hitam", 6000000)

print(p1.merek)
print(p2.warna)
p3.matikan()

p1.merek = "Lenovo"
print(f"Sebelum diubah : {p1.merek}")
p1.ubah_merek("Macbook")
print(f"Setelah diubah : {p1.merek}")
