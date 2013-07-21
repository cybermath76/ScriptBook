# -*- coding: utf-8 -*-
'''
Created on 20 ���� 2013 �.

@author: Sasha
'''
from PyQt4 import QtGui, QtCore, Qsci, uic
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerPython
import sys
import DialogModule
import ConnectionModule


class CategoryWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("Category.ui")
        self.ui = Form()
        self.ui.setupUi(self)

 
  
 
class CreateScriptForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("createScriptForm.ui")
        self.ui = Form()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.connect(self.ui.pBCancel, QtCore.SIGNAL("clicked()"), self.on_close)
        
        
    def on_close(self):
        self.close()
        

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType("mainForm.ui")
        self.ui = Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('res/bpc.svg'))
        self.connect(self.ui.actionNew, QtCore.SIGNAL("triggered()"), self.on_triggeredNew)
        self.connect(self.ui.actionExit, QtCore.SIGNAL("triggered()"), self.on_triggeredExit)
        #self.connect(self.ui.pBAddScript, QtCore.SIGNAL("clicked()"), self.on_clickedpBAddScript(CreateScriptForm))
        self.ui.pBAddScript.clicked.connect(lambda: self.on_clickedpBAddScript(CreateScriptForm))
        
        lexer = QsciLexerPython()
        #self.ui.tEScriptEditor.lexer = self.ui.tEScriptEditor.QsciLexerPython()
        self.ui.tEScriptEditor.setLexer(lexer)

    def on_clickedpBAddScript(self, widget):
        windowAddScript = widget(self)
        windowAddScript.show()
        
        
    def on_triggeredNew(self):

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
    
