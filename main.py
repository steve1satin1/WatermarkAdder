import tkinter as tk
from tkinter import ttk
from image_frame import ImageFrame
from watermark_menu import WatermarkMenu

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# style = ttk.Style(root)
# root.tk.call('source', 'tkBreeze-master/tkBreeze-master/breeze-dark/breeze-dark.tcl')
# style.theme_use('breeze-dark')

main_frame = ttk.Frame(root, width=300, height=300)
main_frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

main_frame.rowconfigure(0, minsize=50)
main_frame.rowconfigure(1, weight=1, minsize=50)

main_frame.columnconfigure((0,1,2), weight=1)

image_frame = ImageFrame(master=main_frame, style='Frame1.TFrame')
image_frame.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W), columnspan=3)

menu = WatermarkMenu(main_frame, canvas=image_frame.canvas)

# PLACE COMPONENTS #
# Add Image button
image_frame.add_image_butt.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
# Create text button
menu.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
# Save image button
image_frame.save_img_butt.grid(column=2, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

root.mainloop()
