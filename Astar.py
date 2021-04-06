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
    arrayOfIndeks = []
    arrayOfIndeks.append(indeksAsal)
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
            elif (arrayKetetanggaan[lokasiSekarang][i].upper() != "X" and Hasil==0 and i not in arrayOfIndeks):
                Hasil = float(arrayKetetanggaan[lokasiSekarang][i]) + arrayBobot[i]
                CalonSimpulSelanjutnya = i
            elif (arrayKetetanggaan[lokasiSekarang][i].upper() != "X" and i not in arrayOfIndeks):
                Hitungan = float(arrayKetetanggaan[lokasiSekarang][i]) + arrayBobot[i]
                if (Hitungan < Hasil):
                    Hasil = Hitungan
                    CalonSimpulSelanjutnya = i
            i+=1
        if (CalonSimpulSelanjutnya == -1):      #stak, gak didapat jalur melalui AStar
            Jalur = ["not_found"]
            found = True
            break
        arrayOfIndeks.append(CalonSimpulSelanjutnya)
        Jalur.append(infoSimpul[CalonSimpulSelanjutnya][0])
        print(infoSimpul[CalonSimpulSelanjutnya][0])
        TotalJarak += float(arrayKetetanggaan[lokasiSekarang][CalonSimpulSelanjutnya])
        lokasiSekarang = CalonSimpulSelanjutnya
    Jalur.append(str(TotalJarak))
    return Jalur



