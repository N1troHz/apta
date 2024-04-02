print("## PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA ##")
print("=============================================")
print()

def hitungLuasSegitiga(a,t):
    return round(0.5 * a * t,2)

alas = float(input("Input Alas Segitiga"))
tinggi = float(input("Input Tinggi Segitiga"))

print('Luas Segitiga = ', hitungLuasSegitiga(alas,tinggi))
print()