import os
import sys
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import QPixmap, QFont
from PIL import Image

connection = sqlite3.connect('camerge.db')
cursor = connection.cursor()
agent_id = None
agent_name = None


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Faturas")
        self.setGeometry(450, 150, 750, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getCustomers()
        self.displayFirstRecord()

    def mainDesign(self):
        self.setStyleSheet("font-size: 14pt; font-family:arial bold;")
        self.customersList = QListWidget()
        self.customersList.itemClicked.connect(self.singleClick)
        self.btnNew = QPushButton("Cadastrar")
        self.btnNew.clicked.connect(self.Insert)
        self.btnUpdate = QPushButton("Atualizar")
        self.btnUpdate.clicked.connect(self.updateCustomer)
        self.btnDelete = QPushButton("Deletar")
        self.btnDelete.clicked.connect(self.delete)

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

    def getCustomers(self):
        query = "SELECT id, agente, cnpj FROM customers"
        customers = cursor.execute(query).fetchall()
        for customer in customers:
            self.customersList.addItem(str(customer[0]) + "-" + customer[1] + "/" + customer[2])

    def displayFirstRecord(self):
        query = "SELECT * FROM customers ORDER BY ROWID ASC LIMIT 1"
        customer = cursor.execute(query).fetchone()
        agent = QLabel(customer[1])
        uc = QLabel(customer[2])
        cnpj = QLabel(customer[3])
        password = QLabel(customer[4])
        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow("Agente: ", agent)
        self.leftLayout.addRow("Unidade C: ", uc)
        self.leftLayout.addRow("CNPJ: ", cnpj)
        self.leftLayout.addRow("Senha: ", password)

    def singleClick(self):
        for i in reversed(range(self.leftLayout.count())):
            widget = self.leftLayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        customer = self.customersList.currentItem().text()
        id = customer.split("-")[0]
        query = "SELECT * FROM customers WHERE id = ?"
        consumer = cursor.execute(query, (id, )).fetchone()
        agent = QLabel(consumer[1])
        uc = QLabel(consumer[2])
        cnpj = QLabel(consumer[3])
        password = QLabel(consumer[4])
        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow("Agente: ", agent)
        self.leftLayout.addRow("Unidade C: ", uc)
        self.leftLayout.addRow("CNPJ: ", cnpj)
        self.leftLayout.addRow("Senha: ", password)

    def delete(self):
        if self.customersList.selectedItems():
            person = self.customersList.currentItem().text()
            id = person.split("-")[0]
            agente = person.split("-")[1]
            mbox = QMessageBox.question(self, "Alerta!!!", "Você realmente quer deletar o agente {}".format(agente), QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM customers WHERE id = ?"
                    cursor.execute(query, (id,))
                    connection.commit()
                    QMessageBox.information(self, "Info", "Agente {} deletado".format(agente))
                    self.close()
                    self.main = Window()
                except:
                    QMessageBox.information(self, "Alerta!!!", "Agente não deletado")
        else:
            QMessageBox.information(self, "Alerta!!!", "Selecione um agente para deletar")

    def updateCustomer(self):
        global agent_id
        global agent_name
        if self.customersList.selectedItems():
            person = self.customersList.currentItem().text()
            agent_id = person.split("-")[0]
            agent_name = person.split("-")[1]
            self.updateWindow = Update()
            self.close()
        else:
            QMessageBox.information(self, "Alerta", "Selecione um agente ser atualizado")


class Update(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atualizar agente")
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.show()

    def UI(self):
        self.getPerson()
        self.mainDesign()
        self.layouts()

    def closeEvent(self, event):
        self.main = Window()

    def mainDesign(self):
        ########widgets for top Layout############
        self.setStyleSheet("background-color:white; font-size:14pt")
        self.title = QLabel("Atualizar agente")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap("../imagens/minha foto.jpg"))

        #######widgets for bottom layout#############
        self.name_lbl = QLabel("Nome: ")
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.agent)

        self.UC_lbl = QLabel("UC: ")
        self.UCEntry = QLineEdit()
        self.UCEntry.setText(self.UC)

        self.cnpj_lbl = QLabel("CNPJ: ")
        self.cnpjEntry = QLineEdit()
        self.cnpjEntry.setText(self.cnpj)

        self.password_lbl = QLabel("Senha: ")
        self.passwordEntry = QLineEdit()
        self.passwordEntry.setText(self.password)

        self.addButtom = QPushButton("Atualizar")
        self.addButtom.setStyleSheet("background-color:blue;font-size:14p0pt")
        self.addButtom.clicked.connect(self.updateConsumers)

    def getPerson(self):
        global agent_id
        query = "SELECT * FROM customers WHERE id = ?"
        customer = cursor.execute(query, (agent_id,)).fetchone()
        self.agent = customer[1]
        self.UC = customer[2]
        self.cnpj = customer[3]
        self.password = customer[4]

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
        self.bottomLayout.addRow("", self.addButtom)

        ######seeting main layout for window#######
        self.setLayout(self.mainLayout)

    def updateConsumers(self):
        global agent_id
        global agent_name
        name = self.nameEntry.text()
        UC = self.UCEntry.text()
        cnpj = self.cnpjEntry.text()
        password = self.passwordEntry.text()
        if name and UC and cnpj and password != "":
            try:
                query = "UPDATE customers set agente = ?, UC = ?, cnpj = ?, senha = ? WHERE id = ?"
                cursor.execute(query, (name, UC, cnpj, password, agent_id))
                connection.commit()
                QMessageBox.information(self, "SUCESSO!!!", "Agente {} atualizado".format(agent_name))
                self.close()
                self.main = Window()
            except:
                QMessageBox.information(self, "ALERTA!!!", "Agente não atualizado")
        else:
            QMessageBox.information(self, "ALERTA!!!", "Todos os campos devem ser preenchidos")


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

    def closeEvent(self, event):
        self.main = Window()

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

        self.addButtom = QPushButton("Adicionar")
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
        self.topLayout.setContentsMargins(40, 20, 2, 3)

        ######adding widgets to bottom###########
        self.bottomLayout.addRow(self.name_lbl, self.nameEntry)
        self.bottomLayout.addRow(self.UC_lbl, self.UCEntry)
        self.bottomLayout.addRow(self.cnpj_lbl, self.cnpjEntry)
        self.bottomLayout.addRow(self.password_lbl, self.passwordEntry)
        self.bottomLayout.addRow("", self.addButtom)

        ######seeting main layout for window#######
        self.setLayout(self.mainLayout)

    def addConsumers(self):
        name = self.nameEntry.text()
        UC = self.UCEntry.text()
        cnpj = self.cnpjEntry.text()
        password = self.passwordEntry.text()
        if name and UC and cnpj and password != "":
            try:
                query = "INSERT INTO customers(agente,UC,cnpj,senha) VALUES(?,?,?,?) "
                cursor.execute(query, (name, UC, cnpj, password))
                connection.commit()
                QMessageBox.information(self, "SUCESSO!!!", "Agente adicionado")
                self.close()
                self.main = Window()
            except:
                QMessageBox.information(self, "ALERTA!!!", "Agente não adicionado")
        else:
            QMessageBox.information(self, "ALERTA!!!", "Todos os campos devem ser preenchidos")


def execution():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    execution()
