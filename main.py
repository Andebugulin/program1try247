from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.move(650, 300)
        self.pushButton.setFixedSize(100, 100)
        self.pushButton.clicked.connect(self.circle)
        self.label = QLabel()
        canv = QPixmap(600, 600)
        self.label.setPixmap(canv)
        lay = QGridLayout(self.centralwidget)
        lay.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        lay.addWidget(self.label, 1, 0)

    def circle(self):
        x, y = [randint(10, 500) for i in range(2)]
        w = randint(10, 100)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(QColor(255, 255, 0))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, w)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())

