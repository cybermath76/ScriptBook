# -*- coding: utf-8 -*-
'''
Created on 20 ���� 2013 �.

@author: Sasha
'''
from PyQt4 import QtGui, QtCore, uic
import sys
import DialogModule
import ConnectionModule

"""
def on_triggered():
    sd = DialogModule.ShowDialog()
    sd.header = 'Create dataBase' 
    sd.name   = 'Inpute DB'   
    sd.show()
"""

    
    
class CategoryWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("Category.ui")
        self.ui = Form()
        self.ui.setupUi(self)
 #       self.windowModality()
 
 
 
 
 
class CreateScriptForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("createScriptForm.ui")
        self.ui = Form()
        self.ui.setupUi(self)
#        self.windowModality()
        
        

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("mainForm.ui")
        self.ui = Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('res/bpc.svg'))
        self.connect(self.ui.actionNew, QtCore.SIGNAL("triggered()"), self.on_triggeredNew)
        self.connect(self.ui.actionExit, QtCore.SIGNAL("triggered()"), self.on_triggeredExit)
        self.connect(self.ui.pBAddScript, QtCore.SIGNAL("clicked()"), self.on_clickedpBAddScript)
        
    def on_clickedpBAddScript(self):
        windowAddScript = CreateScriptForm()
        windowAddScript.create()
        windowAddScript.show()
        
        
        
    def on_triggeredNew(self):
        """
        iD = DialogModule.InputDialog()
        iD.header = 'Create dataBase'
        iD.name   = 'Inpute DB'
        iD.Show()
        id.
        #resultDB, resultOK = id.getText(self, self.header, self.name)
        #result = iD.Show()
       # resultDB = iD.text
        resultOK = iD.Ok
        if resultOK:
            ConnectionModule.ConnectToDB(resultDB)
        else:
            print("Error create DB")
        """
        global sqlWorker_sW 
        
        header = 'Create dataBase'
        name   = 'Inpute DB'
        resultDB, resultOK = QtGui.QInputDialog.getText(self, header, name)
        sqlWorker_sW = ConnectionModule.SQLiteWorker(resultDB)
        
        
        if resultOK:
            #ConnectionModule.ConnectToDB(resultDB)
            sqlWorker_sW.ConnectToDB()
        else:
            print("Error create DB")  
            
    def on_triggeredExit(self):
        self.close()      
        



if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    window = MainForm()
    
    window.show()
    
    sys.exit(app.exec_())
    
