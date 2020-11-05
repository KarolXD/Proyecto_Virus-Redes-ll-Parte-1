import static as static

from Redes2.Logic.Functions import autentication_customers
from tkinter import *




def show_frame():
    mywindow2 = Tk()
    mywindow2.title("Log In")
    mywindow2.geometry("400x400")

    show_form(mywindow2)
    mywindow2.mainloop()


def call_autentication():
    print('autenticando...')
    card = 'jaha'#valor.get()
    print('valor car'+card)
    autentication_customers(card)

def show_form(windows):
    label0 = Label(windows, text="Welcome again! ", relief="solid", fg='black',font=("Verdana", 16, ""))  # .pack()
    label0.place(x=120, y=53)

    label1 = Label(windows, text="Card", fg='black', bg='white', font=("Verdana", 13, "bold"))
    label1.place(x=80, y=130)
    valor = StringVar()
    entry1=Entry(windows,textvar=valor)
    entry1.place(x=200,y=130)

    b1=Button(windows, text="Sign In", fg='white', bg='brown', relief=RIDGE, command=call_autentication, font=("arial",12,"bold"))#.pack()
    b1.place(x=200,y=210)
