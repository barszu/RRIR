import tkinter as tk
from tkinter import messagebox

from utils import solve

import matplotlib.pyplot as plt

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.minsize(600, 300)
        self.root.maxsize(600, 300)

        self.label = tk.Label(self.root, text="Rurka", font=('Arial', 18))
        self.label.pack(padx=10, pady=40)

        self.label = tk.Label(self.root, text="divisions no")
        self.label.pack(side='top')

        self.entry = tk.Entry(self.root, justify='center' )
        self.entry.pack(side='top')

        self.button = tk.Button(self.root, justify='center', text="calculate!", height=2, width=10, command=self.solve)
        self.button.pack(padx=10, pady=47)

        self.root.mainloop()
        
        
    def showGraph(self, x, y, n):
        ax = plt.subplot()
        ax.set(title='dupa wykres', xlabel='n = ' + str(n))
        ax.plot(x, y, color='red')

        plt.show()

    def solve(self):
        try:
            n = int(self.entry.get())
            if n <= 2: raise Exception("n must be greater than 2")
            
            try:
                x, y = solve(n,1,n)
                print(x)
                print(y)
                
                try:
                    # new window with plot
                    self.showGraph(x, y, n)
                except:
                    messagebox.showwarning(title="ERROR Show Data Malfunction", message="Something goes wrong with showing...")
            except:
                messagebox.showwarning(title="ERROR on solving", message="Something goes wrong with showing...")
                        
        except:
             messagebox.showwarning(title="ERROR Incorrect input data!", message="Please provide a Integer!")
    
        


if __name__ == "__main__":
    App()