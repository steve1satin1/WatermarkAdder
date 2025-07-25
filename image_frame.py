import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class ImageFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.canvas = tk.Canvas(self, width=300, height=300)
        self.add_image_butt = ttk.Button(self, text="Add Image", command=self.add_image)

        self.simple_image = None
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
        # resize image
        resized_image = self.simple_image.resize((self.canvas.winfo_width(), self.canvas.winfo_height()))
        # Make image tk compatible
        self.loaded_image = ImageTk.PhotoImage(resized_image)
        # Load image to canvas
        self.canvas.create_image(5, 5, image=self.loaded_image, anchor=tk.NW)

        # Find all texts and put them on top of the image while resizing
        for item in self.canvas.find_withtag('text'):
            self.canvas.lift(item)

        # Update canvas
        self.canvas.update()

    def grid(self, *args, **kwargs):
        super().grid(*args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W), columnspan=2)
        self.add_image_butt.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))
