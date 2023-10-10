import tkinter
import customtkinter
import Groepskas as gk



class MainMenu:


    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("scouts.json")
        self.root = customtkinter.CTk()
        self.root.geometry("500x350")
        self.mainmenuframe = self.mainmenuframe()
        self.currentframe = self.mainmenuframe
        self.currentframe.pack() 
        self.groepskas = gk.GroepsKas(self.root, self)

        self.root.mainloop()

    def loadframe(self, frame):
        self.currentframe.pack_forget()
        self.currentframe = frame
        self.currentframe.pack(pady=0, padx=0, fill="both", expand=True)

    def mainmenuframe(self):
        def evenement():
            print("Evenement")

        def poef():
            print("Poef")

        def schulden():
            print("Schulden")
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Scouts Wallet", font=("Arial", 20))
        label.pack(pady=12, padx=10)

        button1 = customtkinter.CTkButton(master=frame, text="Groepskas", command=self.clickmainmenu)
        button1.pack(pady=12, padx=10)

        button2 = customtkinter.CTkButton(master=frame, text="Evenement", command=evenement)
        button2.pack(pady=12, padx=10)

        button3 = customtkinter.CTkButton(master=frame, text="Poef", command=poef)
        button3.pack(pady=12, padx=10)

        button4 = customtkinter.CTkButton(master=frame, text="Schulden", command=schulden)
        button4.pack(pady=12, padx=10)

        return frame

    def clickmainmenu(self):
        self.loadframe(self.groepskas.getgroepskasframe())
    
        

MainMenu()