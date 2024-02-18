import datetime 

Tanggal = int(input("Masukan Tanggal Lahir :"))
Bulan = int(input("Masukan Bulan Lahir :"))
Tahun = int(input("Masukan Tahun Lahir :"))

Sekarang = datetime.date.today()
Lahir = datetime.date(Tahun, Bulan, Tanggal)
Umur = Sekarang - Lahir 
Tahun = Umur.days // 365
Bulan = (Umur.days % 365) // 30
Tanggal = (Umur.days % 365) % 30

print(f"umur anda : {Tahun} Tahun, {Bulan} Bulan, {Tanggal} Hari")


