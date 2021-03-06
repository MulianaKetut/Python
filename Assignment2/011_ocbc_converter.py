def konversiSuhu(suhu):
    '''
    Doc:
    1. Mengubah input suhu ke tipe int
    2. Cek tipe suhu berdasarkan huruf yang di inputkan (sesuai ketentuan)
    3. Serta akan mengkonversi suhu tersebut (sesuai yang di input) ke tipe suhu yang lain.
    
    Fitur:
    1. Validasi input suhu & perulangan
    2. Question perulangan
    '''
    drjt = int(suhu[:-1])
    inputan = suhu[-1]

    if inputan.upper() == "C":
        hasil1 = float((9 * drjt) / 5 + 32)
        hasil2 = float(drjt + 273.15)
        hasil3 = float(4/5 * drjt)
        jenisX = "Celcius"
        jenis1 = "Fahrenheit"
        jenis2 = "Kelvin"
        jenis3 = "Reamur"
        print(drjt, jenisX, "=", "{:.1f}".format(hasil1), jenis1)
        print(drjt, jenisX, "=", "{:.1f}".format(hasil2), jenis2)
        print(drjt, jenisX, "=", "{:.1f}".format(hasil3), jenis3)

    elif inputan.upper() == "F":
        hasil1 = float((drjt - 32) * 5 / 9)
        hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
        hasil3 = float(4/9 * (drjt-32))
        jenisX = "Fahrenheit"
        jenis1 = "Celsius"
        jenis2 = "Kelvin"
        jenis3 = "Reamur"
        print(drjt, jenisX, "=", "{:.1f}".format(hasil1), jenis1)
        print(drjt, jenisX, "=", "{:.1f}".format(hasil2), jenis2)
        print(drjt, jenisX, "=", "{:.1f}".format(hasil3), jenis3)

    elif inputan.upper() == "K":
        hasil1 = float(drjt - 273.15)
        hasil2 = float(((drjt - 273.15) * 9 / 5)+32)
        hasil3 = float(4/5 * (drjt-273))
        jenisX = "Kelvin"
        jenis1 = "Celcius"
        jenis2 = "Fahrenheit"
        jenis3 = "Reamur"
        print(drjt, jenisX, "=", "{:.1f}".format(hasil1), jenis1)
        print(drjt, jenisX, "=", "{:.1f}".format(hasil2), jenis2)
        print(drjt, jenisX, "=", "{:.1f}".format(hasil3), jenis3)

    elif inputan.upper() == "R":
        hasil1 = float((5/4) * drjt)
        hasil2 = float((9/4 * drjt) + 32)
        hasil3 = float((5/4 * drjt) + 273)
        jenisX = "Reamur"
        jenis1 = "Celcius"
        jenis2 = "Fahrenheit"
        jenis3 = "Kelvin"
        print(drjt, jenisX, "=", "{:.1f}".format(hasil1), jenis1)
        print(drjt, jenisX, "=", "{:.1f}".format(hasil2), jenis2)
        print(drjt, jenisX, "=", "{:.1f}".format(hasil3), jenis3)

    else:
        print("Inputan tidak sesuai!! Perhatikan Penulisan Input")


i = True
print("\n===> Program Konversi Suhu - Python <===")
while i:
    try:
        print('C = Celcius', '\nF = Fahrenheit',
              '\nK = Kelvin', '\nR = Reamur')
        temp = input("\nMasukan suhu? (Misal: 30C, 20F, 21K, 44R): ")
        konversiSuhu(temp)
    except:
        print("Inputan tidak sesuai!! Perhatikan Penulisan Input")

    j = True
    while j:
        lagi = (input("\nHitung lagi? (y/n): "))
        if(lagi.lower() == 'y'):
            i = True
            j = False
        elif(lagi.lower() == 'n'):
            i = False
            j = False
        else:
            print("Inputan tidak sesuai!! Perhatikan Penulisan Input")
            j = True

print('\n===> Matur Thank You! <===')
