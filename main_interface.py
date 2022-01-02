from tkinter import *

app = Tk()

class funcs():
    def limpar_tela(self):
        self.entry_numero.delete(0, END)

class Aplicativo(funcs):
    def __init__(self):
        self.app = app
        self.tela()
        self.widgets()
        app.mainloop()
    def tela(self):
        self.app.title("Tabuada")
        self.app.geometry("255x300")
        self.app.configure(background="#dfe3ee")
        self.app.resizable(width=False, height=False)

    def widgets(self):
        #Criação dos botões.
        self.bt_calcular = Button(self.app, text="Calcular", background="#187db2",)
        self.bt_calcular.place(x=100, y=55)
        self.bt_limpar = Button(self.app, text="Limpar", background="#187db2", command=self.limpar_tela)
        self.bt_limpar.place(x=200, y=270)
        #Criação das label.
        self.lb_numero = Label(self.app, text="Informe um número para saber sua tabuada", font=("arial", 9), background="#dfe3ee", foreground="#187db2").place(x=3, y=3, width=250, height=30)
        #Criação de entry.
        self.entry_numero = Entry(self.app)
        self.entry_numero.place(x=100, y=28, width=55)

Aplicativo()
