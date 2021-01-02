def luasPersegi():
    print("Rumus luas dari bangun persegi ")
    print("Rumusnya = sisi x sisi")
    sisi = int(input("sisi : "))
    i = 0
    while i < 1:
        sisi *= sisi
        i += 1
    return sisi
def kelilingPersegi():
    print("Rumus keliling dari bangun persegi ")
    print("Rumusnya = sisi + sisi + sisi + sisi")
    sisi = int(input("sisi : "))
    i = 0
    while i < 2:
        sisi += sisi
        i += 1

    return sisi

def luasPersegiPanjang():
    print("Rumus luas dari bangun persegi panjang ")
    print("Rumusnya = panjang x lebar")
    p = int(input("panjang : "))
    l = int(input("lebar : "))
    luas = p * l

    return luas
def kelilingPersegiPanjang():
    print("Rumus keliling dari bangun persegi panjang ")
    print("Rumusnya = 2 x (panjang + lebar)")
    p = int(input("panjang: "))
    l = int(input("lebar : "))
    keliling = 2 * (p + l)

    return keliling

def luasLingkaran():
    print("Rumus luas dari bangun lingkaran ")
    print("Rumusnya = phi x r x r")
    phi = 3.14
    r = float(input("r : "))
    i = 0
    while i < 1:
        r *= r
        i += 1
    luas = phi * r

    return luas
def kelilingLingkaran():
    print("Rumus keliling dari bangun lingkaran ")
    print("Rumusnya = 2 x phi x r")
    phi = 3.14
    r = float(input("r : "))
    keliling = 2 * phi * r

    return keliling

def luasSegitiga():
    print("Rumus luas dari bangun segitiga ")
    print("Rumusnya = 1/2 x alas x tinggi")
    alas = int(input("alas : "))
    tinggi = int(input("tinggi : "))
    luas = (alas * tinggi) / 2

    return luas
def kelilingSegitiga():
    print("Rumus keliling dari bangun segitiga ")
    print("Sisi ke-1 (a)")
    print("Sisi ke-2 (b)")
    print("Sisi ke-3 (c)")
    print("Rumusnya = a + b + c")
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("b : "))
    keliling = (a + b + c)

    return keliling

def luasTrapesium():
    print("Rumus luas dari bangun trapesium ")
    print("Rumusnya = 1/2 x (atas + bawah) x tinggi")
    a = int(input("atas : "))
    b = int(input("bawah : "))
    t = int(input("tinggi : "))
    luas = ((a + b) * t) / 2

    return luas
def kelilingTrapesium():
    print("Rumus luas dari bangun trapesium ")
    print("Sisi ke-1 (ab)")
    print("Sisi ke-2 (bc)")
    print("Sisi ke-3 (cd)")
    print("Sisi ke-4 (da)")
    print("Rumusnya = ab + bc + cd + da")
    a = int(input("ab : "))
    b = int(input("bc : "))
    c = int(input("cd : "))
    d = int(input("da : "))
    keliling = a + b + c + d

    return keliling

def volumeKubus():
    print("Rumus volume dari kubus ")
    print("Rumusnya = sisi x sisi x sisi")
    sisi = int(input("sisi : "))
    i = 0
    while i < 1:
        sisi **= 3
        i += 1

    return sisi
def lpKubus():
    print("Rumus luas permukaan dari bangun kubus")
    print("Rumusnya = 6 x luas persegi")
    print("         = 6 x sisi x sisi")
    lp = 6 * luasPersegi()

    return lp

def volumeBalok():
    print("Rumus volume dari balok ")
    print("Rumusnya = luas persegi panjang x tinggi")
    print("         = panjang x lebar x tinggi")
    t = int(input("tinggi  : "))
    volume = luasPersegiPanjang() * t

    return volume
