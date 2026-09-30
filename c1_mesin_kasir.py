total_buy = int(input("Total Belanja  : "))
money = int(input("Uang dibayar   : "))
kecukupan = total_buy<=money
kelebihan = (money - total_buy) * int(kecukupan)
kekurangan = total_buy > money
kekurangan_val = (total_buy - money) * int(kekurangan)

Rp100k = kelebihan // 100000
kembalian = kelebihan - (100000 * Rp100k)

Rp50k = kembalian // 50000
kembalian = kembalian - (50000 * Rp50k)

Rp20k = kembalian // 20000
kembalian = kembalian - (20000 * Rp20k)

Rp10k = kembalian // 10000
kembalian = kembalian - (10000 * Rp10k)

Rp5k = kembalian // 5000
kembalian = kembalian - (5000 * Rp5k)

Rp2k = kembalian // 2000
kembalian = kembalian - (2000 * Rp2k)

Rp1k = kembalian // 1000
kembalian = kembalian - (1000 * Rp1k)

Rp05k = kembalian // 500
kembalian = kembalian - (500 * Rp05k)

n_lembar = Rp100k + Rp50k + Rp20k + Rp10k + Rp5k + Rp2k + Rp1k + Rp05k


#print("Total belanja  : ",total_buy)
#print("Uang dibayar   : ",money)
print("Uang cukup     :",kecukupan)
print("Kekurangan     :",kekurangan_val)
print("Kembalian      :",kelebihan)
print("Rp100.000      :",Rp100k)
print("Rp50.000       :",Rp50k)
print("Rp20.000       :",Rp20k)
print("Rp10.000       :",Rp10k)
print("Rp5.000        :",Rp5k)
print("Rp2.000        :",Rp2k)
print("Rp1.000        :",Rp1k)
print("Rp500          :",Rp05k)
print("Total lembar/keping :",n_lembar)

#python3 mesin_kasir.py