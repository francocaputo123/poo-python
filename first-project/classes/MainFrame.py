import wx
from image_panel import ImagePanel

class MainFrame(wx.Frame) :

    def __init__(self):
        super().__init__(None, title='Image viewer')
        panel = ImagePanel(self, image_size=(400,400))
        self.Show()

app = wx.App()
frame = MainFrame()
app.MainLoop()