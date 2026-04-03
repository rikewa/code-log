import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Title")

#root settings:
swidth = root.winfo_screenmmwidth()
sheight = root.winfo_screenheight()

width = int(swidth * 0.5)
height = int(sheight * 0.2)

root.geometry(f'{width}x{height}')
root.minsize(width=200,height=100)
root.maxsize(width=200, height=150)
root.resizable(True, True)

#root layout
image = Image.open('logo.png').resize((200,80))
photo = ImageTk.PhotoImage(image)

#root content 
label1 = tk.Label(root, text="hello world!", bg='#00ff00')
label1.pack(side='top', expand=True, fill='both')

label2 = ttk.Label(root, image=photo)
label2.pack()
# --- Start Programm ---
root.mainloop()
