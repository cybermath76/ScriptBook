from PyQt4 import QtGui, QtCore

import sys

class InputDialog(QtGui.QInputDialog):
    def __init__(self, parent = None):
        
        self.header = 'Input'
        self.name   = 'Name'
        
    def Show(self):
        QtGui.QInputDialog.__init__(self)
        self.exec_()
        #self.text, self.ok = QtGui.QInputDialog.getText(self, self.header, self.name) 
        #result = self.exe
        
        
class MessageBox(QtGui.QMessageBox):
    def __init__(self, parent = None):
        self.header = 'Input'
        self.name   = 'Name'
        
    def Show(self):
        QtGui.QMessageBox.__init__(self)
        dialog = QtGui.QMessageBox(4, self.header, self.name, buttons = QtGui.QMessageBox.Ok)
        
        result = dialog.exec_()
        
        
        
        
"""        
app = QtGui.QApplication(sys.argv)
#icon = InputDialog()
#icon.show()
sd = ShowDialog()
sd.header = 'sasha'
sd.Show()
#sd.destroy()
app.exec_() 
"""
"""
app = QtGui.QApplication(sys.argv)
mb  = MessageBox()
mb.Show()
#if mb.result() == 0:
app.exec_() 
"""
       