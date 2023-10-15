import tkinter
import customtkinter
import Groepskas as gk
import win32com.client
import os


class MainMenu:


    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("scouts.json")
        self.config = {}
        self.loadconfig()
        self.root = customtkinter.CTk()
        self.root.geometry("500x350")
        self.groepskas = gk.GroepsKas(self.root, self)
        self.mainmenuframe = self.get_mainmenuframe()
        self.currentframe = self.mainmenuframe
        self.currentframe.pack(pady=0, padx=0, fill="both", expand=True) 

        self.root.mainloop()
        self.evaluateworkbooks()

    def loadframe(self, frame):
        self.currentframe.pack_forget()
        self.currentframe = frame
        self.currentframe.pack(pady=0, padx=0, fill="both", expand=True)

    def get_mainmenuframe(self):

        def jin():
            print("Jin")

        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Scouts Wallet", font=("Arial", 20))
        label.pack(pady=12, padx=10)

        button1 = customtkinter.CTkButton(master=frame, text="Groepskas", command=self.clickmainmenu)
        button1.pack(pady=12, padx=10)

        # button2 = customtkinter.CTkButton(master=frame, text="Evenement", command=evenement)
        # button2.pack(pady=12, padx=10)


        button3 = customtkinter.CTkButton(master=frame, text="Jin", command=jin)
        button3.pack(pady=12, padx=10)

        huidig_jaar_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
        huidig_jaar_frame.pack(pady=20, padx=10)        

        label_jaar = customtkinter.CTkLabel(master=huidig_jaar_frame, text="Huidig jaar:", font=("Arial", 16))
        label_jaar.grid(row=0, column=0, pady=0, padx=0)

        self.jaar_option_var = tkinter.StringVar()
        self.jaar_option_var.set(self.groepskas.huidig_jaar)
        jaar_options = customtkinter.CTkOptionMenu(master=huidig_jaar_frame, variable=self.jaar_option_var, values=self.groepskas.years, command=self.set_huidig_jaar)
        jaar_options.grid(row=0, column=1, pady=0, padx=14)

        return frame
    def set_huidig_jaar(self, jaar):

        #Change the lastchecked config
        self.groepskas.mainmenu.config["huidig_jaar"] = str(jaar)

        #Also change it in the config file
        with open("Config.txt", "w") as file:
            for key, value in self.groepskas.mainmenu.config.items():
                file.write(key + "! " + value + "\n")
        
        self.groepskas.loadfiles()

    def clickmainmenu(self):
        self.loadframe(self.groepskas.getgroepskasframe())
    
    def loadconfig(self):
        
        with open('config.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                key, value = line.strip().split('!')
                self.config[key] = value.strip()
    
    def returntomainmenu(self):
        self.loadframe(self.mainmenuframe)

    def evaluateworkbooks(self):
        excel = win32com.client.Dispatch("Excel.Application")
        #Open and close all xlsx files in Files folder to evaluate formulas and save them
        for filename in os.listdir(self.groepskas.current_path + "/Groepskas"):
            if filename.endswith(".xlsx"):
                wb = excel.Workbooks.Open(self.groepskas.current_path + "/Groepskas/" + filename)
                wb.Save()
                wb.Close(True)
        excel.Quit()
    
MainMenu()