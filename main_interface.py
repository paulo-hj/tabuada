from tkinter import *
from tkinter import messagebox

class Funcs():
    def limpar_tela(self):
        self.entry_numero.delete(0, END)
        self.lb_1.destroy() 
        self.widgets()
    def calcular(self):
        try:
            self.n1 = int(self.entry_numero.get())
            self.lb_1["text"] = """{} X {} = {}\n  {} X {} = {}\n  {} X {} = {}
  {} X {} = {}\n  {} X {} = {}\n  {} X {} = {}\n  {} X {} = {}
  {} X {} = {}\n  {} X {} = {}\n    {} X {} = {}""".format(self.n1, 1, (self.n1 * 1),
            self.n1, 2, (self.n1 * 2), self.n1, 3, (self.n1 * 3), self.n1, 4, (self.n1 * 4),
            self.n1, 5, (self.n1 * 5), self.n1, 6, (self.n1 * 6), self.n1, 7, (self.n1 * 7),
            self.n1, 8, (self.n1 * 8), self.n1, 9, (self.n1 * 9), self.n1, 10, (self.n1 * 10))
        except ValueError:
            messagebox.showerror(title="Erro", message="Digite somente números inteiros.")
        
class Aplicativo(Funcs):
    def __init__(self):
        app = Tk()
        self.app = app
        self.tela()
        self.frames()
        self.widgets()
        app.mainloop()
    def tela(self):
        self.app.title("Tabuada")
        self.app.geometry("255x300+547+200")
        self.app.configure(background="#dfe3ee")
        self.app.resizable(width=False, height=False)
    def frames(self):
        self.frame_1 = Frame(self.app, borderwidth=2, relief="solid", background="#dfe3ee")
        self.frame_1.place(x=3 , y=3, width=249 , height= 83)
        self.frame_2 = Frame(self.app, borderwidth=2, relief="solid", background="#dfe3ee")
        self.frame_2.place(x=3 , y=90, width=249 , height= 207)
    def widgets(self):
        #Criação dos botões.
        self.bt_calcular = Button(self.frame_1, text="Calcular", background="#187db2", command=self.calcular)
        self.bt_calcular.place(x=100, y=50)
        self.bt_limpar = Button(self.frame_2, text="Limpar", background="#187db2", command=self.limpar_tela)
        self.bt_limpar.place(x=195, y=175)
        #Criação das label.
        self.lb_mensagem = Label(self.frame_1, text="Informe um número", font=("arial", 8, "bold"),
        background="#dfe3ee", foreground="#187db2")
        self.lb_mensagem.place(x=54, y=0, width=150, height=30)
        self.lb_1 = Label(self.frame_2, text="", background="#dfe3ee", foreground="#187db2",
        font=("arial", 12, "bold"), anchor=W)
        self.lb_1.place(x=1, y=10, width=150, height=185)
        #Criação de entry.
        self.entry_numero = Entry(self.frame_1)
        self.entry_numero.place(x=100, y=28, width=55)

Aplicativo()