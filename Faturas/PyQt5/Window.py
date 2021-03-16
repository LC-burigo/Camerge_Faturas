import os
import sys
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import QPixmap, QFont
from PIL import Image

connection = sqlite3.connect('camerge.db')
cursor = connection.cursor()
default_img = "../imagens/User_Login"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Faturas")
        self.setGeometry(450, 150, 750, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDeseign()
        self.layouts()

    def mainDeseign(self):
        self.customersList = QListWidget()
        self.btnNew = QPushButton("New")
        self.btnNew.clicked.connect(self.Insert)
        self.btnUpdate = QPushButton("Update")
        self.btnDelete = QPushButton("Delete")

    def layouts(self):
        ########Layouts#########
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        ########Adding child layouts to main layout###########
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 40)
        self.mainLayout.addLayout(self.rightMainLayout, 60)
        #######Adding widgets to layouts###########
        self.rightTopLayout.addWidget(self.customersList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        #######setting main window layout##########
        self.setLayout(self.mainLayout)

    def Insert(self):
        self.insertConsumer = Insert()
        self.close()


class Insert(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adicionar agentes")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        ########widgets for top Layout############
        self.setStyleSheet("background-color:white; font-size:14pt")
        self.title = QLabel("Adicionar agente")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap("../imagens/minha foto.jpg"))

        #######widgets for bottom layout#############
        self.name_lbl = QLabel("Nome: ")
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Nome do agente")

        self.UC_lbl = QLabel("UC: ")
        self.UCEntry = QLineEdit()
        self.UCEntry.setPlaceholderText("UC do agente")

        self.cnpj_lbl = QLabel("CNPJ: ")
        self.cnpjEntry = QLineEdit()
        self.cnpjEntry.setPlaceholderText("CNPJ do agente")

        self.password_lbl = QLabel("Senha: ")
        self.passwordEntry = QLineEdit()
        self.passwordEntry.setPlaceholderText("Senha do agente")

        self.img_lbl = QLabel("Imagem: ")
        self.imgButtom = QPushButton("Browser")
        self.imgButtom.setStyleSheet("background-color:blue;font-size:14p0pt")
        self.imgButtom.clicked.connect(self.uploadImage)

        self.addButtom = QPushButton("Add")
        self.addButtom.setStyleSheet("background-color:blue;font-size:14p0pt")
        self.addButtom.clicked.connect(self.addConsumers)

    def layouts(self):
        #######creating main layouts######
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        #######adding child layouts to main layout#####
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        ######adding widgets to top layouts###########
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(80, 10, 2, 3)

        ######adding widgets to bottom###########
        self.bottomLayout.addRow(self.name_lbl, self.nameEntry)
        self.bottomLayout.addRow(self.UC_lbl, self.UCEntry)
        self.bottomLayout.addRow(self.cnpj_lbl, self.cnpjEntry)
        self.bottomLayout.addRow(self.password_lbl, self.passwordEntry)
        self.bottomLayout.addRow(self.img_lbl, self.imgButtom)
        self.bottomLayout.addRow("", self.addButtom)

        ######seeting main layout for window#######
        self.setLayout(self.mainLayout)

    def addConsumers(self):
        global default_img
        name = self.nameEntry.text()
        UC = self.UCEntry.text()
        cnpj = self.cnpjEntry.text()
        password = self.passwordEntry.text()
        img = default_img

        if name and UC and cnpj and password != "":
            try:
                query = "INSERT INTO customers(agente, unidade consumidora, cnpj, senha, img) VALUES(?, ?, ?, ?, ?, " \
                        "?) "
                cursor.execute(query, (name, UC, cnpj, password, img))
                connection.commit()
                QMessageBox.information(self, "Success", "Person has been added")
            except:
                QMessageBox.information(self, "Warning", "Person has not been added")
        else:
            QMessageBox.information(self, "Warning", "Some field(s) is(are) empty")

    def uploadImage(self):
        global default_img
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')

        if ok:
            default_img = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save("../imagens/{}".format(default_img))


def execution():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    execution()
