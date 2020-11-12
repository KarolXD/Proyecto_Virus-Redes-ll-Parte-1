import tkinter as tk
import time
import datetime as dt
from Redes2.Logic.Functions import autentication_customers,registerCustomers


#metodo que registra
def registrar():
    print('Datos desde formulario')
    card=fn.get()
    password=fn2.get()
    print(f"Nombre:{card}{password}")
    registerCustomers(card,password)
    #parcear  print(f "Nombre:")

def call_configuration():
    valor0 = ocurre.get
    valor1 = fechaInicio.get()
    valor3 = dia.get()
    valor4 = tipoescaneo.get()
    print("Tipo scaneo", valor0, valor1, valor3, valor4)
    from Redes2.Logic.socket_echo_client import socket_client
    socket_client()
    #configuracion_horario(valor0, valor1, valor3, valor4)

#Metodo que valida la autenticacion
def call_autentication():
    card = valor.get()
    #print('valor car'+card)
    autentication_customers(card)



#Ventana para Registrarme
def createNewWindow():
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
app.title("Chose an action")
app.geometry("370x150")

valor=tk.StringVar()
fn=tk.StringVar()
fn2=tk.StringVar()

ocurre = tk.StringVar()
fechaInicio = tk.StringVar()
dia = tk.IntVar()
tipoescaneo = tk.IntVar()

label0 = tk.Label(app, text="Bienvenidos al sistema ", relief="solid", fg='black',
                   font=("Verdana", 16, ""))  # .pack()
label0.place(x=60, y=20)


#Ventana para autenticarme
def createNewWindowAutentication():

    newWindow = tk.Toplevel(app)
    newWindow.geometry("370x250")
    LABEL=tk.Label(newWindow,text="Welcome again! ", relief="solid", fg='black',font=("Verdana",16,""))
    LABEL.place(x=100, y=53)

    label1 = tk.Label(newWindow, text="Card", fg='black', bg='white', font=("Verdana", 13, "bold"))
    label1.place(x=30, y=130)

    entry1 = tk.Entry(newWindow, textvar=valor)
    entry1.place(x=100, y=130)

    b1 = tk.Button(newWindow, text="Log In", fg='white', bg='brown', command=call_autentication,
                font=("arial", 12, "bold"))  # .pack()
    b1.place(x=100, y=170)

buttonExample = tk.Button(app,
              text="Autentication",bg='brown',fg='white',
              command=createNewWindowAutentication)
buttonExample.pack()
buttonExample.place(x=100,y=70)



buttonRegister= tk.Button(app,
              text="Register",bg='brown',fg='white',
              command=createNewWindow)
buttonRegister.pack()
buttonRegister.place(x=190,y=70)

app.mainloop()