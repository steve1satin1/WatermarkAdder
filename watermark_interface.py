from tkinter import ttk, font
import tkinter as tk

class WatermarkInterface(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.minsize(200, 100)

        self.frame = ttk.Frame(self)
        self.frame.columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.text = tk.StringVar()
        self.text_entry = ttk.Entry(self.frame, justify='center', textvariable=self.text)
        self.text_entry.grid(row=0, column=0, sticky=tk.NSEW)

        self.font_selected = tk.StringVar()
        self.fonts_list = ttk.Combobox(self.frame, textvariable=self.font_selected, state='readonly')
        self.create_fonts()
        self.fonts_list.grid(row=1, column=0, sticky=tk.NSEW)

        self.size = tk.StringVar()
        self.size_entry = ttk.Spinbox(self.frame, from_=1.0, to=100.0, textvariable=self.size)
        self.size_entry.grid(row=2, column=0, sticky=tk.NSEW)



    def create_fonts(self):
        choices = sorted([name for name in font.families()])
        self.fonts_list['values'] = tuple(choices)





