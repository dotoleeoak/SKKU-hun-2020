# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PageSignUp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewMebuBar = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewMebuBar.setEnabled(True)
        self.viewMebuBar.setGeometry(QtCore.QRect(0, 0, 800, 60))
        self.viewMebuBar.setAutoFillBackground(False)
        self.viewMebuBar.setStyleSheet("background-color: rgb(241, 145, 39);")
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.viewMebuBar.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.viewMebuBar.setForegroundBrush(brush)
        self.viewMebuBar.setInteractive(True)
        self.viewMebuBar.setSceneRect(QtCore.QRectF(20.0, 20.0, 400.0, 50.0))
        self.viewMebuBar.setObjectName("viewMebuBar")
        self.labelMenuBar = QtWidgets.QLabel(self.centralwidget)
        self.labelMenuBar.setGeometry(QtCore.QRect(280, 0, 240, 70))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.labelMenuBar.setFont(font)
        self.labelMenuBar.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMenuBar.setObjectName("labelMenuBar")
        self.buttonHome = QtWidgets.QPushButton(self.centralwidget)
        self.buttonHome.setGeometry(QtCore.QRect(8, 5, 71, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 145, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.buttonHome.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(20)
        self.buttonHome.setFont(font)
        self.buttonHome.setStyleSheet("background-color: rgb(241, 145, 39);")
        self.buttonHome.setFlat(False)
        self.buttonHome.setObjectName("buttonHome")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(30, 80, 51, 40))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.labelName.setFont(font)
        self.labelName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName("labelName")
        self.labelID = QtWidgets.QLabel(self.centralwidget)
        self.labelID.setGeometry(QtCore.QRect(30, 280, 120, 40))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.labelID.setFont(font)
        self.labelID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelID.setObjectName("labelID")
        self.labelContact = QtWidgets.QLabel(self.centralwidget)
        self.labelContact.setGeometry(QtCore.QRect(30, 180, 101, 40))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(16)
        self.labelContact.setFont(font)
        self.labelContact.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelContact.setObjectName("labelContact")
        self.labelDash1 = QtWidgets.QLabel(self.centralwidget)
        self.labelDash1.setGeometry(QtCore.QRect(115, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(18)
        self.labelDash1.setFont(font)
        self.labelDash1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDash1.setObjectName("labelDash1")
        self.labelDash2 = QtWidgets.QLabel(self.centralwidget)
        self.labelDash2.setGeometry(QtCore.QRect(265, 230, 41, 31))
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(18)
        self.labelDash2.setFont(font)
        self.labelDash2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDash2.setObjectName("labelDash2")
        self.editContact1 = QtWidgets.QLineEdit(self.centralwidget)
        self.editContact1.setGeometry(QtCore.QRect(30, 320, 230, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editContact1.sizePolicy().hasHeightForWidth())
        self.editContact1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(18)
        self.editContact1.setFont(font)
        self.editContact1.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.editContact1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.editContact1.setMaxLength(10)
        self.editContact1.setClearButtonEnabled(True)
        self.editContact1.setObjectName("editContact1")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(30, 390, 320, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet("font: 16pt \"배달의민족 주아\";")
        self.checkBox.setIconSize(QtCore.QSize(40, 40))
        self.checkBox.setShortcut("")
        self.checkBox.setChecked(False)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setAutoExclusive(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.editID = QtWidgets.QLineEdit(self.centralwidget)
        self.editID.setGeometry(QtCore.QRect(30, 220, 85, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editID.sizePolicy().hasHeightForWidth())
        self.editID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(18)
        self.editID.setFont(font)
        self.editID.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.editID.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.editID.setMaxLength(3)
        self.editID.setClearButtonEnabled(True)
        self.editID.setObjectName("editID")
        self.editContact2 = QtWidgets.QLineEdit(self.centralwidget)
        self.editContact2.setGeometry(QtCore.QRect(155, 220, 110, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editContact2.sizePolicy().hasHeightForWidth())
        self.editContact2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(18)
        self.editContact2.setFont(font)
        self.editContact2.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.editContact2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.editContact2.setMaxLength(4)
        self.editContact2.setClearButtonEnabled(True)
        self.editContact2.setObjectName("editContact2")
        self.editContact3 = QtWidgets.QLineEdit(self.centralwidget)
        self.editContact3.setGeometry(QtCore.QRect(305, 220, 110, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editContact3.sizePolicy().hasHeightForWidth())
        self.editContact3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(18)
        self.editContact3.setFont(font)
        self.editContact3.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.editContact3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.editContact3.setMaxLength(4)
        self.editContact3.setClearButtonEnabled(True)
        self.editContact3.setObjectName("editContact3")
        self.editContact1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.editContact1_2.setGeometry(QtCore.QRect(30, 120, 200, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editContact1_2.sizePolicy().hasHeightForWidth())
        self.editContact1_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("배달의민족 주아")
        font.setPointSize(18)
        self.editContact1_2.setFont(font)
        self.editContact1_2.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.editContact1_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.editContact1_2.setMaxLength(20)
        self.editContact1_2.setClearButtonEnabled(True)
        self.editContact1_2.setObjectName("editContact1_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionSignUp = QtWidgets.QAction(MainWindow)
        self.actionSignUp.setObjectName("actionSignUp")
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelMenuBar.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">사용자 등록</span></p></body></html>"))
        self.buttonHome.setText(_translate("MainWindow", "홈"))
        self.labelName.setText(_translate("MainWindow", "이름"))
        self.labelID.setText(_translate("MainWindow", "학번"))
        self.labelContact.setText(_translate("MainWindow", "전화번호"))
        self.labelDash1.setText(_translate("MainWindow", "-"))
        self.labelDash2.setText(_translate("MainWindow", "-"))
        self.checkBox.setText(_translate("MainWindow", " 임시 등록을 하려 합니다."))
        self.menu.setTitle(_translate("MainWindow", "SignUp"))
        self.actionSignUp.setText(_translate("MainWindow", "SignUp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
