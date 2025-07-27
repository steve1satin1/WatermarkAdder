import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, EpsImagePlugin

class ImageFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.master = kwargs.get('master')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(self, width=300, height=300, background="white")
        self.add_image_butt = ttk.Button(self.master, text="Add Image", command=self.add_image)
        self.save_img_butt = ttk.Button(self.master, text="Save Image", command=self.save_image)

        self.simple_image: Image = None
        self.loaded_image = None

        self.canvas.bind('<Configure>', self.fit_image)

    def add_image(self):
        # Load image
        self.simple_image = Image.open(filedialog.askopenfilename())
        self.fit_image()

    def fit_image(self, event=None):

        # Check if an image has selected
        if not self.simple_image:
            return

        # resize Image
        resized_image = self.simple_image.resize((self.canvas.winfo_width(), self.canvas.winfo_height()))
        # Make image tk compatible
        self.loaded_image = ImageTk.PhotoImage(resized_image)
        # Load image to canvas
        self.canvas.create_image(0, 0, image=self.loaded_image, anchor=tk.NW)

        # Find all texts and put them on top of the image while resizing
        for item in self.canvas.find_withtag('text'):
            self.canvas.lift(item)

        # Update canvas
        self.canvas.update()

    def save_image(self):

        temp_filename = 'temp_image.eps'
        self.canvas.postscript(file=temp_filename, colormode='color')
        img = Image.open(temp_filename)
        img.convert()
        img.save(filedialog.asksaveasfilename() + '.png', 'png')

    def grid(self, *args, **kwargs):
        super().grid(*args, **kwargs)
        self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
