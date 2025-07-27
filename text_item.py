from tkinter import Canvas

class TextItem:
    def __init__(self, canvas: Canvas, x=100, y=100, text="", font=(), fill='black', tags='text'):

        self.canvas = canvas
        self.text_created = self.canvas.create_text(x, y, text=text, font=font, fill=fill, tags=tags)

        self.canvas.tag_bind(self.text_created, "<Button-1>", self.drag_start)
        self.canvas.tag_bind(self.text_created, '<B1-Motion>', self.mov)

        self.canvas.update()

    def drag_start(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def mov(self, event):
        widget = event.widget
        widget.move(self.text_created, event.x - widget.startX, event.y - widget.startY)
        widget.startX, widget.startY = event.x, event.y  # update previous position
        self.canvas.update()

