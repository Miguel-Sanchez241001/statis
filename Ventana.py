from tkinter import *
class Ventana:
    p1 = ""
    p2 = ""
    p3 = ""
    p4 = ""

    def __init__(self,p1, p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        raiz = Tk()
        raiz.title("Bootstrap")
        raiz.resizable(False, False)
        raiz.geometry("350x200")
        label0 = Label(text ="Intervalos de confianza por percentiles")
        label0.place(x=20,y = 20)
        label1 = Label(text=p1)
        label1.place(x=40, y=40)
        label2 = Label(text=p2)
        label2.place(x=80, y=40)
        label0 = Label(text="Intervalos de confianza por 95%")
        label0.place(x=20, y=60)
        label1 = Label(text=p3)
        label1.place(x=40, y=80)
        label1 = Label(text=p4)
        label1.place(x=80, y=80)
        raiz.mainloop()