def lpBalok():
    print("Rumus luas permukaan dari balok ")
    print("Rumusnya = 2 x ((p x l) + (p x t) + (l x t))")
    p = int(input("panjang : "))
    l = int(input("lebar   : "))
    t = int(input("tinggi  : "))
    lp = (2 * ((p * l) + (p * t) + (l * t)))

    return lp

def volumeBola():
    print("Rumus volume dari bola")
    print("Rumusnya = 4/3 x phi x r x r x r")
    phi = 3.14
    r = float(input("r : "))
    i = 0
    while i < 1:
        r **= 3
        i += 1
    volume = 4/3 * phi * r

    return volume
def lpBola():
    print("Rumus luas permukaan dari bola ")
    print("Rumusnya = 4 x luas lingkaran")
    print("         = 4 x phi x r x r")
    lp = luasLingkaran() * 4

    return lp

def volumeKerucut():
    print("Rumus volume dari bangun kerucut ")
    print("Rumusnya = 1/3 x luas lingkaran x tinggi")
    print("         = 1/3 x phi x r x r x tinggi")
    t = float(input("tinggi : "))
    volume = (luasLingkaran() * t )/ 3

    return volume
def lpKerucut():
    print("Rumus luas permukaan dari kerucut ")
    print("Rumusnya = phi x r x (r + s)")
    phi = 3.14
    r = float(input("r : "))
    s = float(input("s : "))
    lp = phi * r * (r + s)

    return lp

def volumeTabung():
    print("Rumus volume dari tabung ")
    print("Rumusnya = luas lingkaran x tinggi")
    print("         = phi x r x r x tinggi")
    t = int(input("tinggi : "))
    volume = luasLingkaran() * t

    return volume
def lpTabung():
    print("Rumus luas permukaan dari tabung ")
    print("Rumusnya = keliling lingkaran x (r + tinggi)")
    print("         = 2 x phi x r x (r + tinggi)")
    r = int(input("r : "))
    t = int(input("tinggi : "))
    lp = (kelilingLingkaran() * (r + t))

    return lp

