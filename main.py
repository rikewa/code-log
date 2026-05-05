import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.title("Title")
root.attributes('-topmost',True)
root.configure(padx=10, pady=10)

#-----style settings:
style = ttk.Style()
style.theme_use('classic')


#------functions:
def start_programm():
    pass

#-------------window settings:
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()

width = int(swidth * 0.15)
height = int(sheight * 0.2)

position_x = int((swidth - width)/2)
position_y = int((sheight - height)/2)
root.geometry(f'{width}x{height}+{position_x}+{position_y}')
root.columnconfigure(0, weight=1)

#----------window config:
mainProgramm = ttk.PanedWindow(root, orient='vertical')
mainProgramm.grid(column=0, row=0, sticky='we')

frame1 = ttk.Frame(mainProgramm)
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
label1 = ttk.Label(frame1, text='day01')
label1.grid(column=0, row=0)

day01 = ttk.Button(frame1, text='start',width=30, command=start_programm)
day01.grid(column=1, row=0)

frame2 = ttk.Frame(mainProgramm)
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)
label2 = ttk.Label(frame2, text='day02')
label2.grid(column=0, row=0)

day02 = ttk.Button(frame2, text='start',width=30, command=start_programm)
day02.grid(column=1, row=0)

mainProgramm.add(frame1)
mainProgramm.add(frame2)

# --- Start Programm ---
root.mainloop()
