from tkinter import ttk

class PropertiesFrame(ttk.Frame):
    def __init__(self, master, label, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.config(padding=10, borderwidth=2, relief="ridge")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text=label, padding=10, font=('Calibre', 10, 'bold'), anchor='center').grid(column=0, row=0)
