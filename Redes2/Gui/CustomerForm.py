from tkinter import *
mywindow = Tk()
mywindow.title("Formulario")
mywindow.geometry("600x500")

fn=StringVar()
fn2=StringVar()
ln=StringVar()
dob=StringVar()
var=StringVar()

def exit1():
    exit()
def registrar():
    print('Datos desde formulario')
    nombre=fn.get()
    apellido=fn2.get()
    print(f"Nombre:{nombre}{apellido}")
    #parcear  print(f "Nombre:")

label0=Label(mywindow,text="Bienvenidos al sistema ", relief="solid", fg='black',font=("Verdana",16,""))#.pack()
label0.place(x=200,y=53)

label1=Label(mywindow,text="Nombre", fg='black',bg='white',font=("Verdana",13,"bold"))
label1.place(x=80,y=130)

entry1=Entry(mywindow,textvar=fn)
entry1.place(x=200,y=130)

label2=Label(mywindow,text="Apellido", fg='black',bg='white',font=("Verdana",13,"bold"))
label2.place(x=80,y=179)

entry1=Entry(mywindow,textvar=fn2)
entry1.place(x=200,y=179)


b1=Button(mywindow, text="Registrarme", fg='white', bg='brown', relief=RIDGE, command=registrar, font=("arial",12,"bold"))#.pack()
b1.place(x=150,y=380)


b2=Button(mywindow, text="Cancelar", fg='white', bg='brown', relief=RIDGE, command=exit1, font=("arial",12,"bold"))#.pack()
b2.place(x=300,y=380)

mywindow.mainloop()
