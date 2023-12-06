from tkinter import *
import numpy as np

def media_semestre():
    cp1 = float(E1.get())
    cp2 = float(E2.get())
    cp3 = float(E3.get())
    ch1 = float(E4.get())
    ch2 = float(E5.get())
    gs = float(E6.get())

    peso1 = 0.4
    peso2 = 0.6
    notas = [cp1, cp2, cp3]
    notas.remove(min(notas))

    calculo_cps = np.average(notas)
    calculo_chs = np.average([ch1, ch2])
    calculo_gs = np.multiply(gs, peso2)

    media_cps_chs = np.average([calculo_cps, calculo_chs]) 

    media_peso1 = np.multiply(media_cps_chs, peso1) 

    total = np.sum([media_peso1, calculo_gs])   

    E8.config(state='normal')
    E8.delete(0, END)
    E8.insert(END, str(total))
    E8.config(state='readonly')
    
def limpar_campos():
    for entry in [E1, E2, E3, E4, E5, E6, E8]:
        entry.delete(0, END)

    E8.config(state='readonly')

top = Tk()
L1 = Label(top, text="Cálculo de Média Semestral",).grid(row=0,column=1)
L2 = Label(top, text="Checkpoint 1",).grid(row=1,column=0)
L3 = Label(top, text="Checkpoint 2",).grid(row=2,column=0)
L4 = Label(top, text="Checkpoint 3",).grid(row=3,column=0)
L5 = Label(top, text="Challenge Sprint 1",).grid(row=4,column=0)
L6 = Label(top, text="Challenge Sprint 2",).grid(row=5,column=0)
L7 = Label(top, text="Global Solution",).grid(row=6,column=0)
E1 = Entry(top, bd=5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd=5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd=5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd=5)
E4.grid(row=4,column=1)
E5 = Entry(top, bd=5)
E5.grid(row=5,column=1)
E6 = Entry(top, bd=5)
E6.grid(row=6,column=1)

L9 = Label(top, text="Resultado",).grid(row=8,column=0)
E8 = Entry(top, bd=5, state='readonly')
E8.grid(row=8,column=1)

B_submit = Button(top, text="Submit", command=media_semestre).grid(row=9, column=1)
B_limpar = Button(top, text="Limpar", command=limpar_campos).grid(row=10, column=1)

top.mainloop()
