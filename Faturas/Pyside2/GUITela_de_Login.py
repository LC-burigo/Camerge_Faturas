from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLabel
from PySide2.QtGui import QFont, QIcon
from Faturas.Pyside2 import controle
import sys


class Window(QWidget):
    global logged, tries
    logged = False
    tries = 0

    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 600)
        self.setWindowTitle("Syscad :: Login")
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: white")
        self.build_form()
        self.image()
        self.login_validation()

    def build_form(self):
        global txt_user, txt_password

        font = QFont("fontes/Signika-Light.ttf")
        font.setPointSize(11)

        txt_user = QLineEdit(self)
        txt_user.setPlaceholderText("Usuário")
        txt_user.setFont(font)
        txt_user.setGeometry(10, 240, 381, 41)

        txt_password = QLineEdit(self)
        txt_password.setPlaceholderText("Senha")
        txt_password.setFont(font)
        txt_password.setGeometry(10, 320, 381, 41)
        txt_password.setEchoMode(QLineEdit.EchoMode.Password)

        login_btn = QPushButton('Logar', self)
        login_btn.setFont(font)
        login_btn.setGeometry(10, 390, 381, 41)
        login_btn.setStyleSheet("background-color: rgb(7, 105, 114)")
        login_btn.clicked.connect(self.login_validation)

    def image(self):
        appIcon = QIcon("../imagens/Logo_Camerge2.png")
        img_login = QIcon("../imagens/User_Login.png")
        img_base = QIcon("../imagens/Logo_Camerge.png")

        pixmap_logo = img_login.pixmap(191, 191)
        pixmap_base = img_base.pixmap(100, 100)

        label_logo = QLabel('Logo', self)
        label_logo.setPixmap(pixmap_logo)
        label_logo.move(100, 10)

        label_base = QLabel('base', self)
        label_base.setPixmap(pixmap_base)
        label_base.setGeometry(150, 500, 411, 161)

        self.setWindowIcon(appIcon)

    def login_validation(self):
        global logged, tries

        user = txt_user.text()
        password = txt_password.text()

        if controle.login(user, password):
            logged = True
            self.close()
            print("login efetuado com sucesso")
        else:
            if tries < 4:
                msg = QMessageBox()
                msg.setText('Login ou senha incorretas')
                msg.exec()
                tries += 1
            if tries == 4:
                sys.exit(0)


def execution():
    global logged

    myApp = QApplication.instance()

    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()
    myApp.exec_()
    return logged

execution()
