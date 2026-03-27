import wx

class MyFrame(wx.Frame) :
    def __init__(self) :
        super().__init__(parent=None, title='Prueba')
        panel = MyPanel(self)
        self.Show()

class MyPanel(wx.Panel) :
    def __init__(self, parent) :
        super().__init__(parent)

        button = wx.Button(self, label='Presioname')
        button2 = wx.Button(self, label='Presioname a mi')
        input_txt = wx.TextCtrl(self, size=(100,100 ))
        input_txt.Bind()

        #sizers, basicamente, contenedores de otros widgets
        main_sizer = wx.BoxSizer(wx.HORIZONTAL) #se crea un sizer horizontal

        main_sizer.Add(button, proportion = 0,flag = wx.ALL | wx.CENTER, border = 5)
        main_sizer.Add(button2, 0, wx.ALL, 5)
        self.SetSizer(main_sizer)



app = wx.App()
frame = MyFrame()
app.MainLoop()