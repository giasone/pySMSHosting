# -*- coding: utf-8 -*-
#!/usr/bin/env python

# client.py 

#    Copyright (C) 2010 Gianluca Urgese <g.urgese@jasone.it>    
#    
#	 pySmsHosting is a library for Python that wraps the SmsHosting.it Web Service API.
#	
#	 Questions, comments? g.urgese@jasone.it
#
#    pySmsHosting is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    pySmsHosting is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pySmsHosting.  If not, see <http://www.gnu.org/licenses/>.
#    
#

import sys
import ConfigParser
import string
from smshosting import *
from PyQt4 import QtGui, QtCore

__license__ = 'GPL v.2 http://www.gnu.org/licenses/gpl.txt'
__author__ = "Gianluca Urgese <g.urgese@jasone.it>"
__version__ = '0.4'

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        #config
        config = ConfigParser.ConfigParser()
        config.read("./config.ini")
        self.username = config.get("user", "username")
        self.password = config.get("user", "password")
        self.host = config.get("user", "host")
        self.sender = config.get("user", "sender")
        
        self.setWindowTitle('SMS Desktop Client')
        self.setWindowIcon(QtGui.QIcon('icons/book_open.png'))

        self.createMenu()
        self.statusBar()
        
        self.resize(420, 350)
        
        self.widget = QtGui.QWidget()

        self.title = QtGui.QLabel('Sender')
        self.author = QtGui.QLabel('Number')
        self.review = QtGui.QLabel('Text')

        self.titleEdit = QtGui.QLineEdit()
        self.titleEdit.setText(unicode(self.sender))
        self.authorEdit = QtGui.QLineEdit()
        self.reviewEdit = QtGui.QTextEdit()
        
        self.addressBook = QtGui.QPushButton('', self.widget)
        self.addressBook.setIcon(QtGui.QIcon('icons/book_open.png'))
        self.connect(self.addressBook, QtCore.SIGNAL('clicked()'), self.openAddressBook)

        self.grid = QtGui.QGridLayout(self.widget)
        self.grid.setSpacing(10)

        self.grid.addWidget(self.title, 1, 0)
        self.grid.addWidget(self.titleEdit, 1, 1, 1, 2)

        self.grid.addWidget(self.author, 2, 0)
        self.grid.addWidget(self.authorEdit, 2, 1)
        self.grid.addWidget(self.addressBook, 2, 2)

        #self.grid.addWidget(self.review, 3, 0)
        self.grid.addWidget(self.reviewEdit, 3, 0, 1, 3)


        self.widget.setLayout(self.grid)
        self.setCentralWidget(self.widget)
        
        self.center()

    def createMenuVoice(self, iconPath, name, shortcut, tip, slot):
        voice = QtGui.QAction(QtGui.QIcon(iconPath), name, self)
        voice.setShortcut(shortcut)
        voice.setStatusTip(tip)
        self.connect(voice, QtCore.SIGNAL('triggered()'), slot)

        return voice

    def createSeparator(self):
        sVoice = QtGui.QAction(self)
        sVoice.setSeparator(True)
        return sVoice

    def createMenu(self):
        tinyMenu = self.menuBar()

        file = tinyMenu.addMenu("&File")
        #edit = tinyMenu.addMenu("&Edit")
        help = tinyMenu.addMenu("Help")

        new = self.createMenuVoice("icons/new.png", "New", "Ctrl+N", "New SMS", self.clearField)
        open = self.createMenuVoice("icons/open.png", "Open file", "Ctrl+O", "Open a new file", self.openNewFile)
        save = self.createMenuVoice("icons/save.png", "Save file", "Ctrl+S", "Save As File", self.saveNewFile)
        sep1 = self.createSeparator()
        send = self.createMenuVoice("icons/send.png", "Send", "Ctrl+S", "Send SMS", self.smsSend)
        sep2 = self.createSeparator()
        info = self.createMenuVoice("icons/info.png", "About", "Ctrl+A", "About SMSHostingDesktopClient", self.about)
        quit = self.createMenuVoice("icons/exit.png", "Quit", "Ctrl+Q", "Quit SMSHostingDesktopClient", QtCore.SLOT('close()'))
        file.addAction(new)
        file.addAction(open)
        file.addAction(save)
        file.addAction(sep1)
        file.addAction(send)
        file.addAction(sep2)
        file.addAction(quit)
        help.addAction(info)
        
        #toolbar
        toolbar = self.addToolBar('Tools')
        toolbar.addAction(new)
        toolbar.addAction(open)
        toolbar.addAction(save)
        toolbar.addAction(sep1)
        toolbar.addAction(send)
        toolbar.addAction(sep2)
        toolbar.addAction(info)
        toolbar.addAction(quit)
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)


        
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, 
	    (screen.height()-size.height())/2)

    def openNewFile(self):
        fName = QtGui.QFileDialog.getOpenFileName(self, "Open text file", "Open new file", self.tr("Text Files (*.txt)"))

        if fName.isEmpty() == False:
            fptr = open(fName, 'r')
            content = fptr.read()
            self.reviewEdit.append(content)
            fptr.close()

    def saveNewFile(self):
        fName = QtGui.QFileDialog.getSaveFileName(self, "Save SMS as text file", "Save SMS as new file", self.tr("Text Files (*.txt)"))

        if fName.isEmpty() == False:
            fptr = open(fName, 'w')

            fptr.write(self.reviewEdit.toPlainText())
            fptr.close()

    def smsSend(self):
        
        test1 = smshosting.ManageSmsService(self.username, self.password, self.host)
        
        #test1.setNumber('393939969555', '')
        #test1.setNumber('393932222255', '')
        #test1result1 = test1.send(text, sender)
        #print test1result1
        text = unicode(self.reviewEdit.toPlainText())
        sender = unicode(self.titleEdit.text())
        test1.setNumber(self.authorEdit.text(), '')
        test1result2 = test1.testSend(text, sender)
        print test1result2
        self.clearField()
        return
        
    def clearField(self):

        self.authorEdit.clear()
        self.reviewEdit.clear()
        return
        
    def openAddressBook(self):
        print "rubrica"
        return
        
    def about(self):
         QtGui.QMessageBox.about(self, 'SMS Desktop Client', \
                          "<b>SMSHosting Desktop Client</b> v.\n"+ __version__ + \
                          "<p>pySMSHosting is complete and easy to use Python " + \
                          "SOAP module to interact with SMSHosting.it API.</p><br />" + \
                          "Author: "+__author__ + "<br />" +\
                          "License: "+__license__ + \
                          "<p>More on <a href=\"http://giasone.wordpress.com/\">http://giasone.wordpress.com</a></p>")
                          
                          
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())