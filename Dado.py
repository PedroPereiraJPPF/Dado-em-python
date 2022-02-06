from distutils import command
from tkinter import *
import random
from turtle import bgcolor


def dado():
    a = random.randint(1, 6)
    result["text"] = a


tela = Tk()
tela.title("Dados")

texto = Label(tela, text='Este é um dado simulado')
texto.grid(column=0, row=0, padx=10, pady=10)

Butão = Button(tela, text='Roll', command=dado)
Butão.grid(column=0, row=1, padx=10, pady=10)

result = Label(tela, text='')
result.grid(column=0, row=2)


tela.mainloop()
