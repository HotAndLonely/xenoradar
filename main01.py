from tkinter import *
from tkinter import ttk
from platform import system
import socket
import nmap as nm
from tkinter import messagebox

root = Tk(className="Titulo")
window_size = (1024, 576)
root.geometry(str(window_size[0])+"x"+str(window_size[1]))
root.resizable(False, False)

def nmapScan():
    nmap = nm.PortScanner()
    try:
        scan = nmap.scan(socket.gethostbyname(socket.gethostname()))
    except:
        messagebox.showinfo(message="Nmap is not installed", title="Error dependency")
        pass
    

if system() == "Windows":
    nav = Menu(root)
    root.config(menu=nav)
    menu_nmap = Menu(nav, tearoff=0)
    nav.add_cascade(label="Nmap", menu=menu_nmap)
    menu_nmap.add_command(label="Scan", command=nmapScan)
else:
    root.configure(bg="black")
    label_info = Label(root,
    text="This app is still under development for this OS\n@HotAndLonely",
    font=("Consolas", 25),
    fg="#f0f0f0",
    bg="black",
    pady=str(window_size[1]/2)
     ).pack()

root.mainloop()