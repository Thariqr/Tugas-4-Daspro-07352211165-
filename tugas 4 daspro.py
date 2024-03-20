def konversi_angka(angka):
    desimal = int(angka)
    
    biner = bin(desimal)
    
    oktal = oct(desimal)
    
    heksadesimal = hex(desimal)
    
    return biner, oktal, desimal, heksadesimal

angka = input("Masukkan angka: ")

hasil_biner, hasil_oktal, hasil_desimal, hasil_heksadesimal = konversi_angka(angka)

print("Biner:", hasil_biner)
print("Oktal:", hasil_oktal)
print("Desimal:", hasil_desimal)
print("Heksadesimal:", hasil_heksadesimal)