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
        self.handle_ui()
        self.handle_button()

    def handle_ui(self):
        self.setFixedSize(800,630)
        self.setWindowIcon(QIcon('photos/lock.png'))

    def handle_button(self):
        self.pushButton_3.clicked.connect(self.select_image)

    # Get image Information
    def select_image(self):
        try:
            url_dir = QFileDialog.getOpenFileName(self, 'Select image', '', 'Image Files (*.png)')
            Directory = url_dir[0]
            base = path.basename(Directory)
            name = path.splitext(base)[0]
            extension = path.splitext(base)[1]
            size = path.getsize(Directory)
            self.lineEdit.setText(Directory)
            self.lineEdit_2.setText(name)
            self.lineEdit_5.setText(extension[1:])
            if size < 1000:
                self.lineEdit_3.setText(str(size) + ' Bytes')
            else:
                size /= 1000
                self.lineEdit_3.setText(str(size) + ' KB')
        except:
            pass



def main():
    app = QApplication(sys.argv)
    window = mainApp1()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()