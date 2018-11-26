#!usr/bin/python3

# import Important modules
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from stegano import lsb
from AES_FILE import PrpCrypt

from os import path
import sys , time , os

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
        self.pushButton.clicked.connect(self.select_operation_hide)
        self.pushButton_2.clicked.connect(self.select_operation_show)
        self.pushButton_5.clicked.connect(self.setOutput)
        self.pushButton_4.clicked.connect(self.process)

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
    
    def select_operation_show(self):
        self.label_17.setText('SHOW')

    def select_operation_hide(self):
        self.label_17.setText('HIDE')

    def setOutput(self):
        url_output = QFileDialog.getSaveFileName(self, 'Save As', '', 'Image Files (*.png);; Text Files (*.txt)')
        Directory_output = url_output[0]
        self.lineEdit_4.setText(Directory_output)

    def process(self):
        key_key = self.plainTextEdit.toPlainText()
        message = self.plainTextEdit_2.toPlainText()
        image = self.lineEdit.text()
        pathSave = self.lineEdit_4.text()
        choice = self.label_17.text()

        if choice == 'HIDE':
            if (key_key != '') and (message != '') and (image != '') and (pathSave != ''):
                try:
                    QMessageBox.about(self,' wait', 'waiting ...!')
                    encrypted_message = PrpCrypt(key_key).encrypt(message)
                    encrypted_message_str = encrypted_message.decode() # convert byte to str
                    secret = lsb.hide(image, encrypted_message_str, auto_convert_rgb=True)
                    secret.save(pathSave)
                    time.sleep(1)
                    QMessageBox.about(self, 'terminat', 'DONE!')
                    self.plainTextEdit.setPlainText('')
                    self.plainTextEdit_2.setPlainText('')
                    self.lineEdit_2.setText('')
                    self.lineEdit.setText('')
                    self.lineEdit_3.setText('')
                    self.lineEdit_5.setText('')
                    self.lineEdit_4.setText('')
                except:
                    QMessageBox.about(self, 'Error', 'Fialed operation, Try again !')
            else:
                QMessageBox.about(self, 'Error', 'Please Enter all fields to continu ..')
        elif choice == 'SHOW':
            if (key_key != '') and (image != ''):
                try:
                    QMessageBox.about(self,' wait', 'waiting ...!')
                    clear_message = lsb.reveal(image)
                    clear_message_bytes = str.encode(clear_message) # convert str to bytes
                    decrypted_text = PrpCrypt(key_key).decrypt(clear_message_bytes)
                    op = True
                    if op == True:
                        file_secure_output = self.lineEdit_4.text()
                        open_open = open(file_secure_output, "w")
                        open_open.writelines(decrypted_text)
                        open_open.close()
                        time.sleep(1)
                        QMessageBox.about(self, 'Success', 'Done ^_^ Your message was stored in:\n{}'.format(file_secure_output))
                        self.plainTextEdit.setPlainText('')
                        self.plainTextEdit_2.setPlainText('')
                        self.lineEdit_2.setText('')
                        self.lineEdit.setText('')
                        self.lineEdit_3.setText('')
                        self.lineEdit_5.setText('')
                        self.lineEdit_4.setText('')
                except:
                    QMessageBox.about(self, 'Error', 'Wrong key !')
            else:
                QMessageBox.about(self, 'Error', 'Wrong key or your image not found !')
        else:
            QMessageBox.about(self, 'Error', 'Please select an operation (hide or show) to continue ...')

def main():
    app = QApplication(sys.argv)
    window = mainApp1()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()