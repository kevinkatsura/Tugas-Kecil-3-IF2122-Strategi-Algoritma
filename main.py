import tkinter
import API

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
button2 = tkinter.Button(window,text = " Cari Jarak " , command = API.API)

label2.grid(row=1,column=0)
entry2.grid(row=1,column = 1)
label3.grid(row=2,column=0)
entry3.grid(row=2,column=1)
button2.grid(row=2 ,column = 2)

window.mainloop()

