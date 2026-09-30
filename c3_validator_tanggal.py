tanggal = int(input("Tanggal         : "))
bulan = int(input("Bulan           : "))
tahun = int(input("Tahun           : "))


tahun_kabisat = (tahun % 4 == 0) and (tahun % 100 != 0) or (tahun % 400 == 0)

aa = 31 * (bulan==1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12)
bb = 30 * (bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11)
cc = 28 * (bulan ==2 and (tahun_kabisat==False))
dd = 29 * (bulan ==2 and (tahun_kabisat==True))
jumlah_hari = aa + bb + cc + dd

date_valid = tanggal <= jumlah_hari

print("Tahun Kabisat   :", tahun_kabisat)
print("Jumlah Hari     :", jumlah_hari)
print("Tanggal Valid   :", date_valid)


#python3 c3_validator_tanggal.py