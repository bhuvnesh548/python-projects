#Python Text editor 
import tkinter as tk
from tkinter import filedialog,messagebox
screen=tk.Tk()
screen.title("simple text editor")
screen.geometry("800x600")

text=tk.Text(screen,wrap=tk.WORD,font=("Helvetica",14))
text.pack(expand=True,fill=tk.BOTH)

def newfile():
    text.delete(1.0,tk.END)

def openfile():
    filepath=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if filepath:
        with open(filepath,"r")as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read)

def savefile():
    filepath=filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
        )
    if filepath:
        with open(filepath,"w") as file:
            file.write(text.get(1.0,tk.END))
    messagebox.showinfo("info","your file saved succesfully ! ")

menu=tk.Menu(screen)
screen.config(menu=menu)
filemenu=tk.Menu(menu)

menu.add_cascade(label="file",menu=filemenu)

filemenu.add_command(label="new",command=newfile)
filemenu.add_command(label="save",command=savefile)
filemenu.add_command(label="open",command=openfile)
filemenu.add_separator()
filemenu.add_command(label="exit",command=screen.quit)
screen.mainloop()

