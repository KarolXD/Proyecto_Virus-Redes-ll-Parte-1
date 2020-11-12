import tkinter as tk
import datetime as dt
import time
from Redes2.Logic.Functions import create_hast, configuracion_horario
app = tk.Tk()
app.title("Chose an action")
app.geometry("700x400")
def call_hast():
    create_hast()

def call_configuration():
    valor0= ocurre.get()
    valor1 = fechaInicio.get()
    valor2 = fechaFin.get()
    valor3 = lunes.get()
    valor4 = martes.get()
    valor5 = miercoles.get()
    valor6 = jueves.get()
    valor7 = viernes.get()
    valor8 = sabado.get()
    valor9 = domingo.get()
    print('Ocurre '+valor0)
    print('FechaInicio ' + valor1)
    print('FechaFin ' + valor2)
    print('Lunes ' + str(valor3))
    print('Martes ' + str(valor4))
    print('Miercoles ' + str(valor5))
    print('Jueves ' + str(valor6))
    print('Viernes ' + str(valor7))
    print('Sabado ' + str(valor8))
    print('Domingo ' + str(valor9))
    configuracion_horario(valor0,valor1,valor2,valor3,valor4,valor5,valor6,valor7,valor8,valor9)




LABEL=tk.Label(app,text="Configuracion & Programación de ANTIVIRUS! ", relief="solid", fg='black',font=("Century Gothic",16,""))
LABEL.place(x=100, y=50)


LABEL3=tk.Label(app,text="Ocurre: ",font=("Century Gothic",12,""))
LABEL3.place(x=150, y=130)

ocurre =tk.StringVar()
fechaInicio=tk.StringVar()
fechaFin=tk.StringVar()

lunes=tk.IntVar()
martes=tk.IntVar()
miercoles=tk.IntVar()
jueves=tk.IntVar()
viernes=tk.IntVar()
sabado=tk.IntVar()
domingo=tk.IntVar()


ocurre.set("seleccione");
list1=['Diario','Semanal','Mensual'];
droplist=tk.OptionMenu(app,ocurre,*list1)
droplist.place(x=250, y=130)
droplist.config(width=15);


label=tk.Label(app, text="Inicio")
label.place(x=100, y=170)


entry1 = tk.Entry(app, textvar=fechaInicio)
entry1.insert(0, time.strftime('%Y/%m/%d %H:%M:%S'))
entry1.place(x=150, y=170)

label=tk.Label(app, text="Fin")
label.place(x=300, y=170)

entry1 = tk.Entry(app, textvar=fechaFin)
entry1.insert(0, time.strftime('%Y/%m/%d %H:%M:%S'))
entry1.place(x=360, y=170)

C1 = tk.Checkbutton(app, text = "Lunes", variable = lunes,onvalue = 1, offvalue = -1, height=5, width = 10)
C1.pack()
C1.place(x=5, y=200)

C2 = tk.Checkbutton(app, text = "Martes", variable = martes,onvalue = 2, offvalue = -2, height=5, width = 10)
C2.pack()
C2.place(x=80, y=200)

C3 = tk.Checkbutton(app, text = "Miercoles", variable = miercoles,onvalue = 3, offvalue = -3, height=5, width = 10)
C3.pack()
C3.place(x=170, y=200)

C4= tk.Checkbutton(app, text = "Jueves", variable = jueves,onvalue = 4, offvalue = -4, height=5, width = 10)
C4.pack()
C4.place(x=280, y=200)

C5= tk.Checkbutton(app, text = "Viernes", variable = viernes,onvalue = 5, offvalue = -5, height=5, width = 10)
C5.pack()
C5.place(x=380, y=200)

C6= tk.Checkbutton(app, text = "Sábado", variable = sabado,onvalue = 6, offvalue = -6, height=5, width = 10)
C6.pack()
C6.place(x=460, y=200)

C7= tk.Checkbutton(app, text = "Domingo", variable = domingo,onvalue = 7, offvalue = -7, height=5, width = 10)
C7.pack()
C7.place(x=560, y=200)


w = tk.Label(app, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("Century Gothic", 30))
w.place(x=2,y=350)

buttonExample = tk.Button(app, text="Iniciar Programacion", fg='white', bg='brown', command=call_configuration)
buttonExample.pack()
buttonExample.place(x=250,y=300)



app.mainloop()


