# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:161.127, stop:0 rgba(33, 0, 54, 255), stop:0.258706 rgba(69, 130, 167, 255), stop:0.567164 rgba(126, 226, 244, 255), stop:0.830846 rgba(77, 174, 164, 255), stop:1 rgba(35, 0, 175, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 810, 333, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 810, 333, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 810, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 720, 1000, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 630, 333, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 630, 333, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(660, 630, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 540, 1000, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 450, 1000, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 360, 1001, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Приложение"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить фото"))
        self.pushButton_2.setText(_translate("MainWindow", "Сделать фото"))
        self.pushButton_3.setText(_translate("MainWindow", "Показать фото"))
        self.pushButton_4.setText(_translate("MainWindow", "Показать изображение в оттенках серого"))
        self.pushButton_5.setText(_translate("MainWindow", "Показать красный канал"))
        self.pushButton_6.setText(_translate("MainWindow", "Показать зеленый канал"))
        self.pushButton_7.setText(_translate("MainWindow", "Показать синий канал"))
        self.pushButton_8.setText(_translate("MainWindow", "Нарисовать прямоугольник синим цветом"))
        self.pushButton_9.setText(_translate("MainWindow", "Понизить яркость изображения"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
