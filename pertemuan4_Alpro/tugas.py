class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f"Nama '{nama}' terlalu pendek! Minimal 3 karakter.")

class UmurError(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f"Umur {umur} tidak memenuhi syarat! Harus antara 17-60 tahun.")

class EmailError(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(f"Email '{email}' tidak valid! Harus mengandung '@'.")

class NoHPError(Exception):
    def __init__(self, nohp):
        self.nohp = nohp
        super().__init__(f"No HP '{nohp}' tidak valid! Harus 10-13 angka.")

def validasi_nama(nama):
    if len(nama.strip()) < 3:
        raise NamaError(nama)
    return nama

def validasi_umur(umur):
    if umur < 17 or umur > 60:
        raise UmurError(umur)
    return umur

def validasi_email(email):
    if "@" not in email:
        raise EmailError(email)
    return email

def validasi_nohp(nohp):
    if not nohp.isdigit() or len(nohp) < 10 or len(nohp) > 13:
        raise NoHPError(nohp)
    return nohp

print("=== REGISTRASI PESERTA SEMINAR ===")

while True:
    try:
        nama = input("Nama lengkap: ")
        nama = validasi_nama(nama)
        break
    except NamaError as e:
        print(f" [ERROR] {e}")

while True:
    try:
        input_umur = input("Umur: ")
        umur = int(input_umur)
        umur = validasi_umur(umur)
        break
    except ValueError:
        print(" [ERROR] Umur harus berupa angka!")
    except UmurError as e:
        print(f" [ERROR] {e}")

while True:
    try:
        email = input("Email: ")
        email = validasi_email(email)
        break
    except EmailError as e:
        print(f" [ERROR] {e}")
    
while True:
    try:
        nohp = input("No HP: ")
        nohp = validasi_nohp(nohp)
        break
    except NoHPError as e:
        print(f" [ERROR] {e}")

print("Proses input selesai.")

print("\n=== DATA PESERTA ===")
print(f"Nama    :", nama)
print(f"Umur    :", umur, "tahun")
print(f"Email   :", email)
print(f"No HP   :", nohp)
print("Status  : TERDAFTAR")
