# -*- coding: utf-8 -*-
import os
import sqlite3

import DialogModule


class SQLiteWorker():
    def __init__(self, dbName):
        self.dbName = dbName
        if os.path.exists('../db/' + dbName):
            flagExistsDB = 1
        else:
            flagExistsDB = 0
            
    def __del__(self):
        self.con.close()
        
    def ConnectToDB(self):
        if os.path.exists('../db/' + self.dbName):
            mb  = DialogModule.MessageBox()
            mb.Show()
            if mb.result() != 0:
                return print("File exists")
        
            else:
                return print("Ok") 
        
        else:
            dbName      = "./db/"  + self.dbName + ".sqlite"
            self.con    = sqlite3.connect(dbName)
            mb          = DialogModule.MessageBox()
            mb.header   = 'Message'
            mb.name     = 'DataBase was created'
            mb.Show()
    

     