print("")
print("|| PROGRAM RUMUS BANGUN DATAR DAN BANGUN RUANG ||")
print("Program ini menampilkan rumus-rumus dari bangun datar dan bangun ruang.")
print("Isi dari bangun datar yaitu ada bangun persegi, persegi panjang, lingkaran, segitiga, dan trapesium.")
print("Sementara isi bangun ruang yaitu ada kubus, balok, bola, kerucut, dan tabung.")
print("Keduanya akan diminta menginputkan angka yang ingin dicari hasilnya")
print("")
print("Demikian penjelasan singkat ini.")
print("")
print("Press Enter to Continue]. . .")
a = str(input())
print("++========================================++")
print("||  PILIH MENU YANG INGIN ANDA TAMPILKAN  ||")
print("||  ** APLIKASI HITUNG RUMUS GEOMETRI **  ||")
print("++========================================++")
print("   ")
print("+=====+====================================+")
print("|  1  |     BANGUN DATAR                   |")
print("+=====+====================================+")
print("|  2  |     BANGUN RUANG                   |")
print("+=====+====================================+")
pil = str(input(" PILIH MENU : "))
while (pil != "0"):
    if (pil == "1"):
        print(" ")
        print("PILIH BANGUN DATAR : ")
        print("+-----+------------------------------+")
        print("|  1  |     PERSEGI                  |")
        print("+-----+------------------------------+")
        print("|  2  |     PERSEGI PANJANG          |")
        print("+-----+------------------------------+")
        print("|  3  |     LINGKARAN                |")
        print("+-----+------------------------------+")
        print("|  4  |     SEGITIGA                 |")
        print("+-----+------------------------------+")
        print("|  5  |     TRAPESIUM                |")
        print("+-----+------------------------------+")
        pil1 = str(input(" PILIH BANGUN DATAR : "))
        while (pil1 != "0"):
            if (pil1 == "1"):
                print(" ")
                print("PILIH RUMUS PERSEGI : ")
                print("+--------------------------------+")
                print("|  1.   LUAS PERSEGI             |")
                print("|--------------------------------|")
                print("|  2.   KELILING PERSEGI         |")
                print("+--------------------------------+")   
                pil2 = str(input(" PILIH RUMUS : ")) 
                while (pil2 != "0"):
                    if (pil2 == "1"):
                        print("hasil : ", luasPersegi())
                        print(" ")
                    elif (pil2 == "2"):
                        print("hasil : ", kelilingPersegi())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil2 = str(input(" PILIH RUMUS : "))
            elif (pil1 == "2"):
                print(" ")
                print("PILIH RUMUS PERSEGI PANJANG : ")
                print("+--------------------------------+")
                print("|  1.   LUAS PERSEGI PANJANG     |")
                print("|--------------------------------|")
                print("|  2.   KELILING PERSEGI PANJANG |")
                print("+--------------------------------+") 
                pil3 = str(input(" PILIH RUMUS : "))     
                while (pil3 != "0"):
                    if (pil3 == "1"):
                        print("hasil : ", luasPersegiPanjang())
                        print(" ")
                    elif (pil3 == "2"):
                        print("hasil : ", kelilingPersegiPanjang())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil3 = str(input(" PILIH RUMUS : "))
            elif (pil1 == "3"):
                print(" ")
                print("PILIH RUMUS LINGKARAN : ")
                print("+--------------------------------+")
                print("|  1.   LUAS LINGKARAN           |")
                print("|--------------------------------|")
                print("|  2.   KELILING LINGKARAN       |")
                print("+--------------------------------+") 
                pil4 = str(input(" PILIH RUMUS : "))     
                while (pil4 != "0"):
                    if (pil4 == "1"):
                        print("hasil : ", luasLingkaran())
                        print(" ")
                    elif (pil4 == "2"):
                        print("hasil : ", kelilingLingkaran())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil4 = str(input(" PILIH RUMUS : "))
            elif (pil1 == "4"):
                print(" ")
                print("PILIH RUMUS SEGITIGA : ")
                print("+--------------------------------+")
                print("|  1.   LUAS SEGITIGA            |")
                print("|--------------------------------|")
                print("|  2.   KELILING SEGITIGA        |")
                print("+--------------------------------+")  
                pil5 = str(input(" PILIH RUMUS : "))     
                while (pil5 != "0"):
                    if (pil5 == "1"):
                        print("hasil : ", luasSegitiga())
                        print(" ")
                    elif (pil5 == "2"):
                        print("hasil : ", kelilingSegitiga())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil5 = str(input(" PILIH RUMUS : "))
            elif (pil1 == "5"):
                print(" ")
                print("PILIH RUMUS TRAPESIUM : ")
                print("+--------------------------------+")
                print("|  1.   LUAS TRAPESIUM           |")
                print("|--------------------------------|")
                print("|  2.   KELILING TRAPESIUM       |")
                print("+--------------------------------+") 
                pil6 = str(input(" PILIH RUMUS : "))     
                while (pil6 != "0"):
                    if (pil6 == "1"):
                        print("hasil : ", luasTrapesium())
                        print(" ")
                    elif (pil6 == "2"):
                        print("hasil : ", kelilingTrapesium())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil6 = str(input(" PILIH RUMUS : "))
            else:
                print("INPUTAN TIDAK VALID !!")
            pil1 = str(input(" PILIH BANGUN DATAR : "))
    if (pil == "2"):
        print(" ")
        print("PILIH BANGUN RUANG : ")
        print("+-----+------------------------------+")
        print("|  1  |     KUBUS                    |")
        print("+-----+------------------------------+")
        print("|  2  |     BALOK                    |")
        print("+-----+------------------------------+")
        print("|  3  |     BOLA                     |")
        print("+-----+------------------------------+")
        print("|  4  |     KERUCUT                  |")
        print("+-----+------------------------------+")
        print("|  5  |     TABUNG                   |")
        print("+-----+------------------------------+")
        pil1 = str(input(" PILIH BANGUN RUANG : "))
        while (pil1 != "0"):
            if (pil1 == "1"):
                print(" ")
                print("PILIH RUMUS KUBUS : ")
                print("+--------------------------------+")
                print("|  1.   VOLUME KUBUS             |")
                print("|--------------------------------|")
                print("|  2.   LUAS PERMUKAAN KUBUS     |")
                print("+--------------------------------+")    
                pil2 = str(input(" PILIH RUMUS : ")) 
                while (pil2 != "0"):
                    if (pil2 == "1"):
                        print("hasil : ", volumeKubus())
                        print(" ")
                    elif (pil2 == "2"):
                        print("hasil : ", lpKubus())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil2 = str(input(" PILIH RUMUS : "))
            elif (pil1 == "2"):
                print(" ")
                print("PILIH RUMUS BALOK : ")
                print("+--------------------------------+")
                print("|  1.   VOLUME BALOK             |")
                print("|--------------------------------|")
                print("|  2.   LUAS PERMUKAAN BALOK     |")
                print("+--------------------------------+")    
                pil3 = str(input(" PILIH RUMUS : "))     
                while (pil3 != "0"):
                    if (pil3 == "1"):
                        print("hasil : ", volumeBalok())
                        print(" ")
                    elif (pil3 == "2"):
                        print("hasil : ", lpBalok())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil3 = str(input(" PILIH RUMUS : "))
            elif (pil1 == "3"):
                print(" ")
                print("PILIH RUMUS BOLA : ")
                print("+--------------------------------+")
                print("|  1.   VOLUME BOLA              |")
                print("|--------------------------------|")
                print("|  2.   LUAS PERMUKAAN BOLA      |")
                print("+--------------------------------+")   
                pil4 = str(input(" PILIH RUMUS : "))     
                while (pil4 != "0"):
                    if (pil4 == "1"):
                        print("hasil : ", volumeBola())
                        print(" ")
                    elif (pil4 == "2"):
                        print("hasil : ", lpBola())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil4 = str(input(" PILIH RUMUS : "))
            elif (pil1 == "4"):
                print(" ")
                print("PILIH RUMUS KERUCUT : ")
                print("+--------------------------------+")
                print("|  1.   VOLUME KERUCUT           |")
                print("|--------------------------------|")
                print("|  2.   LUAS PERMUKAAN KERUCUT   |")
                print("+--------------------------------+")   
                pil5 = str(input(" PILIH RUMUS : "))     
                while (pil5 != "0"):
                    if (pil5 == "1"):
                        print("hasil : ", volumeKerucut())
                        print(" ")
                    elif (pil5 == "2"):
                        print("hasil : ", lpKerucut())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil5 = str(input(" PILIH RUMUS : "))
            elif (pil1 == "5"):
                print(" ")
                print("PILIH RUMUS TABUNG : ")
                print("+--------------------------------+")
                print("|  1.   VOLUME TABUNG            |")
                print("|--------------------------------|")
                print("|  2.   LUAS PERMUKAAN TABUNG    |")
                print("+--------------------------------+")    
                pil6 = str(input(" PILIH RUMUS : "))     
                while (pil6 != "0"):
                    if (pil6 == "1"):
                        print("hasil : ", volumeTabung())
                        print(" ")
                    elif (pil6 == "2"):
                        print("hasil : ", lpTabung())
                        print(" ")
                        break
                    else:
                        print("INPUTAN TIDAK VALID !!")
                    pil6 = str(input(" PILIH RUMUS : "))
            else:
                print("INPUTAN TIDAK VALID !!")
            pil1 = str(input(" PILIH BANGUN RUANG : "))
    else:
        print("INPUTAN TIDAK VALID !!")
    pil = str(input(" PILIH MENU : "))
            
print("Ditya Ilmi Rizqi")
print("1303191119")