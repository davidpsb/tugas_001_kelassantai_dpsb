epsilon = 1e-9 #mencegah 79.9999999

tugas            = float(input("Nilai Tugas         : "))
uts              = float(input("Nilai UTS           : "))
uas              = float(input("Nilai UAS           : "))
kehadiran_persen = float(input("Kehadiran (%)       : "))
kehadiran        = kehadiran_persen/100
penghasilan      = int(input("Penghasilan Orang Tua : "))
n_sertif         = int(input("Jumlah Sertifikat     : "))

nilai_akhir = (20*tugas + 35*uts + 45*uas) / 100
valid_nilai_akhir = nilai_akhir >= 80 - epsilon
valid_hadir = kehadiran >= 0.85
valid_ass_2 = tugas >=65 and uts >=65 and uas >=65
valid_ass_3 = penghasilan < 4000000 or n_sertif >= 2

layak = (valid_nilai_akhir == True) and (valid_hadir == True) and (valid_ass_2 == True) and (valid_ass_3 == True) 
alasan = "Nilai Akhir dibawah 80 "*(not valid_nilai_akhir) , " Kehadiran Kurang dari 85%"* (not valid_hadir), " Nilai Tugas, UTS, UTS ada yang dibawah 75" * (not valid_ass_2), " Pebghasilan Orangtua diatas 4000000 atau Jumlah Sertifikat dibawah 2"* (not valid_ass_3)

input_tugas_valid = (((tugas*10) - int((tugas*10))) < epsilon) or ((int((tugas*10)) + 1 - (tugas*10)) < epsilon)
input_uts_valid = (((uts*10) - int((uts*10))) < epsilon) or ((int((uts*10)) + 1 - (uts*10)) < epsilon)
input_uas_valid = (((uas*10) - int((uas*10))) < epsilon) or ((int((uas*10)) + 1 - (uas*10)) < epsilon)
input_kehadiran_valid = (((kehadiran_persen*10) - int(kehadiran_persen*10)) < epsilon) or ((int(kehadiran_persen*10) + 1 - kehadiran_persen*10) < epsilon)

input_valid = (input_tugas_valid == True) and (input_uts_valid == True) and (input_uas_valid == True) and (input_kehadiran_valid == True)


print("Nilai Akhir        :",nilai_akhir)
print("Input Valid        :", input_valid)
print("Status             :",("Tidak" * (not layak) + " Layak"))
print("Alasan Tidak Layak :",alasan)


#python3 c4_beasiswa.py