import tkinter as tk
from tkinter import messagebox

from solver import solve

import matplotlib.pyplot as plt

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.minsize(600, 400)
        self.root.maxsize(600, 400)

        self.label = tk.Label(self.root, text="Gravitational Field Potential Solwer", font=('Arial', 20))
        self.label.pack(padx=10, pady=40)
        
        # n input
        self.label = tk.Label(self.root, text="divisions no")
        self.label.pack(side='top')

        self.entry = tk.Entry(self.root, justify='center' )
        self.entry.pack(side='top')
        
        # G input
        self.label2 = tk.Label(self.root, text="G  (default G= 6.67430e-11)")
        self.label2.pack(side='top' , pady=10)

        self.entry2 = tk.Entry(self.root, justify='center' )
        self.entry2.pack(side='top')
        
        # start button
        self.button = tk.Button(self.root, justify='center', text="COMPUTE", height=2, width=10, command=self.solve)
        self.button.pack(padx=10, pady=40)

        self.root.mainloop()
        
        
    def showGraph(self, x, y, n , G):
        ax = plt.subplot()
        ax.set(title='Computed Solution:', xlabel='n = ' + str(n) + "  G =" + str(G))
        ax.plot(x, y, color='red')
  
        plt.show()

    def solve(self):
        try:
            n = int(self.entry.get())
            G = float(self.entry2.get())
            if n <= 2: raise Exception("n must be greater than 2")
            
            try:
                x, y = solve(n,G,n)
                print(x)
                print(y)
                
                try:
                    # new window with plot
                    self.showGraph(x, y, n, G)
                except:
                    messagebox.showwarning(title="ERROR Show Data Malfunction", message="Something goes wrong with showing...")
            except:
                messagebox.showwarning(title="ERROR on solving", message="Something goes wrong with computing...")
                        
        except:
             messagebox.showwarning(title="ERROR Incorrect input data!", message="Please provide a n as Integer & G as float (eq. 0.55) !")
    
        


if __name__ == "__main__":
    App()