from tkinter import *

mywindowFiles = Tk()
mywindowFiles.title("Formulario")
mywindowFiles.geometry("600x500")


def start_server():
    from Redes2.Logic.socket_echo_server import socket_server
    socket_server()

b2=Button(mywindowFiles, text="Iniciar", fg='white', bg='brown', command=start_server, relief=RIDGE,  font=("arial",12,"bold"))#.pack()
b2.place(x=300,y=210)

mywindowFiles.mainloop()