import wx


#se crea una clase para inicializar un nuevo frame o pantalla
class MyFrame(wx.Frame) :
    def __init__(self) :
        super().__init__(None, title='hello world') #para un mejor codigo, usamos super()
        panel = MyPanel(self) #le pasamos self que sera la referencia de frame hacia panel
        self.Show()

class MyPanel(wx.Panel) : #creamos un panel. Este sera contenido por el frame
    def __init__(self, parent) :
        super().__init__(parent)

        button = wx.Button(self, label='Presioname')

app = wx.App()
frame = MyFrame()
app.MainLoop()

