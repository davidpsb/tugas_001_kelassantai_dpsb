a = int(input("Bilangan 1: "))
b = int(input("Bilangan 2: "))
c = int(input("Bilangan 3: "))

# Cari terkecil
x = (a * (a <= b) * (a <= c)) + (b * (b < a) * (b <= c)) + (c * (c < a) * (c < b))
x = int(x)

# Cari terbesar
z = (a * (a >= b) * (a >= c)) + (b * (b > a) * (b >= c)) + (c * (c > a) * (c > b))
z = int(z)

# Tengah = total - terkecil - terbesar
y = a + b + c - x - z
y= int(y)


selisih1 = y - x
selisih2 = z - y
aritmetika = selisih1 == selisih2


print(f"Terkecil : {x}")
print(f"Tengah : {y}")
print(f"Terbesar : {z}")
print(f"Barisan aritmetika : {aritmetika}")

# python3 c6_mengurutkan.py