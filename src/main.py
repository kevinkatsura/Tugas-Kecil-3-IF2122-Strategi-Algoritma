import tkinter
import Graph
import Astar
from tkinter import ttk

class GUI:
    def __init__(self):
        self.File = File()
        self.window = tkinter.Tk()
        self.window.title(" Bala-bala ")
        # First Row
        self.label1 = tkinter.Label(self.window, text="Nama File pada folder test")
        self.label1.grid(row = 0 , column = 0)
        self.entry1 = tkinter.Entry(self.window, bd =5)
        self.entry1.grid(row = 0 , column = 1)
        self.button1 = tkinter.Button(self.window,text = " open ")
        self.button1.grid(row = 0 , column = 2)

        # Origin
        self.label2 = tkinter.Label(self.window, text="Masukkan Posisi Asal")
        self.label3 = tkinter.Label(self.window, text="Masukkan Posisi Tujuan")
        self.entry2 = ttk.Combobox(self.window)
        self.entry3 = ttk.Combobox(self.window)
        self.button2 = tkinter.Button(self.window, text=" Cari Jarak ")
        self.label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        self.label3.grid(row=2, column=0)
        self.entry3.grid(row=2, column=1)
        self.button2.grid(row=2, column=2)
        self.label4 = tkinter.Label(self.window)
        self.label4.grid(row=3,column=0,columnspan=3)
        self.label5 = tkinter.Label(self.window)
        self.label5.grid(row=4,column=0,columnspan=3)
        self.label6 = tkinter.Label(self.window)
        self.label6.grid(row=5, column=0,columnspan = 3)
        self.label7 = tkinter.Label(self.window)
        self.label8 = tkinter.Label(self.window)
        self.label6["text"] = "Catatan : "
        self.label7.grid(row=6, column=0, columnspan=3)
        self.label7["text"] = "1. Catatan Jalur juga akan muncul di atas dari text ini setelah ditekan tombol Cari Jarak."
        self.label8.grid(row=7, column=0, columnspan=3)
        self.label8["text"] = "2. Nilai yang muncul pada GUI akan diupdate dari penggunaan sebelumnya jika visualisasi graph di close."


    def button1click(self,entry1Value):
        self.File.openFile(entry1Value)
        self.entry2["values"] = self.File.getSimpul()
        self.entry3["values"] = self.File.getSimpul()

    def button2click(self):
        if(self.entry2.get() == self.entry3.get()):
            self.label5["text"] = ""
            self.label4["text"] = " -- Tidak boleh menginput simpul yang sama -- "
        else:
            Jalur = Astar.AStar(self.File.infoSimpul, self.File.arrayKetetanggaan, self.entry2.get(), self.entry3.get(), len(self.File.infoSimpul))
            if(len(Jalur) == 2):
                self.label5["text"] = ""
                self.label4["text"] = " -- Tidak ditemukan jalur dengan algoritma A* -- "
            else:
                jalurInString = ""
                for i in range(len(Jalur)-1):
                    if(i == len(Jalur)-2):
                        jalurInString = jalurInString + Jalur[i]
                    else:
                        jalurInString = jalurInString + Jalur[i] + " -> "

                self.label5["text"] = "Total Jarak = " + Jalur[len(Jalur)-1]
                self.label4["text"] = jalurInString

                # Membentuk graph
                G = Graph.GraphVisualization()
                for i in (self.File.getEdge()):
                    index1 = 0
                    index2 = 0
                    while(i[0] != self.File.infoSimpul[index1][0]):
                        index1+=1
                    while (i[1] != self.File.infoSimpul[index2][0]):
                        index2 += 1
                    G.addEdge(i[0],i[1],self.File.arrayKetetanggaan[index1][index2])

                # Graph visualization
                G.visualize(jalur=Jalur)

class File:
    def __init__(self):
        # Buffer untuk isi file input
        self.arrayKetetanggaan = [] # matriks nxn, elemenij = "X" jika simpul i dan j tidak tetangga dan = sebuah nilai jika bertetangga
        self.infoSimpul = [] # matriks nx3, elemen pertama nama simpul, kedua dan ketiga koordinat x dan y

    def openFile(self,namaFile):
        t_file = open("../test/"+namaFile, "r")
        teks = t_file.readlines()
        t_file.close()
        indeks =0
        jumlah = -1
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
                self.infoSimpul.append(arr)
            else:
                temp =""
                arr=[]
                for karakter in baris:
                    if (karakter != " " and karakter != "\n"):
                        temp += karakter
                    elif (karakter == " " or karakter =="\n"):
                        arr.append(temp)
                        temp =""
                if(temp != ""):
                    arr.append(temp)
                self.arrayKetetanggaan.append(arr)
            indeks+=1

    def getSimpul(self):
        simpul = []
        for i in range(len(self.infoSimpul)):
            simpul.append(self.infoSimpul[i][0])
        return simpul

    def getEdge(self):
        Edge = []
        for i in range(len(self.arrayKetetanggaan)):
            for j in range(len(self.arrayKetetanggaan)):
                if(i != j):
                    if(self.arrayKetetanggaan[i][j] != "X"):
                        Edge.append((self.infoSimpul[i][0],self.infoSimpul[j][0]))
        return Edge

def main():
    root = GUI()
    root.button1["command"] = lambda: root.button1click(entry1Value=root.entry1.get())
    root.button2["command"] = root.button2click
    root.window.mainloop()

main()






