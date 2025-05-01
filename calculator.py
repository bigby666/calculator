import tkinter
from tkinter import *
import re




#creation de la fenêtre et des dimensions
screen= Tk()
screen.title("Calculator made by bigby666")
screen.minsize(300, 150)
screen.maxsize(300,150)
screen.config(bg="black")
titre= Label(screen, text= "calculatrice", bg="black", fg="white")
titre.pack()

interface= Frame(screen, background="black")
interface.pack()

#zone d'écriture
expression= StringVar()
expression.set("")

text = Text(interface, width= 39, height=3, bg="#f1f1f1", fg="black", font=("Eurostile",16))
text.pack()
text.delete("1.0", "end")
#case qui affiche le resultat
label_result =Label(interface, text="", bg="#f1f1f1", fg="black", font=("Eurostile",16))
label_result.pack()
label_result.place(x=0, y=40)
#bouton pour valider l'opperation

def calculate():
  valeurs= text.get("1.0","end-1c")

  #on filtre l'entrée des informations
  if re.fullmatch(r"[0-9+\-*/^().]+", valeurs):
    try:
      valeurs = valeurs.replace("^", "**")
      result = eval(valeurs)
    except Exception as e:
      result = f"Erreur: {e}"
  else:
    result = "caractère non autorisée"
  print(result)
  label_result.config(text=f"{result}")

valider = Button(interface, text="=", command=calculate)
valider.pack()


print(calculate)
screen.mainloop()