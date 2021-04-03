import math

def FindSimpul (infoSimpul, simpul):
    i = 0
    lokasi = -1
    found = False
    while (i <len(infoSimpul) and not found):
        if (CompareSimpul(infoSimpul[i][0], simpul)):
            found=True
            lokasi = i
        i+=1
    return lokasi


def CompareSimpul (simpul1, simpul2): 
    if (len(simpul1)==len(simpul2)):
        i = 0
        found = True
        while (i <len(simpul1) and found):
            if (simpul1[i]!=simpul2[i]):
                found=False
            i+=1
        return found
    else:
        return False


def BobotkeSimpulTujuan (infoSimpul, simpulTujuan):
    indeksTujuan = FindSimpul(infoSimpul, simpulTujuan)
    arrBobot = []
    for i in range(len(infoSimpul)):
        if(i == indeksTujuan):
            arrBobot.append(0)
        else:
            bobot = Bobot(infoSimpul, i, indeksTujuan)
            arrBobot.append(bobot)
    return arrBobot


def Bobot(infoSimpul, lokasi1, lokasi2):
    akar = ((float(infoSimpul[lokasi1][1]) - float(infoSimpul[lokasi2][1]))**2) + ((float(infoSimpul[lokasi1][2]) - float(infoSimpul[lokasi2][2]))**2)
    bobot = math.sqrt(akar)
    return bobot


def AStar (infoSimpul, arrayKetetanggaan, simpulAsal, simpulTujuan, jumlah):
    arrayBobot = BobotkeSimpulTujuan(infoSimpul, simpulTujuan)
    indeksTujuan = FindSimpul(infoSimpul, simpulTujuan)
    indeksAsal = FindSimpul(infoSimpul, simpulAsal)
    lokasiSekarang = indeksAsal
    found = False
    Jalur = []
    TotalJarak = 0
    Jalur.append(simpulAsal)
    while (not found):
        i = 0
        Hasil = 0
        CalonSimpulSelanjutnya = -1
        while (i<jumlah and not found):
            if(arrayKetetanggaan[lokasiSekarang][i].upper() != "X" and i==indeksTujuan):
                found = True
                CalonSimpulSelanjutnya = i
            elif (arrayKetetanggaan[lokasiSekarang][i].upper() != "X" and Hasil==0):
                Hasil = float(arrayKetetanggaan[lokasiSekarang][i]) + arrayBobot[i]
                CalonSimpulSelanjutnya = i
            elif (arrayKetetanggaan[lokasiSekarang][i].upper() != "X"):
                Hitungan = float(arrayKetetanggaan[lokasiSekarang][i]) + arrayBobot[i]
                if (Hitungan < Hasil):
                    Hasil = Hitungan
                    CalonSimpulSelanjutnya = i
            i+=1
        Jalur.append(infoSimpul[CalonSimpulSelanjutnya][0])
        TotalJarak += float(arrayKetetanggaan[lokasiSekarang][CalonSimpulSelanjutnya])
        lokasiSekarang = CalonSimpulSelanjutnya
    Jalur.append(str(TotalJarak))
    return Jalur

t_file = open("./test/file1.txt", "r")
teks=t_file.readlines()
t_file.close()
indeks =0
jumlah =-1
infoSimpul=[]                   #matriks nx3, elemen pertama nama simpul, kedua dan ketiga koordinat x dan y
arrayKetetanggaan = []          #matriks nxn, elemenij = "X" jika simpul i dan j tidak tetangga dan = sebuah nilai jika bertetangga
for baris in teks:
    if(indeks==0):
        jumlah = int(baris)
    elif (indeks <= jumlah):
        temp =""
        arr=[]
        for karakter in baris:
            if (karakter != " " and karakter != "\n"):
                temp += karakter
            elif (karakter == " " or karakter =="\n"):
                arr.append(temp)
                temp =""
        infoSimpul.append(arr)
    else:
        temp =""
        arr=[]
        for karakter in baris:
            if (karakter != " " and karakter != "\n"):
                temp += karakter
            elif (karakter == " " or karakter =="\n"):
                arr.append(temp)
                temp =""
        arrayKetetanggaan.append(arr)
    indeks+=1

Jalur = AStar(infoSimpul, arrayKetetanggaan, "A", "C", jumlah)
for i in Jalur:
    print(i)
