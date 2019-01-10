# import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType('input_output_gui.ui')

class IO_Dialogue(QMainWindow):
    def __init__(self):
        super(IO_Dialogue, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.statusbar.setObjectName('statusbar')
        # window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        # self.retranslateUi(self)

        self.pushButton.clicked.connect(self.browseSlot)
        self.lineEdit.returnPressed.connect(self.returnPressedSlot)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File Name"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))

    @pyqtSlot()
    def returnPressedSlot(self):
        pass

    @pyqtSlot()
    def browseSlot(self):
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = IO_Dialogue()
    # window = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    window.show()
    sys.exit(app.exec_())



class Ui_MainWindow(QObject):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
# class Ui_MainWindow(QMainWindow):
    # self.statusbar.setObjectName('statusbar')
    # MainWindow.setStatusBar(self.statusbar)

    self.retranslateUi(MainWindow)

    self.pushButton.clicked.connect(self.browseSlot)
    self.lineEdit.returnPressed.connect(self.returnPressedSlot)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File Name"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))

    @pyqtSlot()
    def returnPressedSlot(self):
        pass

    @pyqtSlot()
    def browseSlot(self):
        pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(ap.exec_())
    # ui.setupUi(Ui_MainWindow)


# class MyApp(QMainWindow):
#     def __init__(self):
#         super(MyApp, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.input_file_browse_button.clicked.connect(self.BrowseInputFile)
#         self.ui.ok_cancel_buttons.clicked.connect(self.RunScript)
#
#     def BrowseInputFile(self):
#         price = float(self.ui.price_box.toPlainText())
#         tax = (self.ui.tax_rate.value())
#         tax_paid = (tax / 100) * price
#         total_price = price + tax_paid
#         # print (total_price)
#         tax_paid_string = 'The tax paid is: ' + str(tax_paid)
#         total_price_string = 'The total price with tax is: ' + str(total_price)
#         self.ui.results_window_tax.setText(tax_paid_string)
#         self.ui.results_window_total.setText(total_price_string)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyApp()
#     window.show()
#     sys.exit(app.exec_())

