import tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import Graph

window = tkinter.Tk()
window.title(" Bala-bala ")

# First Row
label1 = tkinter.Label(window, text="Nama File")
label1.grid(row = 0 , column = 0)
entry1 = tkinter.Entry(window, bd =5)
entry1.grid(row = 0 , column = 1)
button1 = tkinter.Button(window,text = " open ")
button1.grid(row = 0 , column = 2)

# Origin
label2 = tkinter.Label(window,text = "Masukkan Posisi Asal")
label3 = tkinter.Label(window,text = "Masukkan Posisi Tujuan")
entry2 = tkinter.Entry(window, bd = 5)
entry3 = tkinter.Entry(window, bd = 5)
button2 = tkinter.Button(window,text = " Cari Jarak ")

label2.grid(row=1,column=0)
entry2.grid(row=1,column = 1)
label3.grid(row=2,column=0)
entry3.grid(row=2,column=1)
button2.grid(row=2 ,column = 2)

# Graph visualization
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


# Driver code
G = Graph.GraphVisualization()
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(1, 0)
G.visualize()

canvas = FigureCanvasTkAgg(f,G)
canvas.show()
canvas.get_tk_widget().grid(row=3 , column = 0, fill = tkinter.BOTH, expand = True)

window.mainloop()

