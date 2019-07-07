from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
from PySide2 import QtCore, QtGui
from ui.ui_pyTyper import Ui_quoteTyper
from countdownWindow import countdownWindow
import sys
import time

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
        #self.ui.giveupButton.clicked.connect(self.update_letter)

        self.oldPos = self.pos()

        self.countdown = countdownWindow()
        self.countdown.end_signal.connect(self.start_type)
        #text input
        self.current_index = None
        self.typedLetter = None
        self.accuracy = None
        self.total = None
        self.time_elapsed = 0


    def update_letter(self, index):
        i = index
        colored = self.quote[:i]
        uncolored = self.quote[i:]

        new_text = f"<span style='color:#00453C;font-weight:bold'>{colored}</span>{uncolored}"
        self.ui.quoteText.setText(new_text)
    
    #check the user input matches the current typed section
    def check_input(self):
        try:
            typed = self.ui.lineEdit.text()[-1]
        except IndexError:
            return
        current = self.quote[self.current_index]

        if typed == current:
            self.acc_signal.emit(1)
            self.current_index += 1
            self.ui.lineEdit.setStyleSheet('background-color: #2E86AB')
            self.update_letter(self.current_index)
            if self.current_index == self.quote_len:
                print('Done Typing')
                #end_time = time.time()

                self.ui.lineEdit.clear()
                self.timer.stop()
                self.timer_wpm.stop()

                total = self.ui.timeLabel.text().split()[1]
                wpm, n_wpm = self.calc_wpm(final=True)
                acc = self.ui.accLabel.text().split()[1]

                msg = (
                    f'Total Time: {total} seconds\n'
                    f'Gross WPM: {wpm}\n'
                    f'Net WPM: {n_wpm}\n'
                    f'Accuracy: {acc}\n'
                )
                self.message_indicate(msg)
            
            if typed == ' ':
                self.ui.lineEdit.clear()
        else:
            #print('bad')
            self.ui.lineEdit.setStyleSheet('background-color: #931621')
            self.acc_signal.emit(0)
        
    def calc_wpm(self, final=False):
        #net wpm = (All/5 - E)/t
        #gross wpm = (All/5)/t
        time = self.time_elapsed
        wpm = (self.accuracy/ 5)/(time/60)
        wpm = int(round(wpm))
        self.ui.wpmLabel.setText(f'WPM: {wpm}')

        if final:
            n_wpm = wpm - ((self.total - self.accuracy)/5/(time/60))
            n_wpm = int(round(n_wpm))
            return (wpm, n_wpm)


    def message_indicate(self, msg):
        choice = QMessageBox(self)
        choice.setIcon(QMessageBox.Information)
        choice.setWindowTitle("Quote Completed")
        choice.setText(msg)
        r = choice.exec_()

    def calc_accuracy(self, result):
        if result == 1:
            self.total += 1
            self.accuracy += 1
        else:
            self.total += 1
        acc = self.accuracy / self.total * 100
        acc = "{0:.2f}".format(acc)
        self.ui.accLabel.setText(f'Accuracy: {acc}%')

    def reset(self):
        self.current_index = 0
        self.total = 0
        self.accuracy = 0
        self.time_elapsed = 0

        self.ui.lineEdit.clear()
        self.ui.accLabel.setText('Accuracy: 100.00%')

    def fetch_quote(self):
        pass
        
    def exit(self):
        sys.exit()

    def time_update(self):
        end = time.time()
        total = end - self.start_time 
        self.time_elapsed = round(total, 2)

        self.ui.timeLabel.setText('Time: {0:.2f}'.format(self.time_elapsed))

    def populate_quote(self):
        self.quote = ('This is a sample quote. This could be typed')
        #self.quote = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        self.ui.quoteText.setHtml(self.quote)
        self.quote_len = len(self.quote)

        self.countdown.start_countdown()


    def start_type(self):
        self.reset()
        self.start_time = time.time()
        print(self.start_time)

        self.ui.lineEdit.setFocus()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.time_update)
        self.timer.start(50)

        self.timer_wpm = QtCore.QTimer()
        self.timer_wpm.timeout.connect(self.calc_wpm)
        self.timer_wpm.start(250)


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


