print("## PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA ##")
print("=============================================")
print()

def hitungLuasSegitiga(a,t):
    return round(0.5 * a * t,2)

alas = float(input("Input Alas Segitiga : "))
tinggi = float(input("Input Tinggi Segitiga : "))

print('Luas Segitiga = ', hitungLuasSegitiga(alas,tinggi))
print()

print("## PROGRAM PYTHON MENGHITUNG PANJANG PERSEGI ##")
print("=============================================")
print()

def hitungPersegiPanjang(p,l):
    return round(p * l,2)

panjang = float(input('Input Panjang : '))
lebar = float(input('Input Lebar : '))
print('Luas Persegi Panjang = ',hitungPersegiPanjang(panjang,lebar))


