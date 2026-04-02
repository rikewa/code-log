import tkinter as tk


root = tk.Tk()
root.title("Title")

#root settings:
swidth = root.winfo_screenmmwidth()
sheight = root.winfo_screenheight()

width = int(swidth * 0.5)
height = int(sheight * 0.2)

root.geometry(f'{width}x{height}')
root.minsize(width=200,height=100)
root.maxsize(width=500, height=400)
root.resizable(True, True)

#root layout

#root content 
label1 = tk.Label(root, text="hello world!", bg='#00ff00')
label1.pack(side='top', expand=True, fill='both')

label2 = tk.Label(root, text='hallo welt!', bg='#ff00fc')
label2.pack(side='top', expand=True, fill='both')



# --- Start Programm ---
root.mainloop()
