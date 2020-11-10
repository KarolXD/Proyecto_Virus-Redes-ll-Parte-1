from tkinter import *

mywindowServer = Tk()
mywindowServer.title("Server")
mywindowServer.geometry("190x100")


def start_server():
    from Redes2.Logic.socket_echo_server import socket_server
    socket_server()

b2=Button(mywindowServer, text="Iniciar Servidor", fg='white', bg='brown', command=start_server, relief=RIDGE,  font=("arial",12,"bold"))#.pack()
b2.place(x=20,y=50)

mywindowServer.mainloop()