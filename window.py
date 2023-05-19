import tkinter as tk
from tkinter import font

class Window:

    def __init__(self, root):
        self.root = root
        self.settings()
        self.create_widgets()


    def settings(self): 
        self.root.title("CRUD PYTHON MYSQL") # Title of the window
        self.root.resizable(0, 0) # Disable to resizable the window

        icon = tk.PhotoImage(file="images\icon.png")
        self.root.iconphoto(True, icon)

        # Size and position of the window
        widthScreen = self.root.winfo_screenwidth()
        heightScreen = self.root.winfo_screenheight()
        widthWindow = 1200
        heightWindow = 600
        pwidth = int(widthScreen/2 - widthWindow/2)
        pheight = int(heightScreen/2 - heightWindow/2)
        self.root.geometry(f"{widthWindow}x{heightWindow}+{pwidth}+{pheight-30}")

    def create_widgets(self):
        frame1 = tk.Frame(self.root, width=200, height=600, bg="grey")
        frame1.place(x=0, y=0)
        
        
        
