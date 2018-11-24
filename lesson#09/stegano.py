# import Important modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from threading import Thread
import time

from os import path
import sys

LIMIT_TIME = 100

# import UI file
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'welcomeWindow.ui'))


class Ex(QThread):
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < LIMIT_TIME :
            count += 1
            time.sleep(0.04)
            self.countChanged.emit(count)


class mainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.onStart()

    def onStart(self):
        self.calc = Ex()
        self.calc.countChanged.connect(self.countChangedProcess)
        self.calc.start()

    def countChangedProcess(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            time.sleep(1)
        


def main():
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()