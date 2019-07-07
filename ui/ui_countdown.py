# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\ui_countdown.ui',
# licensing of '.\ui\ui_countdown.ui' applies.
#
# Created: Sun Jul  7 00:15:18 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_countdownForm(object):
    def setupUi(self, countdownForm):
        countdownForm.setObjectName("countdownForm")
        countdownForm.resize(323, 234)
        countdownForm.setStyleSheet("QWidget#countdownForm{\n"
"    background-color: #2E4057;\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 24pt \"Consolas\";\n"
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
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(countdownForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(countdownForm)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.timeLabel = QtWidgets.QLabel(countdownForm)
        self.timeLabel.setStyleSheet("font: 48pt;")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout.addWidget(self.timeLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(countdownForm)
        QtCore.QMetaObject.connectSlotsByName(countdownForm)

    def retranslateUi(self, countdownForm):
        countdownForm.setWindowTitle(QtWidgets.QApplication.translate("countdownForm", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("countdownForm", "Get Ready", None, -1))
        self.timeLabel.setText(QtWidgets.QApplication.translate("countdownForm", "5", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    countdownForm = QtWidgets.QWidget()
    ui = Ui_countdownForm()
    ui.setupUi(countdownForm)
    countdownForm.show()
    sys.exit(app.exec_())

