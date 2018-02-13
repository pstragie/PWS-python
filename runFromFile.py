__author__ = 'pstragie'

import os
import sys
import wx
import wx.lib.scrolledpanel
import subprocess

class RunFromFile(wx.Panel):
    """ Count Files script panel"""
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)


        # put some text in it
        info = wx.StaticText(self, label="This script allows you to run a script from a file.", pos=(25, 15))
        kiesFolder = wx.StaticText(self, label="Kies python script", pos=(25, 40))
        dirSelectorPromptStr = "Kies folder"
        DIRP_DEFAULT_STYLE = wx.DIRP_DIR_MUST_EXIST
        DirPickerCtrlNameStr = "test Picker"
        #self.chosenfolder = wx.DirPickerCtrl(self, id=1, path="", message=dirSelectorPromptStr, pos=(25, 70), style=DIRP_DEFAULT_STYLE, name=DirPickerCtrlNameStr)
        self.chosenfile = wx.FilePickerCtrl(self, id=1, path="", message="Select a python file", pos=(25, 70), size=(500, -1))
        self.button = wx.Button(self, label="Run script", pos=(25, 170))
        self.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, event):

        #self.frame = wx.Frame(None, -1, title='Redirect Test', size=(620,450), style=wx.STAY_ON_TOP | wx.DEFAULT_FRAME_STYLE)
        panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, pos=(25, 260), size=(505, 155), style=wx.BORDER_RAISED)
        panel.SetupScrolling()

        self.log = wx.TextCtrl(panel, -1, size=(500, 150), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        redir = RedirectText(self.log)
        sys.stdout = redir

        chosenfile = self.chosenfile.GetPath()
        name, ext = os.path.splitext(chosenfile)
        if chosenfile == "":
            wx.MessageBox("Geen bestand geselecteerd", "Selecteer eerst een bestand", wx.OK | wx.ICON_INFORMATION)
        elif ext != ".py":
            print("extensie: ", ext)
            wx.MessageBox("Fout bestand!", "Kies een python bestand (.py)", wx.OK | wx.ICON_INFORMATION)
        else:
            proc = subprocess.Popen(['python', chosenfile], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in proc.stdout:
                print(line.rstrip().decode('UTF-8'))

        file = wx.StaticText(self, label=chosenfile, pos=(25, 200))

        return True


class RedirectText:
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        self.out.WriteText(string)