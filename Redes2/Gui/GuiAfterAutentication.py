import tkinter as tk
from Redes2.Logic.Functions import create_hast,scanner_files
app = tk.Tk()
app.title("Chose an action")
app.geometry("500x300")
def call_hast():
    create_hast()

def call_scanner():
     scanner_files()



LABEL=tk.Label(app,text="Welcome again AntiVirus! ", relief="solid", fg='black',font=("Century Gothic",16,""))
LABEL.place(x=100, y=50)

LABEL2=tk.Label(app,text="Programar Antivirus ",font=("Century Gothic",12,""))
LABEL2.place(x=100, y=100)

LABEL3=tk.Label(app,text="Ocurre: ",font=("Century Gothic",12,""))
LABEL3.place(x=100, y=130)

var =tk.StringVar()


var.set("seleccione");
list1=['Diario','Semanal','Mensual'];
droplist=tk.OptionMenu(app,var,*list1)
droplist.place(x=170, y=130)
droplist.config(width=15);


buttonExample = tk.Button(app, text="Register", fg='white', bg='brown', command=call_hast)
buttonExample.pack()
buttonExample.place(x=100,y=300)


buttonScanner = tk.Button(app,
              text="Syncronization", fg='white', bg='brown', command=call_scanner)
buttonScanner.pack()
buttonScanner.place(x=100,y=400)



app.mainloop()


