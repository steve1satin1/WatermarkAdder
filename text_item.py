from tkinter import Canvas

class TextItem:
    def __init__(self, menu, canvas: Canvas, x=100, y=100, tags='text'): #text="", font=(), fill='black', tags='text'):

        self.canvas = canvas
        self.menu_opened = False
        self.menu = menu
        # Extract the properties from watermark interface.
        self.properties = self.menu.get_properties()
        # Create the text on the canvas.
        self.text_created = self.canvas.create_text(
            x, y, text=self.properties['text'],
            font=(self.properties['font'], self.properties['size']),
            fill=self.properties['color'], tags=tags, angle=self.properties['angle']
        )
        # Save the coordinates of the created text.
        self.x, self.y = x, y
        # Bind the events for moving the text and changing it.
        self.canvas.tag_bind(self.text_created, "<Button-1>", self.drag_start)
        self.canvas.tag_bind(self.text_created, '<B1-Motion>', self.mov)
        self.canvas.tag_bind(self.text_created, '<Double-Button-1>', self.change_text)
        # Update the canvas to show the new text (not necessary).
        self.canvas.update()

    def drag_start(self, event):
        """
        This method is called when a mouse button is pressed inside the text item.
        Just saves the start coordinates of the text item.
        :param event: The mouse event.
        :return: None
        """
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def mov(self, event):
        """
        This method is called when the mouse is pressed and moves.
        It moves the text item to based on the coordinates of the mouse.
        :param event: The mouse event.
        :return: None
        """
        widget = event.widget
        widget.move(self.text_created, event.x - widget.startX, event.y - widget.startY)
        widget.startX, widget.startY = event.x, event.y  # update previous position
        self.canvas.update()

    def change_text(self, event):
        """
        This method is called when the user double-clicks the text item.
        It opens a watermark interface menu to let the user change the text item.
        :param event: The mouse event.
        :return: None
        """
        self.menu.open_menu(self.canvas, self.properties, (self.text_created, *self.canvas.coords(self.text_created)))
