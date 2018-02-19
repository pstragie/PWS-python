#!usr/bin/python

__author__ = 'pstragie'
__company__ = 'PWS'
hostname = "latitude-e6520"

import os
import sys
import socket

print(socket.gethostname())
if socket.gethostname() != hostname:
    print("Wrong hostname!")
else:
    print("Correct hostname!")
import wx
import wx.lib.scrolledpanel
from countFiles import CountFiles
from checkWebsiteUpdate import CheckForUpdates
from runFromFile import RunFromFile
from reportFromOds import ReadFromOds
clientCompany = "Ipsum Lorem"

class MasterFrame(wx.Frame):
    """
    A Frame with menu bar and output panel
    """
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MasterFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        self.panel_home = MasterPanel(self)
        self.panel_two = CountFiles(self)
        self.panel_three = CheckForUpdates(self)
        self.panel_four = RunFromFile(self)
        self.panel_five = ReadFromOds(self)
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_home, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.sizer.Add(self.panel_three, 1, wx.EXPAND)
        self.sizer.Add(self.panel_four, 1, wx.EXPAND)
        self.sizer.Add(self.panel_five, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.SetTitle("PWS digital solutions")
        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText(sys.version)


    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        homeItem = fileMenu.Append(-1, "&Home\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # A script menu for the scripts
        scriptMenu = wx.Menu()
        countFiles = scriptMenu.Append(-1, "&countFiles...\tCtrl-1", "count files in folder")
        checkWebsiteUpdate = scriptMenu.Append(-1, "&checkSiteUpdate...\tCtrl-2", "check for website update")
        summaryFromOds = scriptMenu.Append(-1, "&summaryFromOds...\tCtrl-3", "make report from multiple ods files")
        scriptMenu.AppendSeparator()
        runFromFile = scriptMenu.Append(-1, "&runFromFile...\tCtrl-R", "run a script from a file")

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(scriptMenu, "&Scripts")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.onHome, homeItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.onCountFiles, countFiles)
        self.Bind(wx.EVT_MENU, self.onCheckWebsiteUpdate, checkWebsiteUpdate)
        self.Bind(wx.EVT_MENU, self.onSummaryFromOds, summaryFromOds)
        self.Bind(wx.EVT_MENU, self.onRunFromFile, runFromFile)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def onHome(self, event):
        """Show home panel"""
        self.SetStatusText("Home")
        self.panel_home.Show()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.Layout()

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("Software designed by PWS", "About Application", wx.OK | wx.ICON_INFORMATION)

    def onCountFiles(self, event):
        """Show countFiles script panel"""
        self.SetStatusText("Count Files in a folder")
        self.panel_home.Hide()
        self.panel_two.Show()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.Layout()

    def onCheckWebsiteUpdate(self, event):
        """Show checkwebsiteupdate script panel"""
        self.SetStatusText("Check website update")
        self.panel_home.Hide()
        self.panel_two.Hide()
        self.panel_three.Show()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.Layout()

    def onSummaryFromOds(self, event):
        """Show report from ods files panel"""
        self.SetStatusText("Make report from ods files")
        self.panel_home.Hide()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Show()
        self.Layout()

    def onRunFromFile(self, event):
        """Show checkwebsiteupdate script panel"""
        self.SetStatusText("Run Script from file")
        self.panel_home.Hide()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Show()
        self.panel_five.Hide()
        self.Layout()

class MasterPanel(wx.Panel):
    """ Home panel """
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        pnl = wx.Panel(self)

        # and put some text with a larger bold font on it
        version = sys.version
        st = wx.StaticText(self, label="Python: "+version, pos=(25,25))
        font = st.GetFont()
        font.PointSize = 8
        font = font.Bold()
        st.SetFont(font)

        # read file names in folder
        curdir = os.getcwd()


        # and put some text on it
        txt = wx.StaticText(self, 1, label="Current directory: " + curdir, pos=(25,40))
        font = txt.GetFont()
        font.PointSize = 10
        font = font.Bold()
        txt.SetFont(font)

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MasterFrame(None, -1, title='Home')
    # set Window size
    frm.SetSize(0,0,640,480)
    # center a window
    frm.Centre()
    frm.Show()
    app.MainLoop()