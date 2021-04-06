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

        # MAP
        # frame = HtmlFrame(self.window,horizontal_scrollbar="auto")
        # frame.set_content(urllib.request.urlopen("https://www.google.com/maps/@2.6016679,98.7044794,18.94z").read().decode())

    def button1click(self,entry1Value):
        self.File.openFile(entry1Value)
        self.entry2["values"] = self.File.getSimpul()
        self.entry3["values"] = self.File.getSimpul()

    def button2click(self):
        Jalur = Astar.AStar(self.File.infoSimpul, self.File.arrayKetetanggaan, self.entry2.get(), self.entry3.get(), len(self.File.infoSimpul))
        print(Jalur)

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

    def jalur (self):
        Jalur = Astar.AStar(self.File.infoSimpul, self.File.arrayKetetanggaan, self.entry2.get(), self.entry3.get(),
                            len(self.File.infoSimpul))
        print(Jalur)
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

    def tampilkan(self):
        print(self.arrayKetetanggaan)
        print(self.infoSimpul)
        print(len(self.infoSimpul))
        print(self.getEdge())
        print(self.getEdge()[0][0])

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






