import tkinter as tk
from tkinter import ttk
from image_frame import ImageFrame
from watermark_menu import WatermarkMenu

root = tk.Tk()

main_frame = ttk.Frame(root, width=300, height=300)
main_frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame.columnconfigure(0, weight=1)
# main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
image_frame = ImageFrame(main_frame)
image_frame.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W), columnspan=2)

menu = WatermarkMenu(main_frame, canvas=image_frame.canvas)
menu.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

root.mainloop()

# print(ttk.Frame().config())