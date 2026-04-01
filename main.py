#tk alias führt Tk funktion aus
#window = tk.Tk()

#Spicker:
#int, float, str, bool → einfache Werte
#list, tuple, set, dict → Sammlungen / Datenstrukturen
#None → leerer Wert
#def → Funktionen
#class → Objekte / eigene Datentypen

#wiederholung der basics:
#string = "das ist ein String/text"
#integer = 5
#float = 1.5
#print("string\n", "integer\n", "float")


#import tkinter library and name it as a alias 
#tkinter ist eine Library/ Anbindung zu Tk, ein Tool-kit für grafische Oberflächen. Mithilfe von tkinter können wir auch Tk zugreifen.


#hier importieren wir tkinter und haben somit zugriff auf das Tool-Kit Tk
import tkinter as tk
#import tkinter.font as tkFont

#testing window for tkinter
#tk._test()

#Labels sind Widgets in einer GUI, also ein baustein innerhalb meines Fensters.
#Buttons sind ebenfalls Widgets
#es gibt viele weitere Widgets in der tkinter library 

#how to create a GUI?

#create tk-object and safe it in variable (root)
root = tk.Tk()
#widget erstellen um inhalt in das fenster einzubauen

#root ist hier parent
#um später zugriff auf das label zu haben braucht es eine Variable (label1)
label1 = tk.Label(root, text="hello world")

#text wird bisher nicht angezeigt weil layout fehlt, es benötigt die methode pack:
label1.pack()

#hier wird eine Methode gestartet
root.mainloop()