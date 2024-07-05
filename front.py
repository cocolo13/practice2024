"""Файл, описывающий графический интерфейс приложения, а также
 его логику"""
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QFileDialog, QMessageBox, QInputDialog,
                             QMainWindow)

"""Основной класс программы"""


class Ui_MainWindow(QMainWindow):
    """Конструктор класса"""

    def __init__(self):
        super().__init__()
        self.image = None
        self.setupUi()

    """Функция создания графического интерфейса(кнопки надписи и т.д)"""

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1000, 900)
        self.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:161.127,"
            " stop:0 rgba(33, 0, 54, 255),stop:0.258706 rgba(69, 130, 167,"
            " 255), stop:0.567164 rgba(126, 226, 244, 255), stop:0.830846"
            " rgba(77, 174, 164, 255), stop:1 rgba(35, 0, 175, 255));")
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.label_pictures = QtWidgets.QLabel(self.centralwidget)
        self.label_pictures.setGeometry(QtCore.QRect(0, 0, 1001, 359))
        self.label_pictures.setFont(font)
        self.label_pictures.setText("")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.load_pictures)
        self.pushButton_2.clicked.connect(self.open_camera)
        self.pushButton_3.clicked.connect(self.view_pictures)
        self.pushButton_4.clicked.connect(self.view_gray)
        self.pushButton_5.clicked.connect(lambda: self.show_channel(2))
        self.pushButton_6.clicked.connect(lambda: self.show_channel(1))
        self.pushButton_7.clicked.connect(lambda: self.show_channel(0))
        self.pushButton_8.clicked.connect(self.draw_rectangle)
        self.pushButton_9.clicked.connect(self.lower_brightness)

    """Функция, предназначения для понижения яркости изображения"""

    def lower_brightness(self):
        if self.image is None:
            QMessageBox.critical(self, "Ошибка", "Изображение "
                                                 "еще не загружено.")
            return
        value, flag = QInputDialog.getInt(self, "Уменьшить яркость"
                                                " изображения Введите"
                                                " значение на которое "
                                                "следует понизить яркость:"
                                                "", 10, 0, 255)
        if flag:
            self.image = (np.clip(self.image - value, 0, 255).
                          astype(np.uint8))
            self.display_image(self.image)

    """Функция, предназначенная для рисования прямоугольник синего цвета с
     заданными координатами"""

    def draw_rectangle(self):
        if self.image is None:
            QMessageBox.critical(self, "Ошибка", "Изображение еще"
                                                 " не загружено.")
        x, flag1 = QInputDialog.getInt(self, "Рисуем прямоугольник",
                                       "Введите координату по x:", 0, 0,
                                       self.image.shape[1])
        y, flag2 = QInputDialog.getInt(self, "Рисуем прямоугольник",
                                       "Введите координату по y:", 0, 0,
                                       self.image.shape[0])
        w, flag3 = QInputDialog.getInt(self, "Рисуем прямоугольник",
                                       "Введите ширину прямоугольника:",
                                       50, 0,
                                       self.image.shape[1] - x)
        h, flag4 = QInputDialog.getInt(self, "Рисуем прямоугольник",
                                       "Введите высоту прямоугольника:",
                                       50, 0,
                                       self.image.shape[0] - y)
        if flag1 and flag2 and flag3 and flag4:
            image_with_rectangle = self.image.copy()
            cv.rectangle(image_with_rectangle, (x, y), (x + w, y + h),
                         (255, 0, 0), 2)
            self.display_image(image_with_rectangle)

    """Функция, предназначенная для вывода различных цветовых
     каналов изображения"""

    def show_channel(self, channel):
        if self.image is None:
            QMessageBox.critical(self, "Ошибка",
                                 "Изображение еще не загружено.")
            return
        channel_image = np.zeros_like(self.image)
        channel_image[:, :, channel] = self.image[:, :, channel]
        self.display_image(channel_image)

    def display_image(self, image):  # for view gray
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height,
                         bytes_per_line, QImage.Format_BGR888)
        self.label_pictures.setPixmap(QPixmap.fromImage(q_image).scaled(
            self.label_pictures.width(), self.label_pictures.height(),
            Qt.KeepAspectRatio))

    """Функция для вывода изображения в оттенках серого"""

    def view_gray(self):
        if self.image is None:
            QMessageBox.critical(self, "Ошибка",
                                 "Изображение еще не загружено.")
            return
        gray_image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        self.display_image(cv.cvtColor(gray_image, cv.COLOR_GRAY2BGR))

    """Функция для вывода изображения на экран"""

    def view_pictures(self):
        if self.image is None:
            QMessageBox.critical(self, "Ошибка",
                                 "Изображение еще не загружено.")
        else:
            height, width, channel = self.image.shape
            bytes_per_line = 3 * width
            q_image = QImage(self.image.data, width, height,
                             bytes_per_line, QImage.Format_BGR888)
            self.label_pictures.setPixmap(QPixmap.fromImage(q_image).
                                          scaled(self.label_pictures.width(), self.
                                                 label_pictures.height(), Qt.KeepAspectRatio))

    """Функция для открытия вебкамеры и снятия фотографии"""

    def open_camera(self):
        self.label.setText("Нажмите клавишу 'q', чтобы сделать фото"
                           "(Расскладка должна быть англ!)")
        camera = cv.VideoCapture(0)
        while True:
            flag, img = camera.read()
            cv.imshow("Camera", img)
            if flag:
                self.image = img
                self.label.setText("Фото успешно сохранено")
            if cv.waitKey(1) & 0xFF == ord("q"):
                break

    """Функция для загрузки фотографии с компьютера"""

    def load_pictures(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self,
                                                   "Выберите изображение",
                                                   "", "Image Files"
                                                       " (*.png *.jpg *.jpeg)")
        if file_path:
            self.image = cv.imread(file_path)
            if self.image is None:
                QMessageBox.critical(self, "Ошибка",
                                     "Не удалось загрузить изображение.")
            else:
                self.label.setText("Изображение успешно загружено")

    """Функция, предназначенная для изменения текста
     на кнопках в приложении"""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Приложение"))
        self.pushButton.setText(_translate("MainWindow",
                                           "Загрузить фото"))
        self.pushButton_2.setText(_translate("MainWindow",
                                             "Сделать фото"))
        self.pushButton_3.setText(_translate("MainWindow",
                                             "Показать фото"))
        self.pushButton_4.setText(_translate("MainWindow",
                                             "Показать изображение"
                                             " в оттенках серого"))
        self.pushButton_5.setText(_translate("MainWindow", "Показать"
                                                           " красный канал"))
        self.pushButton_6.setText(_translate("MainWindow", "Показать"
                                                           " зеленый канал"))
        self.pushButton_7.setText(_translate("MainWindow",
                                             "Показать синий канал"))
        self.pushButton_8.setText(_translate("MainWindow",
                                             "Нарисовать прямоугольник"
                                             " синим цветом"))
        self.pushButton_9.setText(_translate("MainWindow",
                                             "Понизить яркость изображения"))
