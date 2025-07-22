from tkinter import ttk
import tkinter as tk
from watermark_interface import WatermarkInterface

class WatermarkMenu(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.start_button = ttk.Button(self, text="W", command=self.open_menu)
        self.menu_opened = False
        self.menu = None


    def open_menu(self):

        if not self.menu_opened:
            # Mark menu opened
            self.menu_opened = True
            # Open menu
            self.menu = self.create_menu()
        else:
            self.menu.destroy()
            self.menu_opened = False

    def create_menu(self):
        menu = WatermarkInterface()
        menu.title("Watermark")
        return menu

    def grid(self, *args, **kwargs):
        super().grid(*args, **kwargs)

        self.start_button.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

