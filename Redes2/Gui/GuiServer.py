from tkinter import *
from Redes2.Logic.Functions import  obtener_datos
import time
mywindowServer = Tk()
mywindowServer.title("Server")
mywindowServer.geometry("500x500")


def start_server():
    from Redes2.Logic.socket_echo_server import socket_server
    socket_server()



b2=Button(mywindowServer, text="Iniciar Servidor", fg='white', bg='brown', command=start_server, relief=RIDGE,  font=("arial",12,"bold"))#.pack()
b2.place(x=20,y=200)

T = Text(mywindowServer, height=15, width=50)
T.insert(END,str(obtener_datos()))
b2.place(x=90,y=300)
T.pack()


mywindowServer.mainloop()

