import tkinter as tk
from tkinter import font
from tkinter import ttk

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
        # FRAME BUTTONS
        frame1 = tk.Frame(self.root, width=200, height=600, bg="grey")
        frame1.place(x=0, y=0)

        self.buttonNew = tk.Button(frame1, text="New", command=self.InsertData,
                               width=24, height=2)
        self.buttonNew.place(x=10, y=20)
        
        self.buttonUpdate = tk.Button(frame1, text="Update", command=self.UpdateData, 
                                 width=24, height=2)
        self.buttonUpdate.place(x=10, y=70)

        self.buttonDelete = tk.Button(frame1, text="Delete", command=self.DeleteData, 
                                 width=24, height=2) 
        self.buttonDelete.place(x=10, y=120)       

        # FRAME INPUT 25 + 40
        self.frame2 = tk.Frame(self.root, width=300, height=600, bg="whitesmoke")
        

        lbl1 = tk.Label(self.frame2, text="ID")
        lbl1.place(x=10, y=15)
        entry1 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry1.place(x=10, y=40)

        lbl2 = tk.Label(self.frame2, text="Modelo:")
        lbl2.place(x=10, y=80)
        entry2 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry2.place(x=10, y=105)

        lbl3 = tk.Label(self.frame2, text="Año:")
        lbl3.place(x=10, y=145)
        entry3 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry3.place(x=10, y=170)

        lbl4 = tk.Label(self.frame2, text="Color:")
        lbl4.place(x=10, y=210)
        entry4 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry4.place(x=10, y=235)

        lbl5 = tk.Label(self.frame2, text="Capacidad del Motor:")
        lbl5.place(x=10, y=275)
        entry5 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry5.place(x=10, y=300)

        lbl6 = tk.Label(self.frame2, text="Potencia del Motor:")
        lbl6.place(x=10, y=340)
        entry6 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry6.place(x=10, y=365)

        lbl7 = tk.Label(self.frame2, text="Tipo de Motor:")
        lbl7.place(x=10, y=405)
        entry7 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry7.place(x=10, y=430)

        lbl8 = tk.Label(self.frame2, text="Transmision:")
        lbl8.place(x=10, y=470)
        entry8 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry8.place(x=10, y=495)

        lbl9 = tk.Label(self.frame2, text="Precio")
        lbl9.place(x=10, y=535)
        entry9 = tk.Entry(self.frame2, width=30, font=font.Font(size=12))
        entry9.place(x=10, y=560)

        # Frame Buttons Save and Cancel
        self.buttonSave = tk.Button(frame1, text="Save", command=self.save,
                               width=24, height=2, background="green", foreground="black")
        
        
        self.buttonCancel = tk.Button(frame1, text="Cancel", command=self.cancel,
                               width=24, height=2, background="red", foreground="black")
        
        # Table's frame of database
        self.grid = ttk.Treeview(self.root, columns=("col1","col2","col3","col4"
                                                     , "col5", "col6", "col7", "col8"))
        self.grid.column("#0", width=50)
        self.grid.column("col1", width=70)
        self.grid.column("col2", width=70)
        self.grid.column("col3", width=70)
        self.grid.column("col4", width=70)
        self.grid.column("col5", width=70)
        self.grid.column("col6", width=70)
        self.grid.column("col7", width=70)
        self.grid.column("col8", width=70)

        self.grid.heading("#0", text="ID")
        self.grid.heading("col1", text="Model")
        self.grid.heading("col2", text="Year")
        self.grid.heading("col3", text="Color")
        self.grid.heading("col4", text="EngineCapacity")
        self.grid.heading("col5", text="EnginePower")
        self.grid.heading("col6", text="EngineType")
        self.grid.heading("col7", text="Transmission")
        self.grid.heading("col8", text="Price")
        
        self.grid.place(x=200, y=0, width=999, height=599)
        

    
    def cancel(self):
        self.buttonSave.place_forget()
        self.buttonCancel.place_forget()
        self.grid.place_forget()
        self.grid.place(x=200, y=0, width=999, height=599)


    def save(self):
        pass

    def InsertData(self):
        self.grid.place(x=500, y=0, width=699, height=599)
        self.frame2.place(x=200, y=0)
        self.buttonSave.place(x=10, y=495)
        self.buttonCancel.place(x=10, y=545)

    def UpdateData(self):
        self.grid.place(x=500, y=0, width=699, height=599)
        self.frame2.place(x=200, y=0)
        self.buttonSave.place(x=10, y=495)
        self.buttonCancel.place(x=10, y=545)

    def DeleteData(self):
        pass

