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

        button = wx.Button(self, label='Presioname', pos=(100,100)) 
        
        self.Bind(wx.EVT_BUTTON, self.panel_handler, button)
        button.Bind(wx.EVT_BUTTON, self.on_press)
        '''
        Se pasan dos argumentos: el evento y la funcion que cumplira ese evento.
        Otra manera de pasar el boton y el evento es usando self
        self.Bind(wx.EVT_BUTTON, self.on_on press, button) esto "envuelve" la funcion dentro del panel y ademas
        permite utilizar multiples objetos como los botones.
        '''
        #button.Bind(wx.EVT_BUTTON, self.on_press) #los eventos se pasan a traves de Bind.

        '''
        La funcion que dispare el evento tiene que tener event. Este es un objeto de wxPython 
        que tiene la informacion de quien llamo al evento y otro tipo de informacion.

        '''
    def panel_handler(self, event) :
        print('Llamaste a panel_handler')

    def on_press(self, event) :
        print('Presionaste el boton')
        event.Skip() #ell boton tiene dos llamadas, este evento propaga el llamado de funciones a la siguiente (si hay mas eventos en el boton)

app = wx.App()
frame = MyFrame()
app.MainLoop()

