import PyPDF2
import wx
import os

app = wx.App(False)


class MainFrame(wx.Frame):
    def __init__(self, parent, title, size=(200, 100)):
        wx.Frame.__init__(self, parent, title=title, size=size)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        file_menu = wx.Menu()

        open_item = file_menu.Append(wx.ID_OPEN, "Open", "Open a file")
        self.Bind(wx.EVT_MENU, self.OnOpen, open_item)

        file_menu.AppendSeparator()

        about_item = file_menu.Append(wx.ID_ABOUT, "About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, about_item)
        exit_item = file_menu.Append(wx.ID_EXIT, "Exit", "Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnExit, exit_item)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "File")
        self.SetMenuBar(menu_bar)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0, 10):
            self.buttons.append(wx.Button(self, -1, "Button " + str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        self.Show(True)

    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def OnExit(self, event):
        self.Close(True)

    def OnOpen(self, event):
        self.path = ""
        dialog = wx.FileDialog(self, "Choose a file", self.path, "", "*.*", wx.ID_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.filename = dialog.GetFilename()
            self.path = dialog.GetDirectory()
            file = open(os.path.join(self.path, self.filename), "r")
            self.control.SetValue(file.read())
            file.close()
        dialog.Destroy()

frame = MainFrame(None, "Small Editor", (600, 400))
app.MainLoop()
