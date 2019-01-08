import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType('tax_calculator.ui')

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calc_tax_button.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = float(self.ui.price_box.toPlainText())
        tax = (self.ui.tax_rate.value())
        tax_paid = (tax / 100) * price
        total_price = price + tax_paid
        # print (total_price)
        tax_paid_string = 'The tax paid is: ' + str(tax_paid)
        total_price_string = 'The total price with tax is: ' + str(total_price)
        self.ui.results_window_tax.setText(tax_paid_string)
        self.ui.results_window_total.setText(total_price_string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

