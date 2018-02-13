__author__ = 'pstragie'

#import os
import sys
import wx
import wx.lib.scrolledpanel
import webbrowser

class CheckForUpdates(wx.Panel):
    """ Check web site update script panel"""
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)


        # put some text in it
        info = wx.StaticText(self, label="This script will check if a website has updated yet.", pos=(25, 15))
        kiesURL = wx.StaticText(self, label="Vul url in:", pos=(25, 40))
        self.chosenURL = wx.TextCtrl(self, -1, pos=(25, 70), size=(300, -1))
        tijdsInterval = wx.StaticText(self, label="Tijdsinterval (minuten):", pos=(25, 100))
        self.chosenTijdsInterval = wx.TextCtrl(self, pos=(25, 130))

        self.button = wx.Button(self, label="Run script", pos=(25, 170))
        self.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, event):

        # scrolled panel
        panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, pos=(25, 260), size=(505, 155), style=wx.BORDER_RAISED)
        panel.SetupScrolling()

        self.log = wx.TextCtrl(panel, -1, size=(500, 150), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        redir = RedirectText(self.log)
        sys.stdout = redir

        # script
        chosenInterval = self.chosenTijdsInterval.GetValue()
        chosenUrl = self.chosenURL.GetValue()
        if chosenUrl != "":
            url = chosenUrl
            print(url)
        else:
            print("No url entered.")

        #chosenUrl = wx.StaticText(self, label=chosenUrl, pos=(25, 200))
        print(chosenInterval)

        self.checkCurrentStatus()
        return True

    def checkCurrentStatus(self):
        webbrowser.open(self.chosenURL.GetValue())
        return True

class RedirectText:
    def __init__(self, aWxTextCtrl):
        self.out=aWxTextCtrl

    def write(self, string):
        self.out.WriteText(string)