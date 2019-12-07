#!/usr/bin/python
# -*- coding: UTF - 8 -*-
import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tkinter import *
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        PyQt5.uic.loadUi('UI.ui', self)
        self.flag = True
        self.pushButton.clicked.connect(self.paintEvent)

    def paintEvent(self, event):
        if self.flag:
            self.flag = False
            self.paint = QPainter()
            self.paint.begin(self)
            self.draw_E(event)
            self.paint.end()

    def draw_E(self, e):
        size = random.randint(50, 350)
        self.paint.setBrush(QColor(random.choice(['yellow'])))
        self.paint.drawEllipse(0, 0, size, size)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())