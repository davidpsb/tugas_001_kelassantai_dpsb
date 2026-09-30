jam_masuk = int(input("Jam Masuk :"))
menit_masuk = int(input("Menit masuk :"))
jam_keluar = int(input("Jam Keluar :"))
menit_keluar = int(input("Menit Keluar :"))

point_masuk = jam_masuk*60 + menit_masuk
point_keluar = jam_keluar*60 + menit_keluar
nginep = point_masuk > point_keluar

nginep_delta = (24%jam_masuk)*60 - ((60-menit_masuk)*(not (menit_masuk==0))) + point_keluar
point_delta = ((point_keluar - point_masuk)*int( not nginep)) + ((nginep_delta)*int(nginep))


jam_delta = point_delta//60
menit_delta =  point_delta - (jam_delta*60)
pas_bgt =  (jam_delta > 1) and (menit_delta == 0)
jam_ditagih = ((int(point_delta/60) + 1)* (not pas_bgt)) + ((int(point_delta/60))* (pas_bgt))

total_tarif = (3000 + ((jam_ditagih-1)*2000))

print(f"Lama Parkir : {jam_delta} Jam {menit_delta} Menit")
print(f"Jam Ditagih : {jam_ditagih}")
print(f"Total Tarif : Rp.{total_tarif}")

#python c5_parkir.py

