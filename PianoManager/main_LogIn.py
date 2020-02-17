import sys
from functools import partial
from PySide2.QtCore import Slot
from PySide2.QtWidgets import *
from ui_LogIn import Ui_LogIn
from reader_for_login_test import TestDatabaseReader
from NFC.NFCReaderForTest import NFCReader
    

class LogIn(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        # Database Reader Module
        self.dbReader = TestDatabaseReader()
        # NFC Reader Thread
        self.nfcReader = NFCReader()
        self.nfcReader.start()

        # UI for the page
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)

        # hide dialogue
        self.ui.DialogueShadow.hide()

        # Insert buttons into QButtonGroup
        self.keypadButtons = QButtonGroup()
        self.keypadButtons.addButton(self.ui.KeypadButton_0, 0)
        self.keypadButtons.addButton(self.ui.KeypadButton_1, 1)
        self.keypadButtons.addButton(self.ui.KeypadButton_2, 2)
        self.keypadButtons.addButton(self.ui.KeypadButton_3, 3)
        self.keypadButtons.addButton(self.ui.KeypadButton_4, 4)
        self.keypadButtons.addButton(self.ui.KeypadButton_5, 5)
        self.keypadButtons.addButton(self.ui.KeypadButton_6, 6)
        self.keypadButtons.addButton(self.ui.KeypadButton_7, 7)
        self.keypadButtons.addButton(self.ui.KeypadButton_8, 8)
        self.keypadButtons.addButton(self.ui.KeypadButton_9, 9)

        self.keyDisplays = QButtonGroup()
        self.keyDisplays.addButton(self.ui.roundDisplay_1, 1)
        self.keyDisplays.addButton(self.ui.roundDisplay_2, 2)
        self.keyDisplays.addButton(self.ui.roundDisplay_3, 3)
        self.keyDisplays.addButton(self.ui.roundDisplay_4, 4)
        self.keyDisplays.addButton(self.ui.roundDisplay_5, 5)
        self.keyDisplays.addButton(self.ui.roundDisplay_6, 6)
        self.keyDisplays.addButton(self.ui.roundDisplay_7, 7)
        self.keyDisplays.addButton(self.ui.roundDisplay_8, 8)
            
        self.displayIndex = 1
        self.password = ""

        for i in range(0, 10):
            self.keypadButtons.button(i).clicked.connect(partial(self.writeNumber, i))

        self.ui.DButtonYes.clicked.connect(lambda : print("playing piano!"))
        self.ui.DButtonNo.clicked.connect(lambda: self.hideDialogueCheck())
        self.nfcReader.nfc_connect.connect(self.checkValidUid)
        

    # Input a password and display it
    def writeNumber(self, num):
        
        self.keyDisplays.button(self.displayIndex).setText(str(num))
        self.password += str(num)
        self.displayIndex += 1
        if self.displayIndex > 8 :
            self.checkValidPass(self.password)
            

    # Check whether the password is valid
    def checkValidPass(self, password):

        (isInDB, data) = self.dbReader.isPassInDatabase(password) # (bool, data)
        
        if isInDB:
            print("valid")
            self.showDialogueCheck(data["name"])
        else:
            print("invalid")
            #self.showErrorAnimation()
        self.clearPassword()
        

    # When NFC signal detected
    @Slot(str)
    def checkValidUid(self, uid):
        
        (isInDB, data) = self.dbReader.isUidInDatabase(uid) # (bool, data)

        if isInDB:
            print("valid")
            self.showDialogueCheck(data["name"])
        else:
            print("invalid")
        self.clearPassword()
    

    def showDialogueCheck(self, name):

        self.ui.DLabelName.setText(name + " 님")
        self.ui.DialogueShadow.show()
        

    def hideDialogueCheck(self):

        self.ui.DialogueShadow.hide()
        print("hide!")
        
        
    def clearPassword(self):
        
        self.password = ""
        self.displayIndex = 1
        for i in range(1, 9):
            self.keyDisplays.button(i).setText("")
        

    def setPage(self):
        
        if not self.nfcReader.isRunning():
            print("thread run")
            self.nfcReader.start()
            

    def clearPage(self):

        if not self.nfcReader.isFinished():
            print("thread quit")
            self.nfcReader.quit()
        self.hideDialogueCheck()
        self.clearPassword()
            

    def __del__(self):

        self.nfcReader.quit()
        self.nfcReader.terminate()
        self.nfcReader.wait()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    login = LogIn()

    login.show()
    sys.exit(app.exec_())
