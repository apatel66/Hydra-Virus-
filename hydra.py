from random import random
import tkinter as tk

def on_closing(r):
    r.destroy()

    for i in range(2):
        window()


def window():
    root = tk.Toplevel()
    root.title("Hydra")

    #Position the window
    w = 450
    h = 250
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = random()*sw
    y = random()*sh
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    path = "h.png"
    message = "Cut off one head and two more grow in its place..."
    tk.Label(root, text=message, width=120, height=20).pack()

    root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))


root = tk.Tk()
root.title("Hydra")
message = "Cut off one head and two more take its place..."
tk.Label(root, text=message).pack()
root.geometry("450x250")
root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))
root.mainloop()