from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
import sys
import random


class Ui_yellow_rounds(object):
    def setupUi(self, yellow_rounds):
        yellow_rounds.setObjectName("yellow_rounds")
        yellow_rounds.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=yellow_rounds)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 280, 121, 61))
        self.pushButton.setObjectName("pushButton")
        yellow_rounds.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=yellow_rounds)
        self.statusbar.setObjectName("statusbar")
        yellow_rounds.setStatusBar(self.statusbar)

        self.retranslateUi(yellow_rounds)
        QtCore.QMetaObject.connectSlotsByName(yellow_rounds)

    def retranslateUi(self, yellow_rounds):
        _translate = QtCore.QCoreApplication.translate
        yellow_rounds.setWindowTitle(_translate("yellow_rounds", "Yellow rounds"))
        self.pushButton.setText(_translate("yellow_rounds", "PushButton"))


class YellowRounds(QMainWindow, Ui_yellow_rounds):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.size = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            x, y = random.randint(100, 800 - 100), random.randint(100, 600 - 100)
            qp.drawEllipse(x, y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowRounds()
    ex.show()
    sys.exit(app.exec())
