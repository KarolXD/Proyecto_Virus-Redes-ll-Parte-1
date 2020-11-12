import tkinter as tk
import time
import datetime as dt
from Redes2.Logic.Functions import autentication_customers,registerCustomers,configuracion_horario


#metodo que registra
def registrar():
    print('Datos desde formulario')
    card=fn.get()
    password=fn2.get()
    print(f"Nombre:{card}{password}")
    registerCustomers(card,password)
    #parcear  print(f "Nombre:")

def call_autentication():
    card = valor.get()
    #print('valor car'+card)
    autentication_customers(card)

def call_configuration():
    valor0 = ocurre.get()
    valor1 = fechaInicio.get()
    valor3 = dia.get()
    valor4 = tipoescaneo.get()
    print("Tipo scaneo", valor0, valor1, valor3, valor4)
    from Redes2.Logic.socket_echo_client import socket_client
    socket_client()
    configuracion_horario(valor0, valor1, valor3, valor4)


def horario():
    newWindow = tk.Toplevel(app)
    newWindow.title("Programar Horario")
    newWindow.geometry("700x500")
    LABEL = tk.Label(newWindow, text="Configuracion & Programación de ANTIVIRUS! ", relief="solid", fg='black',
                  font=("Century Gothic", 16, ""))
    LABEL.place(x=100, y=50)

    LABEL3 = tk.Label(newWindow, text="Ocurre: ", font=("Century Gothic", 12, ""))
    LABEL3.place(x=150, y=130)

    label =tk.Label(newWindow, text="fecha Inicio")
    label.place(x=190, y=170)

    ocurre.set("seleccione");
    list1 = ['Diario', 'Semanal', 'Mensual']
    droplist = tk.OptionMenu(newWindow, ocurre, *list1)
    droplist.place(x=250, y=130)
    droplist.config(width=15);

    entry1 = tk.Entry(newWindow, textvar=fechaInicio)
    entry1.insert(0, time.strftime('%H:%M'))
    entry1.place(x=240, y=170)

    C1 = tk.Checkbutton(newWindow, text="Lunes", variable=dia, onvalue=1, offvalue=-1, height=5, width=10)
    C1.pack()
    C1.place(x=5, y=200)

    C2 =tk.Checkbutton(newWindow, text="Martes", variable=dia, onvalue=2, offvalue=-2, height=5, width=10)
    C2.pack()
    C2.place(x=80, y=200)

    C3 = tk.Checkbutton(newWindow, text="Miercoles", variable=dia, onvalue=3, offvalue=-3, height=5, width=10)
    C3.pack()
    C3.place(x=170, y=200)

    C4 =tk.Checkbutton(newWindow, text="Jueves", variable=dia, onvalue=4, offvalue=-4, height=5, width=10)
    C4.pack()
    C4.place(x=280, y=200)

    C5 = tk.Checkbutton(newWindow, text="Viernes", variable=dia, onvalue=5, offvalue=-5, height=5, width=10)
    C5.pack()
    C5.place(x=380, y=200)

    C6 =tk. Checkbutton(newWindow, text="Sabado", variable=dia, onvalue=6, offvalue=-6, height=5, width=10)
    C6.pack()
    C6.place(x=460, y=200)

    C7 =tk. Checkbutton(newWindow, text="Domingo", variable=dia, onvalue=7, offvalue=-7, height=5, width=10)
    C7.pack()
    C7.place(x=560, y=200)

    C8 = tk.Checkbutton(newWindow, text="Todo C:", variable=tipoescaneo, onvalue=8, offvalue=-8, height=5, width=10)
    C8.pack()
    C8.place(x=160, y=260)

    C9 = tk.Checkbutton(newWindow, text="Completo Dir", variable=tipoescaneo, onvalue=9, offvalue=-9, height=5, width=10)
    C9.pack()
    C9.place(x=290, y=260)

    w = tk.Label(newWindow, text=f"{dt.datetime.now():%A, %b %d %Y %p  }", fg="white", bg="black", font=("Century Gothic", 30))
    w.place(x=2, y=430)

    buttonExample = tk.Button(newWindow, text="Scanner now", fg='white', bg='brown', command=call_configuration)
    buttonExample.pack()
    buttonExample.place(x=250, y=350)


def windows_register():
    newWindow = tk.Toplevel(app)
    newWindow.geometry("400x300")

    label0 = tk.Label(newWindow, text="Bienvenidos al sistema ", relief="solid", fg='black',
                   font=("Verdana", 16, ""))  # .pack()
    label0.place(x=100, y=53)

    label1 = tk.Label(newWindow, text="Card", fg='black', bg='white', font=("Verdana", 13, "bold"))
    label1.place(x=30, y=130)

    entry1 = tk.Entry(newWindow, textvar=fn)
    entry1.place(x=100, y=130)

    label2 = tk.Label(newWindow, text="Password", fg='black', bg='white', font=("Verdana", 10, "bold"))
    label2.place(x=10, y=179)

    entry1 = tk.Entry(newWindow, textvar=fn2)
    entry1.place(x=100, y=179)

    b1 = tk.Button(newWindow, text="Sign In", fg='white', bg='brown', command=registrar,
                font=("arial", 12, "bold"))  # .pack()
    b1.place(x=160, y=210)


app = tk.Tk()
app.geometry("370x250")
valor=tk.StringVar()
fn=tk.StringVar()
fn2=tk.StringVar()

ocurre = tk.StringVar()
fechaInicio = tk.StringVar()
dia = tk.IntVar()
tipoescaneo = tk.IntVar()


LABEL=tk.Label(app,text="Welcome again! ", relief="solid", fg='black',font=("Verdana",16,""))
LABEL.place(x=100, y=53)

label1 = tk.Label(app, text="Card", fg='black', bg='white', font=("Verdana", 13, "bold"))
label1.place(x=30, y=130)

entry1 = tk.Entry(app, textvar=valor)
entry1.place(x=100, y=130)

b1 = tk.Button(app, text="Log In", fg='white', bg='brown', command=call_autentication,
            font=("Century Gothic", 12, "bold"))  # .pack()
b1.place(x=100, y=170)


buttonRegister= tk.Button(app,text="Register",bg='brown',fg='white',
          command=windows_register,font=("Century Gothic", 12, "bold"))
buttonRegister.pack()
buttonRegister.place(x=170,y=170)

app.mainloop()