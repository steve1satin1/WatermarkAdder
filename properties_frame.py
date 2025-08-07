from tkinter import ttk

class PropertiesFrame(ttk.Frame):
    def __init__(self, master, label, *args, **kwargs):

        """
        A frame that has cosmetic purpose. Every element in the watermark interface is being contained inside propertie
        frame.
        :param master: The master widget in which the frame will be created.
        :param label: The label of the widget that the frame will contain.
        :param args: tk.Frame arguments passed to tk.Frame.
        :param kwargs: tk.Frame keyword arguments passed to tk.Frame.
        """

        super().__init__(master, *args, **kwargs)

        self.config(padding=10, borderwidth=2, relief="ridge")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        ttk.Label(self, text=label, padding=10, font=('Calibre', 10, 'bold'), anchor='center').grid(column=0, row=0)
