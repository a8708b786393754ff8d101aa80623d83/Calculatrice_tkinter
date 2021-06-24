import tkinter as tk 
import tkinter.messagebox 

from  tkinter.constants import *


b = "#1EE"

class Calculatrice(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.menu_bar()
        self.main()

    def recup_touche(self,touche=str()):
        current = self.entry.get()
        self.entry.delete(0,END)
        self.entry.insert(0,current+touche)
    
    def egal(self):
        calcul = self.entry.get()
        self.entry.delete(0, END)
        try:
            self.entry.insert(0,eval(calcul))
        except SyntaxError:
            tkinter.messagebox.showerror("Syntaxe invalide","Veuillez verifier votre syntaxe")
            


    def delete(self): 
        self.entry.delete(0,END)

    def menu_bar(self): 
        menu_main = tk.Menu(self)        
        menu_main.add_cascade(label="QUIT",command=self.quit)
        self.config(menu=menu_main)

    def main(self):
        self.entry = tk.Entry(self)
        self.entry.grid(sticky="WE")

        frame = tk.Frame(self,bg=b)
        frame.grid()

        btn_pourcent = tk.Button(frame,text="%",bg=b,command=lambda:self.recup_touche("%"))
        btn_pourcent.grid(row=2,column=0,ipadx=10,ipady=10)
        
        btn_ce = tk.Button(frame,text="CE",bg=b,command=self.delete)
        btn_ce.grid(row=2,column=1,ipadx=10,ipady=10)

        btn_c = tk.Button(frame,text="C",bg=b)
        btn_c.grid(row=2,column=2,ipadx=10,ipady=10)

        btn_effacement = tk.Button(frame,text="|x|",bg=b,command=self.delete)
        btn_effacement.grid(row=2,column=3,ipadx=10,ipady=10)

        btn_1 = tk.Button(frame,text="1",bg=b,command=lambda:self.recup_touche("1"))
        btn_1.grid(row=3,column=0,ipadx=10,ipady=10)
        
        btn_2 = tk.Button(frame,text="2",bg=b,command=lambda:self.recup_touche("2"))
        btn_2.grid(row=3,column=1,ipadx=10,ipady=10)
        
        btn_3 = tk.Button(frame,text="3",bg=b,command=lambda:self.recup_touche("3"))
        btn_3.grid(row=3,column=2,ipadx=10,ipady=10)

        btn_4 = tk.Button(frame,text="4",bg=b,command=lambda:self.recup_touche("4"))
        btn_4.grid(row=4,column=0,ipadx=10,ipady=10)
        
        btn_5 = tk.Button(frame,text="5",bg=b,command=lambda:self.recup_touche("5"))
        btn_5.grid(row=4,column=1,ipadx=10,ipady=10)

        btn_6 = tk.Button(frame,text="6",bg=b,command=lambda:self.recup_touche("6"))
        btn_6.grid(row=4,column=2,ipadx=10,ipady=10)

        btn_7 = tk.Button(frame,text="7",bg=b,command=lambda:self.recup_touche("7"))        
        btn_7.grid(row=5,column=0,ipadx=10,ipady=10)
        
        btn_8 = tk.Button(frame,text="8",bg=b,command=lambda:self.recup_touche("8"))
        btn_8.grid(row=5,column=1,ipadx=10,ipady=10)

        btn_9 = tk.Button(frame,text="9",bg=b,command=lambda:self.recup_touche("9"))
        btn_9.grid(row=5,column=2,ipadx=10,ipady=10)

        btn_moins = tk.Button(frame,text="--",bg=b,command=lambda:self.recup_touche("-"))
        btn_moins.grid(row=6,column=0,ipadx=10,ipady=10)

        btn_0 = tk.Button(frame,text="0",bg=b,command=lambda:self.recup_touche("0"))
        btn_0.grid(row=6,column=1,ipadx=10,ipady=10)

        btn_virgule = tk.Button(frame,text=",",bg=b,command=lambda:self.recup_touche("."))
        btn_virgule.grid(row=6,column=2,ipadx=10,ipady=10)

        btn_plus = tk.Button(frame,text="+",bg=b,command=lambda:self.recup_touche("+"))
        btn_plus.grid(row=3,column=3,ipadx=10,ipady=10)

        btn_fois = tk.Button(frame,text="x",bg=b,command=lambda:self.recup_touche("*"))
        btn_fois.grid(row=4,column=3,ipadx=10,ipady=10)

        btn_diviser = tk.Button(frame,text="`-.",bg=b,command=lambda:self.recup_touche("/"))
        btn_diviser.grid(row=5,column=3,ipadx=10,ipady=10)

        btn_egale = tk.Button(frame,text="=",bg=b,command=self.egal)
        btn_egale.grid(row=6,column=3,ipadx=10,ipady=10)


if __name__ == "__main__":
    app = Calculatrice()
    app.title("Calculatrice")
    app.config(bg=b)
    app.mainloop()