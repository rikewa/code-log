import tkinter as tk 
from tkinter import ttk 
# pink: #ff00e4 grün:#00ff00


root = tk.Tk()
root.title('')
root.attributes('-topmost', True)
root.configure(pady=10, padx=10, background='#ff00e4')

#-----window settings:
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()

width = int(swidth * 0.6)
height = int(sheight * 0.4)

position_x = int((swidth - width)/2)
position_y = int((sheight - height)/2)

root.geometry(f'{width}x{height}+{position_x}+{position_y}')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

#-----style settings:
style = ttk.Style()
style.theme_use('alt')
style.configure('button1.TButton', padding =(10, 10))

#--------gui setup:
#----1. Zeile:
zeile1 = ttk.Frame(root)
zeile1.grid(column=0, row=0, sticky='nswe')

for i in range(13):
    zeile1.columnconfigure(i, weight=1)

zeile1.columnconfigure(14, weight=10)
zeile1.rowconfigure(0, weight=1)

button1 = ttk.Button(zeile1, text='B1', style='button1.TButton')
button1.grid(column=0, row=0, pady=10)

button2 = ttk.Button(zeile1, text='B2',style='button1.TButton')
button2.grid(column=1, row=0)

button3 = ttk.Button(zeile1, text='B3',style='button1.TButton')
button3.grid(column=2, row=0)

button4 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button4.grid(column=3, row=0)

button5 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button5.grid(column=4, row=0)

button6 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button6.grid(column=5, row=0)

button7 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button7.grid(column=6, row=0)

button8 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button8.grid(column=7, row=0)

button9 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button9.grid(column=8, row=0)

button10 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button10.grid(column=9, row=0)

button11 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button11.grid(column=10, row=0)

button12 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button12.grid(column=11, row=0)

button13 = ttk.Button(zeile1, text='B4',style='button1.TButton')
button13.grid(column=12, row=0)

button14 = ttk.Button(zeile1, text='B4', style='button1.TButton')
button14.grid(column=13, row=0)

#----2. Zeile:
zeile2 = ttk.Frame(root)
zeile2.grid(column=0, row=1, padx=10)

#----3. Zeile:
zeile3 = ttk.Frame(root)
zeile3.grid(column=0, row=2)

#----4. Zeile:
zeile4 = ttk.Frame(root)
zeile4.grid(column=0, row=3)

#----5. Zeile:
zeile5 = ttk.Frame(root)
zeile5.grid(column=0, row=4)




#----prgram start:
root.mainloop()