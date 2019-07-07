from PySide2.QtWidgets import QWidget
from PySide2 import QtCore, QtGui
from ui.ui_countdown import Ui_countdownForm
import sys

class countdownWindow(QWidget):
    end_signal = QtCore.Signal()

    def __init__(self):
        super(countdownWindow, self).__init__()
        self.ui = Ui_countdownForm()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    
        radius = 10.0
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

        self.oldPos = self.pos()
        self.countdown = 3

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def start_countdown(self):
        self.show()
        self.countdown = 3
        self.ui.timeLabel.setText(str(self.countdown))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        self.countdown -= 1
        self.ui.timeLabel.setText(str(self.countdown))

        if self.countdown == 0:
            self.end_signal.emit()
            self.hide()
            self.timer.stop()


    

 