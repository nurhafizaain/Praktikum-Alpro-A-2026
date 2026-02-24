while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")
        print("Selesai.")
        break
        
    except ValueError:
        print("Error: Input harus berupa angka!")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol!")

print("Program selesai.")
    