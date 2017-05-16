# encoding: utf8
import wx
import os
from MainFrame import MainFrame
if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    if not os.path.exists('script18.log'):
        wx.MessageBox('Файл лога не найден. Файл будет создан автоматически.',
                      'Файл лога не найден!',
                      wx.OK | wx.ICON_INFORMATION)
        open('script.log', 'w').close()

    app.MainLoop()
