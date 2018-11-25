# import Important modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from os import path
import sys

# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'mainProgram.ui'))

class mainApp1(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp1,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = mainApp1()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()