from tkinter import Canvas

class TextItem:
    def __init__(self, menu, canvas: Canvas, x=100, y=100, tags='text'): #text="", font=(), fill='black', tags='text'):
        self.canvas = canvas
        self.menu_opened = False
        self.menu = menu
        self.properties = self.menu.get_properties()
        self.text_created = self.canvas.create_text(
            x, y, text=self.properties['text'],
            font=(self.properties['font'], self.properties['size']),
            fill=self.properties['color'], tags=tags
        )
        self.x, self.y = x, y

        self.canvas.tag_bind(self.text_created, "<Button-1>", self.drag_start)
        self.canvas.tag_bind(self.text_created, '<B1-Motion>', self.mov)
        self.canvas.tag_bind(self.text_created, '<Double-Button-1>', self.change_text)

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

    def change_text(self, event):
        self.menu.open_menu(self.canvas, self.properties, (self.text_created, *self.canvas.coords(self.text_created)))
