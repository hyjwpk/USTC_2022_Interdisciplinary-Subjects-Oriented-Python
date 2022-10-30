import sys
from PyQt5.QtWidgets import QApplication, QWidget
import window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = window.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
