import tkinter
import customtkinter

class GroepsKas:
    def __init__(self, root):
        self.root = root
        self.frame = self.groepskasframe()
        self.overzicht = Overzicht(self.frame)
        
        
    def groepskasframe(self):
        frame = customtkinter.CTkFrame(master=self.root)
        label = customtkinter.CTkLabel(master=frame, text="Groepskas", font=("Arial", 30))
        label.grid(row = 0, column = 0, columnspan = 2, pady=12, padx=10)
        
        addtransactionsbutton = customtkinter.CTkButton(master=frame, text="Voeg transacties toe")
        addtransactionsbutton.grid(row = 1, column = 0, columnspan = 2, sticky = "", pady=(0,24), padx=10,)

        frame.columnconfigure(1, weight=5)
        frame.rowconfigure(2, weight=1)
        frame.columnconfigure(0, weight=1)
        
        return frame
    
    def getgroepskasframe(self):
        return self.frame

class Overzicht:
    def __init__(self, frame):
        # Create an oversight frame which is split up in silectframe (left) and dataframe (right)
        self.frame = frame
        # self.selectframe = customtkinter.CTkScrollableFrame(master=self.frame, bg_color="red")
        # self.selectframe.grid(row = 2, column = 0, sticky = "nswe", pady=0, padx=0)
        # self.dataframe = customtkinter.CTkScrollableFrame(master=self.frame, bg_color = "blue")
        # self.dataframe.grid(row = 2, column = 1, sticky = "nswe", pady=0, padx=0)

        # v1 = customtkinter.CTkScrollbar(self.selectframe, command=self.selectframe.yview)
        # v2 = customtkinter.CTkScrollbar(self.dataframeframe, command=self.dataframeframe.yview)

        #Create and load in the different years
        # self.loadyears()
    
    def loadyears(self):
        # Create a list of years
        self.years = []
        for i in range(2019, 2025):
            self.years.append(i)
        
        # Create a list of buttons for the years
        self.yearbuttons = []
        self.selectframe.columnconfigure(0, weight=1) 
        for i in range(len(self.years)):
            self.yearbuttons.append(customtkinter.CTkButton(master=self.selectframe, text=self.years[i], command= lambda i=i: self.clickyear(self.years[i])))
            self.yearbuttons[i].grid(row = i, column = 0, sticky = "nswe", pady=4, padx=2)
            # self.yearbuttons[i].bind("<Button-1>", self.clickyear)

    def clickyear(self, year):
        # if a year is clicked we need to generate the data for that year
        # we are now gonna generate some random data
        data = []
        for i in range (1, 10):
            data.append(("test", i * 1000 * (-1) ** i))
        
        # we need to clear the dataframe
        for widget in self.dataframe.winfo_children():
            widget.destroy()

        # we need to create 2 labels for each transaction, 1 with the name and 1 with the amount, if the amount is negative it needs to be red otherwise green
        for i in range(len(data)):
            name = customtkinter.CTkLabel(master=self.dataframe, text=data[i][0])
            name.grid(row = i, column = 0, sticky = "nsw", pady=4, padx=10)
            amount = customtkinter.CTkLabel(master=self.dataframe, text=data[i][1])
            amount.grid(row = i, column = 1, sticky = "nswe", pady=4, padx=10)
            if data[i][1] < 0:
                amount.configure(text_color="red")
            else:
                amount.configure(text_color="green")   
        self.dataframe.columnconfigure(0, weight=1)
        
            


class AddTransactions:
    def __init__(self, frame):
        self.frame = frame
        self.addtransactionsframe = self.addtransactionsframe()

    # def addtransactionsframe(self):

 