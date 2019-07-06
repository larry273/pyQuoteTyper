from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
from PySide2 import QtCore, QtGui
from ui.ui_pyTyper import Ui_quoteTyper
import sys

class typeWindow(QWidget):
    acc_signal = QtCore.Signal(int)

    def __init__(self):
        super(typeWindow, self).__init__()
        self.ui = Ui_quoteTyper()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    
        radius = 10.0
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

        self.ui.lineEdit.textChanged.connect(self.check_input)
        self.ui.newButton.clicked.connect(self.populate_quote)
        self.ui.exitButton.clicked.connect(self.exit)
        self.acc_signal.connect(self.calc_accuracy)
        self.ui.giveupButton.clicked.connect(self.update_letter)

        self.oldPos = self.pos()

        #text input
        self.currentLetter = None
        self.currentIndex = None
        self.typedLetter = None

    def update_letter(self, index):
        i = index
        colored = self.quote[:i]
        uncolored = self.quote[i:]

        new_text = f"<span style='color:#00453C;font-weight:bold'>{colored}</span>{uncolored}"
        self.ui.quoteText.setText(new_text)
    
    #check the user input matches the current typed section
    def check_input(self):
        typed = self.ui.lineEdit.text()[-1]
        print(typed)

        current = self.quote[self.currentIndex]
        print(current)

        if typed == current:
            print('good')
            self.acc_signal.emit(1)
            self.currentIndex += 1
            self.ui.lineEdit.setStyleSheet('background-color: #2E86AB')
            self.update_letter(self.currentIndex)
            if typed == ' ':
                self.ui.lineEdit.clear()
        else:
            print('bad')
            self.ui.lineEdit.setStyleSheet('background-color: #931621')
            self.acc_signal.emit(0)
        

    def calc_wpm(self):
        pass

    def calc_accuracy(self, result):
        print(result)
    
    def calc_time(self):
        pass

    def fetch_quote(self):
        pass
        
    def exit(self):
        sys.exit()

    def populate_quote(self):
        self.quote = ('This is a sample quote. This could be typed')
        self.ui.quoteText.setHtml(self.quote)
        self.currentIndex = 0
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = typeWindow()
    window.show()
    sys.exit(app.exec_())


