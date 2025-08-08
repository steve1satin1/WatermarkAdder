from tkinter import ttk, font, colorchooser
import tkinter as tk
from text_item import TextItem
from properties_frame import PropertiesFrame

class WatermarkInterface(tk.Toplevel):
    def __init__(self, canvas: tk.Canvas, text='Example text', font='Calibre', size=20, color='red', rotation='0.0', *args, **kwargs):
        """
        The menu which the user can select the properties that he/she wants the text item to have.
        It handles the text changes.
        :param canvas: The canvas in which the text item will be created.
        :param text: The text which the text item will contain. (For already created text items).
        :param font: The text font (For already created text items).
        :param size: The text size (For already created text items).
        :param color: The text color (For already created text items).
        :param rotation: The text rotation (For already created text items).
        :param args: extra arguments passed to the tk.Toplevel() constructor.
        :param kwargs: extra arguments passed to the tk.Toplevel() constructor.
        """
        super().__init__(*args, **kwargs)

        self.menu_opened = True
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.previous_text_properties = None

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
        self.text.set(text)
        text_frame = PropertiesFrame(self.frame, label='Text')
        self.text_entry = ttk.Entry(text_frame, justify='center', textvariable=self.text, font=('Calibre', 15))
        text_frame.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=10)
        self.text_entry.grid(row=0, column=1, sticky=tk.NSEW)

        # Font
        self.font_selected = tk.StringVar()
        self.font_selected.set(font)
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
        self.size_entry.set(size)
        self.create_sizes()
        size_frame.grid(row=3, column=0, sticky=tk.NSEW, padx=5, pady=10)
        self.size_entry.grid(row=0, column=1, sticky=tk.NSEW)

        # Rotation
        self.rotation = tk.DoubleVar()
        self.rotation.set(float(rotation))
        rotation_frame = PropertiesFrame(self.frame, label='Rotation')
        self.rotation_lb = ttk.Label(rotation_frame, text=self.update_scale_label(rotation), font=('Calibre', 10))
        self.rotation_scale = ttk.Scale(rotation_frame, from_= -180, to= 180, orient=tk.HORIZONTAL, value=0,
                                        variable=self.rotation, command=self.update_scale_label)
        rotation_frame.grid(row=4, column=0, sticky=tk.NSEW, padx=5, pady=10)
        self.rotation_scale.grid(row=0, column=1, sticky=tk.NSEW)
        self.rotation_lb.grid(row=0, column=2, sticky=tk.NSEW)


        # Color
        self.color = tk.StringVar()
        self.color.set(color)
        color_frame = PropertiesFrame(self.frame, label='Color')
        self.color_button = tk.Button(color_frame, command=self.set_color, bg=color, fg=color)
        self.color_button.grid(row=0, column=1, sticky=tk.NSEW)
        color_frame.grid(row=5, column=0, sticky=tk.NSEW, padx=5, pady=10)

        self.frame.rowconfigure(5, minsize=50)
        self.done_button = ttk.Button(self.frame, command=self.done, text="Done")
        self.done_button.grid(row=6, column=0, sticky=tk.NS)

        self.text_item_id = None

    def create_fonts(self):
        """
        Creates the fonts list.
        :return: None
        """
        choices = sorted([name for name in font.families()])
        self.fonts_list['values'] = tuple(choices)

    def set_color(self):
        """
        Sets the color of the text.
        :return:
        """
        self.color = colorchooser.askcolor(initialcolor='#ff0000')
        self.color_button.config(fg=self.color[1], bg=self.color[1])

    def done(self):
        """
        Creates the text item when the user clicks 'Done'.
        :param ev: The event that triggered the method.
        :return: None
        """
        # For already created text items that the user wants to change.
        p_x = 100
        p_y = 100
        # Check if there is already a text created from this menu and delete it for the new to add.
        if self.previous_text_properties:
            p_id = self.previous_text_properties[0]
            p_x, p_y = self.canvas.coords(p_id)
            self.canvas.delete(p_id)

        # Create the new text item
        self.text_item_id = TextItem(self, self.canvas, p_x, p_y, tags='text')
        self.menu_opened = False
        self.destroy()





    def create_sizes(self):
        """
        Creates the sizes list.
        :return: None
        """
        choices = [num for num in range(1, 100)]
        self.size_entry['values'] = tuple(choices)

    def font_selection_fun(self, ev):
        """
        Every time a user chooses a new font this function changes the font
        in the text and font entry so that the change will be visible.
        :param ev: the select font event from the fonts list.
        :return: None
        """
        self.fonts_list.configure(font=(self.font_selected.get(), 15))
        self.text_entry.config(font=(self.font_selected.get(), 15))

    def extract_color(self):
        """
        Extracts the color from the color pallet.
        :return:
        """
        try: # If the color comes from the color pallet
            color = self.color[1]
        except: # else the color comes from the color string variable.
            color = self.color.get()
        print('returned color: ', color)
        return color

    def get_properties(self):
        """
        Gets the properties set in the properties frame
        :return: dictionary of the properties in this form {'text': ..., 'font': ..., 'size': ..., 'color': ...}
        """
        properties = {
            'text': self.text.get(),
            'font': self.font_selected.get(),
            'size': self.size_entry.get(),
            'angle': self.rotation.get(),
            'color': self.extract_color()
        }
        return properties

    def open_menu(self, canvas, properties, previous_text_properties: tuple):
        """
        This method gets called from the text item when the user double clicks it.
        :param canvas: The canvas in which the new text will be drawn.
        :param properties: The properties of the text item which the user wants to change.
        :param previous_text_properties: A tuple containing (text, x coord, y coord) from previous text.
        :return:
        """
        if not self.menu_opened:
            self.__init__(canvas, properties['text'], properties['font'], properties['size'], properties['color'], rotation=properties['angle'])
            self.previous_text_properties = previous_text_properties

    def on_closing(self):
        self.menu_opened = False
        self.destroy()

    def update_scale_label(self, val):
        """
        Updates the scale label. and also sets the rotation label when text first created or changes.
        :param event: The widget event
        :return: None
        """
        val = float(val)
        val = round(val, 1)
        try:
            self.rotation_lb.config(text=f"{val}")
        except:
            return str(val)

