from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(
            initialfile="Untitled.txt",
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
        )
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    textArea.event_generate(("<<Cut>>"))


def copy():
    textArea.event_generate(("<<Copy>>"))


def paste():
    textArea.event_generate(("<<Paste>>"))


def about():
    tmsg.showinfo("Notepad", "Notepad by Umang Agrawal")


if __name__ == "__main__":

    root = Tk()
    root.title("Notepad")
    # root.wm_iconbitmap('')
    root.geometry("644x748")

    # Textarea
    textArea = Text(root, font="lucida 16")
    file = None
    textArea.pack(fill=BOTH, expand=True)

    # menubar
    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)
    menubar.add_cascade(label="File", menu=fileMenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)

    # scrollbar
    scrollbar = Scrollbar(textArea)
    scrollbar.pack(side=RIGHT, fill=Y, ipadx=5)
    scrollbar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollbar.set)
    root.mainloop()
