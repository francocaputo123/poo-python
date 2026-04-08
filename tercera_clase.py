import wx

class MFrame(wx.Frame) :
    def __init__(self):
        super().__init__(None,title='Hola')
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.paneltitle = ''

        self.panel = MyPanel(self)

        self.sizer.Add(self.panel, 1, wx.EXPAND)

        self.SetSizer(self.sizer)

        self.SetSize(600,600)
        self.SetBackgroundColour(wx.RED)
        self.Show()

    def show_another_window(self) :
        self.paneltitle = 
        self.panel.Hide()

        self.panelTwo = PanelTwo(self)
        self.sizer.Add(self.panelTwo, 1, wx.EXPAND)

        self.Layout()

    def close_window(self) :
        self.Destroy()

class PanelTwo(wx.Panel) :
    def __init__(self,parent):
        super().__init__(parent)
        
        self.title = wx.StaticText(self, size=(150, -1))
        self.btn = wx.Button(self, label='Cerrar')

        self.Bind(wx.EVT_BUTTON, self.close_window, self.btn)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.Add(self.btn, 0,wx.ALL, 30)
        self.sizer.Add(self.title, 0,wx.ALL, 30)

        self.SetSizer(self.sizer)

    def close_window(self,event) :
        self.Parent.close_window()


class MyPanel(wx.Panel) :
    def __init__(self,parent):
        super().__init__(parent)

        self.ipt = wx.TextCtrl(self, value='default')
        self.btn = wx.Button(self, label='Get val')
        self.btn_new_window = wx.Button(self, label='New win')
        self.lbl = wx.StaticText(self, size=(100,-1))
        self.lbl.SetForegroundColour(wx.BLACK)
        self.lbl.SetBackgroundColour(wx.BLUE)

        self.Bind(wx.EVT_BUTTON, self.show_lbl, self.btn)
        self.Bind(wx.EVT_BUTTON, self.new_window, self.btn_new_window)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.AddStretchSpacer(prop=1)
        self.sizer.Add(self.ipt,proportion=0, flag=wx.CENTER | wx.ALL, border=5)
        self.sizer.Add(self.btn, proportion=0, flag=wx.CENTER | wx.ALL, border=5)
        self.sizer.Add(self.lbl, proportion=0, flag=wx.CENTER | wx.ALL, border=5)
        self.sizer.Add(self.btn_new_window, proportion=0, flag=wx.CENTER | wx.ALL, border=5)
        self.sizer.AddStretchSpacer(prop=1)
        
        self.SetSizer(self.sizer)

    def show_lbl(self, event) :
        a = self.ipt.GetValue()
        self.lbl.SetLabel(a)
        self.Layout()
    
    def new_window(self,event) :
        self.Parent.show_another_window()
        


app = wx.App()
frame = MFrame()
app.MainLoop()
