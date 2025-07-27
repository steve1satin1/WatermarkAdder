from ipaddress import ip_address
from tkinter import ttk, font, colorchooser
import tkinter as tk

from Tools.demo.sortvisu import steps

from text_item import TextItem
from properties_frame import PropertiesFrame

class WatermarkInterface(tk.Toplevel):
    def __init__(self, canvas: tk.Canvas, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.canvas = canvas

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.minsize(200, 100)

        self.frame = ttk.Frame(self)
        self.frame.columnconfigure(0, weight=1, minsize=100)
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        ## COMPONENTS ##
        # ``Properties`` label
        ttk.Label(self.frame, text="Properties", anchor='center', font=('Calibre', 15, 'bold'), padding=(10, 10)).grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)

        # Text entry
        self.text = tk.StringVar()
        self.text.set("Example text")
        text_frame = PropertiesFrame(self.frame, label='Text')
        self.text_entry = ttk.Entry(text_frame, justify='center', textvariable=self.text, font=('Calibre', 15))
        text_frame.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=10)
        self.text_entry.grid(row=0, column=1, sticky=tk.NSEW)

        # Font
        self.font_selected = tk.StringVar()
        self.font_selected.set('Calibre')
        font_frame = PropertiesFrame(self.frame, label='Font')
        self.fonts_list = ttk.Combobox(font_frame, textvariable=self.font_selected, state='readonly', font=('Calibre', 15))
        self.create_fonts()
        font_frame.grid(row=2, column=0, sticky=tk.NSEW, padx=5, pady=10)
        self.fonts_list.grid(row=0, column=1, sticky=tk.NSEW)

        self.fonts_list.bind("<<ComboboxSelected>>", self.font_selection_fun)

        # Size
        self.size = tk.StringVar()
        size_frame = PropertiesFrame(self.frame, label='Size')
        self.size_entry = ttk.Combobox(size_frame, textvariable=self.size, state='readonly', font=('Calibre', 15, 'bold'))
        self.size_entry.set(20)
        self.create_sizes()
        size_frame.grid(row=3, column=0, sticky=tk.NSEW, padx=5, pady=10)
        self.size_entry.grid(row=0, column=1, sticky=tk.NSEW)

        # Color
        self.color = tk.StringVar()
        self.color.set('red')
        color_frame = PropertiesFrame(self.frame, label='Color')
        self.color_button = tk.Button(color_frame, command=self.set_color, bg='red', fg='red')
        self.color_button.grid(row=0, column=1, sticky=tk.NSEW)
        color_frame.grid(row=4, column=0, sticky=tk.NSEW, padx=5, pady=10)

        self.frame.rowconfigure(5, minsize=50)
        self.done_button = ttk.Button(self.frame, command=self.done, text="Done")
        self.done_button.grid(row=5, column=0, sticky=tk.NS)

    def create_fonts(self):
        choices = sorted([name for name in font.families()])
        self.fonts_list['values'] = tuple(choices)

    def set_color(self):
        self.color = colorchooser.askcolor(initialcolor='#ff0000')
        self.color_button.config(fg=self.color[1], bg=self.color[1])

    def done(self):
        TextItem(self.canvas,
                 text=self.text.get(),
                 font=(self.font_selected.get(), self.size.get()),
                 fill=self.color[1],
                 tags='text')

    def create_sizes(self):
        choices = [num for num in range(1, 100)]
        self.size_entry['values'] = tuple(choices)

    def font_selection_fun(self, ev):
        self.fonts_list.configure(font=(self.font_selected.get(), 15))
        self.text_entry.config(font=(self.font_selected.get(), 15))