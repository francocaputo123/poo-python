import wx 

#se crea una subclase de panel para la imagen
class ImagePanel(wx.Panel) :

    def __init__(self, parent, image_size) :
        super().__init__(parent)
        self.max_size = 1000

        img = wx.Image(*image_size) #se pasa una tupla del ancho y alto. El * indica a python que se le pasara una tupla o array
        self.image_ctrl = wx.StaticBitmap(self, bitmap=wx.Bitmap(img))

        browse_btn = wx.Button(self, label='Elegir imagen')
        self.Bind(wx.EVT_BUTTON, self.on_browse, browse_btn)

        self.photo_txt = wx.TextCtrl(self, size=(200, -1))

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        main_sizer.Add(self.image_ctrl, 0, wx.ALL, 5)
        hsizer.Add(browse_btn, 0, wx.ALL, 5)
        hsizer.Add(self.photo_txt, 0, wx.ALL, 5)
        main_sizer.Add(hsizer, 0, wx.ALL, 5)

        self.SetSizer(main_sizer)
        main_sizer.Fit(parent)
        self.Layout()

    def on_browse(self, event) :
        '''
        Evento para navegar y buscar una imagen
        '''

        wildcard = "JPEG files (*.jpg) | *.jpg" #esto permite decirle a python que tipo de archivos permitimos tomar.
        with wx.FileDialog(None, "Choose a file", style=wx.FD_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK :
                self.photo_txt.SetValue(dialog.GetPath())
                self.load_image()

    def load_image(self) :
        '''
        Carga la imagen y la desplega al usuario
        '''
        filepath = self.photo_txt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)

        #preservar el aspecto
        W = img.GetWidth()
        H = img.GetHeight()

        if W > H :
            NewW = self.max_size
            NewH = self.max_size * H / W
        else :
            NewH = self.max_size
            NewW = self.max_size * W / H
        img = img.Scale(int(NewW), int(NewH))

        self.image_ctrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()