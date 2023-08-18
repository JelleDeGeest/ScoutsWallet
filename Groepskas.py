import tkinter
import customtkinter

class GroepsKas:
    def __init__(self, root):
        self.root = root
        self.frame = self.groepskasframe()
        self.test = test()
        
    def groepskasframe(self):
        frame = customtkinter.CTkFrame(master=self.root)
        label = customtkinter.CTkLabel(master=frame, text="Groepskas", font=("Arial", 20))
        label.pack(pady=12, padx=10)
        return frame
    
    def getgroepskasframe(self):
        return self.frame

class Overzicht:
    def __init__(self):
        print("test")
 