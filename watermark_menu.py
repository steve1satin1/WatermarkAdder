from tkinter import ttk
import tkinter as tk
from watermark_interface import WatermarkInterface

class WatermarkMenu(ttk.Frame):

    def __init__(self, master, canvas, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.canvas = canvas
        self.start_button = ttk.Button(self, text="Create Text", command=self.open_menu)
        self.menu_opened = 0
        self.menu = None

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


    def open_menu(self):
        """
        Controls the ``Create Text`` button. It Opens and closes the menu for the text creation.
        :return: None
        """
        if self.menu and tk.Toplevel.winfo_exists(self.menu):
            self.menu.destroy()
        else:
            self.menu = self.create_menu()

    def create_menu(self):
        """
        Creates a Toplevel window of type WatermarkInterface that represents the menu for the text creation.
        :return: WatermarkInterface object.
        """
        menu = WatermarkInterface(canvas=self.canvas)
        menu.title("Watermark")
        return menu

    def grid(self, *args, **kwargs):
        super().grid(*args, **kwargs)
        self.start_button.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

