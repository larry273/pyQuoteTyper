# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\ui_quotetyper.ui',
# licensing of '.\ui\ui_quotetyper.ui' applies.
#
# Created: Sun Jul  7 00:27:28 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_quoteTyper(object):
    def setupUi(self, quoteTyper):
        quoteTyper.setObjectName("quoteTyper")
        quoteTyper.resize(1172, 483)
        quoteTyper.setStyleSheet("QWidget#quoteTyper{\n"
"    background-color: #2E4057;\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 14pt \"Consolas\";\n"
"    color: white;\n"
"}\n"
"QPushButton {\n"
"    font: 12pt \"Consolas\";\n"
"    color: white;\n"
"    background-color: #5BC0EB;\n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(53, 114, 138);\n"
"}\n"
"\n"
"QTextEdit {\n"
"    font: 12pt \"Consolas\";\n"
"    color: white;\n"
"    background-color: #2E86AB;\n"
"    border-radius: 5;\n"
"    padding: 15;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font: 12pt \"Consolas\";\n"
"    color: white;\n"
"    background-color: #2E86AB;\n"
"    border-radius: 5;\n"
"    padding-left: 15;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    font: 14pt \"Consolas\";\n"
"    color: white;\n"
"    background-color: #2E4057;\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    font: 12pt \"Consolas\";\n"
"    color: white;\n"
"    background-color: #5BC0EB;\n"
"    border-radius: 5;\n"
"    width: 150;\n"
"    height: 40;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(quoteTyper)
        self.gridLayout.setObjectName("gridLayout")
        self.exitButton = QtWidgets.QPushButton(quoteTyper)
        self.exitButton.setMinimumSize(QtCore.QSize(40, 40))
        self.exitButton.setMaximumSize(QtCore.QSize(40, 40))
        self.exitButton.setStyleSheet("width: 40;\n"
"height: 40;")
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 0, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(quoteTyper)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 6)
        self.quoteText = QtWidgets.QTextEdit(quoteTyper)
        self.quoteText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.quoteText.setReadOnly(True)
        self.quoteText.setObjectName("quoteText")
        self.gridLayout.addWidget(self.quoteText, 4, 0, 1, 6)
        self.label_5 = QtWidgets.QLabel(quoteTyper)
        self.label_5.setStyleSheet("font: 24pt;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.quoteLabel = QtWidgets.QLabel(quoteTyper)
        self.quoteLabel.setObjectName("quoteLabel")
        self.horizontalLayout_3.addWidget(self.quoteLabel)
        self.accLabel = QtWidgets.QLabel(quoteTyper)
        self.accLabel.setMaximumSize(QtCore.QSize(235, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.accLabel.setFont(font)
        self.accLabel.setObjectName("accLabel")
        self.horizontalLayout_3.addWidget(self.accLabel)
        self.wpmLabel = QtWidgets.QLabel(quoteTyper)
        self.wpmLabel.setMaximumSize(QtCore.QSize(125, 16777215))
        self.wpmLabel.setObjectName("wpmLabel")
        self.horizontalLayout_3.addWidget(self.wpmLabel)
        self.timeLabel = QtWidgets.QLabel(quoteTyper)
        self.timeLabel.setMaximumSize(QtCore.QSize(160, 16777215))
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout_3.addWidget(self.timeLabel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(quoteTyper)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.newButton = QtWidgets.QPushButton(quoteTyper)
        self.newButton.setMinimumSize(QtCore.QSize(200, 40))
        self.newButton.setMaximumSize(QtCore.QSize(200, 40))
        self.newButton.setObjectName("newButton")
        self.horizontalLayout_4.addWidget(self.newButton)
        self.restartButton = QtWidgets.QPushButton(quoteTyper)
        self.restartButton.setMinimumSize(QtCore.QSize(200, 40))
        self.restartButton.setMaximumSize(QtCore.QSize(200, 40))
        self.restartButton.setObjectName("restartButton")
        self.horizontalLayout_4.addWidget(self.restartButton)
        self.giveupButton = QtWidgets.QPushButton(quoteTyper)
        self.giveupButton.setMinimumSize(QtCore.QSize(200, 40))
        self.giveupButton.setMaximumSize(QtCore.QSize(200, 40))
        self.giveupButton.setObjectName("giveupButton")
        self.horizontalLayout_4.addWidget(self.giveupButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 6)

        self.retranslateUi(quoteTyper)
        QtCore.QMetaObject.connectSlotsByName(quoteTyper)

    def retranslateUi(self, quoteTyper):
        quoteTyper.setWindowTitle(QtWidgets.QApplication.translate("quoteTyper", "Form", None, -1))
        self.exitButton.setText(QtWidgets.QApplication.translate("quoteTyper", "X", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("quoteTyper", "pyQuoteTyper", None, -1))
        self.quoteLabel.setText(QtWidgets.QApplication.translate("quoteTyper", "Quote:", None, -1))
        self.accLabel.setText(QtWidgets.QApplication.translate("quoteTyper", "Accuracy: 100.00%", None, -1))
        self.wpmLabel.setText(QtWidgets.QApplication.translate("quoteTyper", "WPM: 000", None, -1))
        self.timeLabel.setText(QtWidgets.QApplication.translate("quoteTyper", "Time: 00.00", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("quoteTyper", "Source:", None, -1))
        self.newButton.setText(QtWidgets.QApplication.translate("quoteTyper", "New Quote", None, -1))
        self.restartButton.setText(QtWidgets.QApplication.translate("quoteTyper", "Restart", None, -1))
        self.giveupButton.setText(QtWidgets.QApplication.translate("quoteTyper", "Give Up", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quoteTyper = QtWidgets.QWidget()
    ui = Ui_quoteTyper()
    ui.setupUi(quoteTyper)
    quoteTyper.show()
    sys.exit(app.exec_())

