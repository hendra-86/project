print("Kalkulator Desimal, Biner, Oktal, dan Heksadesimal")
print("1. Desimal ke Biner, Oktal, Heksa")
print("2. Biner ke Desimal, Oktal, Heksa")
print("3. Oktal ke Desimal, Biner, Heksa")
print("4. Heksa ke Desimal, Biner, Oktal")
print("======================================================")
pil = input("Masukkan Pilihan = ")
if pil=="1":
            print("Kalkulator Desimal ke Biner, oktal, heksa")
            nilai_input = input("Masukkan Nilai = ")
            nilai = int(nilai_input)
            biner = bin(nilai)[2:]
            oktal = oct(nilai)[2:]
            heksa = hex(nilai)[2:].upper()
            print("Hasil dari bil. Desimal = ",nilai)
            print("Biner = ",biner)
            print("Oktal = ",oktal)
            print("Heksadesimal = ",heksa)
        
elif pil=="2":
            print("Kalkulator Biner ke Desimal, Oktal, Heksa")
            nilai = input("Masukkan Nilai = ")
            biner = str(nilai)
            desimal = int(biner,2)
            oktal = oct(desimal)[2:]
            heksa = hex(desimal)[2:].upper()
            print("Hasil dari bil. Biner = ",nilai)
            print("Desimal = ",desimal)
            print("Oktal = ",oktal)
            print("Heksadesimal = ",heksa)
        
elif pil=="3":
            print("Kalkulator Oktal ke Desimal, Biner, Heksa")
            nilai = input("Masukkan Nilai = ")
            oktal = str(nilai)
            desimal = int(nilai,8)
            biner = bin(desimal)[2:]
            heksa = hex(desimal)[2:].upper()
            print("Hasil dari bil. Oktal = ",nilai)
            print("Desimal = ",desimal)
            print("Biner = ",biner)
            print("Heksadesimal = ",heksa)
        
elif pil=="4":
            print("Kalkulator Heksa ke Desimal, Biner, Oktal")
            nilai = input("Masukkan Nilai = ")
            heksa = nilai
            desimal = int(heksa,16)
            biner = bin(desimal)[2:]
            oktal = oct(desimal)[2:]
            print("Hasil dari bil. Heksadesimal = ",nilai)
            print("Desimal = ",desimal)
            print("Biner = ",biner)
            print("Oktal = ",oktal)
        
else:
    print("masukkan pilihan yang tepat")