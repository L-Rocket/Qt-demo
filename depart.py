# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(295, 433)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 361))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.p1 = QtWidgets.QPushButton(self.groupBox)
        self.p1.setGeometry(QtCore.QRect(30, 120, 41, 41))
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QPushButton(self.groupBox)
        self.p2.setGeometry(QtCore.QRect(70, 120, 41, 41))
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QPushButton(self.groupBox)
        self.p3.setGeometry(QtCore.QRect(110, 120, 41, 41))
        self.p3.setObjectName("p3")
        self.p6 = QtWidgets.QPushButton(self.groupBox)
        self.p6.setGeometry(QtCore.QRect(110, 160, 41, 41))
        self.p6.setObjectName("p6")
        self.p5 = QtWidgets.QPushButton(self.groupBox)
        self.p5.setGeometry(QtCore.QRect(70, 160, 41, 41))
        self.p5.setObjectName("p5")
        self.p4 = QtWidgets.QPushButton(self.groupBox)
        self.p4.setGeometry(QtCore.QRect(30, 160, 41, 41))
        self.p4.setObjectName("p4")
        self.p9 = QtWidgets.QPushButton(self.groupBox)
        self.p9.setGeometry(QtCore.QRect(110, 200, 41, 41))
        self.p9.setObjectName("p9")
        self.p8 = QtWidgets.QPushButton(self.groupBox)
        self.p8.setGeometry(QtCore.QRect(70, 200, 41, 41))
        self.p8.setObjectName("p8")
        self.p7 = QtWidgets.QPushButton(self.groupBox)
        self.p7.setGeometry(QtCore.QRect(30, 200, 41, 41))
        self.p7.setObjectName("p7")
        self.p10 = QtWidgets.QPushButton(self.groupBox)
        self.p10.setGeometry(QtCore.QRect(200, 120, 41, 41))
        self.p10.setObjectName("p10")
        self.p11 = QtWidgets.QPushButton(self.groupBox)
        self.p11.setGeometry(QtCore.QRect(200, 160, 41, 41))
        self.p11.setObjectName("p11")
        self.p12 = QtWidgets.QPushButton(self.groupBox)
        self.p12.setGeometry(QtCore.QRect(200, 200, 41, 41))
        self.p12.setObjectName("p12")
        self.p13 = QtWidgets.QPushButton(self.groupBox)
        self.p13.setGeometry(QtCore.QRect(200, 240, 41, 41))
        self.p13.setObjectName("p13")
        self.p14 = QtWidgets.QPushButton(self.groupBox)
        self.p14.setGeometry(QtCore.QRect(130, 300, 111, 31))
        self.p14.setObjectName("p14")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(20, 30, 211, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(20, 80, 211, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.p0 = QtWidgets.QPushButton(self.groupBox)
        self.p0.setGeometry(QtCore.QRect(30, 240, 41, 41))
        self.p0.setObjectName("p0")
        self.pc = QtWidgets.QPushButton(self.groupBox)
        self.pc.setGeometry(QtCore.QRect(20, 300, 91, 31))
        self.pc.setObjectName("pc")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("mainWindow", "计算器"))
        self.p1.setText(_translate("mainWindow", "1"))
        self.p1.setShortcut(_translate("mainWindow", "1"))
        self.p2.setText(_translate("mainWindow", "2"))
        self.p2.setShortcut(_translate("mainWindow", "2"))
        self.p3.setText(_translate("mainWindow", "3"))
        self.p3.setShortcut(_translate("mainWindow", "3"))
        self.p6.setText(_translate("mainWindow", "6"))
        self.p6.setShortcut(_translate("mainWindow", "6"))
        self.p5.setText(_translate("mainWindow", "5"))
        self.p5.setShortcut(_translate("mainWindow", "5"))
        self.p4.setText(_translate("mainWindow", "4"))
        self.p4.setShortcut(_translate("mainWindow", "4"))
        self.p9.setText(_translate("mainWindow", "9"))
        self.p9.setShortcut(_translate("mainWindow", "9"))
        self.p8.setText(_translate("mainWindow", "8"))
        self.p8.setShortcut(_translate("mainWindow", "8"))
        self.p7.setText(_translate("mainWindow", "7"))
        self.p7.setShortcut(_translate("mainWindow", "7"))
        self.p10.setText(_translate("mainWindow", "+"))
        self.p10.setShortcut(_translate("mainWindow", "+"))
        self.p11.setText(_translate("mainWindow", "-"))
        self.p11.setShortcut(_translate("mainWindow", "-"))
        self.p12.setText(_translate("mainWindow", "×"))
        self.p12.setShortcut(_translate("mainWindow", "*"))
        self.p13.setText(_translate("mainWindow", "÷"))
        self.p13.setShortcut(_translate("mainWindow", "/"))
        self.p14.setText(_translate("mainWindow", "="))
        self.p14.setShortcut(_translate("mainWindow", "Enter"))
        self.p0.setText(_translate("mainWindow", "0"))
        self.p0.setShortcut(_translate("mainWindow", "0"))
        self.pc.setText(_translate("mainWindow", "clean"))
        self.pc.setShortcut(_translate("mainWindow", "Del"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())