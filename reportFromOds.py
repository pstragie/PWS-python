#!usr/bin/python

__author__ = 'pstragie'

import os
import sys
import wx
import wx.lib.scrolledpanel
from pyexcel_ods3 import get_data
import json

class ReadFromOds(wx.Panel):
    """ Count Files script panel"""
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.dataDictionary = {}
        # self.frame = wx.Frame(None, -1, title='Redirect Test', size=(620,450), style=wx.STAY_ON_TOP | wx.DEFAULT_FRAME_STYLE)
        panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, pos=(25, 260), size=(505, 155), style=wx.BORDER_RAISED)
        panel.SetupScrolling()

        self.log = wx.TextCtrl(panel, -1, size=(500, 150), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        redir = RedirectText(self.log)
        sys.stdout = redir

        # put some text in it
        info = wx.StaticText(self, label="This script will summarize all ods files in a folder.", pos=(25, 15))
        kiesFolder = wx.StaticText(self, label="Kies folder", pos=(25, 40))
        dirSelectorPromptStr = "Kies folder"
        DIRP_DEFAULT_STYLE = wx.DIRP_DIR_MUST_EXIST
        DirPickerCtrlNameStr = "test Picker"
        self.chosenfolder = wx.DirPickerCtrl(self, id=1, path="", message=dirSelectorPromptStr, pos=(25, 70), style=DIRP_DEFAULT_STYLE, name=DirPickerCtrlNameStr)

        self.button = wx.Button(self, label="Run script", pos=(25, 170))
        self.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, event):
        chosenfolder = self.chosenfolder.GetPath()
        if chosenfolder == "":
            chosendirectory = os.getcwd()
        else:
            chosendirectory = chosenfolder
        count = 0
        print("Path: ", chosenfolder)
        for (dp, dn, fn) in os.walk(chosendirectory):
            for f in fn:
                name, ext = os.path.splitext(f)
                if ext == ".ods":  # xls or xlsx for windows
                    count += 1
        wx.MessageBox("Aantal bestanden: \(count)", "Doorgaan?", wx.OK | wx.ICON_INFORMATION)
        for (dp, dn, fn) in os.walk(chosendirectory):
            for f in fn:
                name, ext = os.path.splitext(f)
                if ext == ".ods":  # xls or xlsx for windows
                    self.storeDataInDictionary(os.path.join(dp, f), f)
        #fold = wx.StaticText(self, label=chosendirectory, pos=(25, 200))
        #total = wx.StaticText(self, label=counttxt, pos=(25, 220))
        print("Gevonden: \(count)")
        return True

    def storeDataInDictionary(self, path, file):
        print("Reading from file: ", path)
        data = get_data(path)
        print(json.dumps(data))
        data2 = get_data(file)
        print(json.dumps(data2))
        self.dataDictionary[file] = json.dumps(data)
        print("Dictionary: ", self.dataDictionary)

class RedirectText:
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        self.out.WriteText(string)