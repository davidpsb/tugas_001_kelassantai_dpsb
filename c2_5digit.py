num = float(input("Masukkan bilangan 5 digit :"))
digit = 1 + (num >= 10) + (num >= 100) + (num >= 1000) + (num >= 10000) + (num >= 100000) + (num >= 1000000) + (num >= 10000000) + (num >= 100000000) 
valid = digit % 5 == 0

d1 = num % 10
d2 = num // 10 % 10
d3 = num // 100 % 10
d4 = num // 1000 % 10
d5 = num // 10000 % 10
d6 = num // 100000 % 10
d7 = num // 1000000 % 10
d8 = num // 10000000 % 10
penjumlahan_num = int(d1+d2+d3+d4+d5+d6+d7+d8)

n_genap = (
    (d1 % 2 == 0) * (digit >= 1) +
    (d2 % 2 == 0) * (digit >= 2) +
    (d3 % 2 == 0) * (digit >= 3) +
    (d4 % 2 == 0) * (digit >= 4) +
    (d5 % 2 == 0) * (digit >= 5) +
    (d6 % 2 == 0) * (digit >= 6) +
    (d7 % 2 == 0) * (digit >= 7) +
    (d8 % 2 == 0) * (digit >= 8)
)

terbalik = (
    (d1*10000000*int(d1>0)) + (d2*1000000*int(d2>0)) + 
    (d3*100000*int(d3>0)) + (d4*10000*int(d4>0)) + 
    (d5*1000*int(d5>0)) + (d6*100*int(d6>0)) + 
    (d7*10*int(d7>0)) + (d8*int(d8>0))
)

terbalik = terbalik / (10**(8-digit))

palindrom = terbalik == num

harshad = (num % penjumlahan_num) == 0

print("Input valid        :",valid)
print("Jumlah digit       :",penjumlahan_num)
print("Banyak digit genap :",n_genap)
print("Bilangan terbalik  :",int(terbalik))
print("Palindrom          :",palindrom)
print("Bilangan Harshad   :",harshad)


#python3 c2_5digit.py