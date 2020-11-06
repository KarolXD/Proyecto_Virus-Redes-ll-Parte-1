import tkinter as tk
from Redes2.Logic.Functions import create_hast,scanner_files
app = tk.Tk()
app.title("Chose an action")
app.geometry("200x100")
def call_hast():
    create_hast()

def call_scanner():
     scanner_files()

buttonExample = tk.Button(app,
              text="Register", fg='white', bg='brown', command=call_hast)
buttonExample.pack()
buttonExample.place(x=5,y=30)


buttonScanner = tk.Button(app,
              text="Syncronization", fg='white', bg='brown', command=call_scanner)
buttonScanner.pack()
buttonScanner.place(x=5,y=60)
app.mainloop()


