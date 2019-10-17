import wx

class ApplicationName(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Title',size=(300,200))
		panel = wx.Panel(self)

		box =wx.TextEntryDialog(None, "How old are you?","default text")
		if box.ShowModal() == wx.ID_OK:
			answer = box.GetValue()

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = ApplicationName(parent=None, id=-1)
	frame.Show()
	app.MainLoop()