from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QLabel, QLineEdit, QTableView, QHeaderView, \
    QMessageBox
from PySide2.QtGui import QFont
import sys
from Faturas.Pyside2.Modelo import CustomTableModel
import mysql.connector


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.frame_register = QFrame(self)
        self.frame_search = QFrame(self)
        self.frame_report = QFrame(self)
        self.frame_edit = QFrame(self)
        self.btn_edit = QPushButton('editar', self)
        self.btn_report = QPushButton('Relatório', self)
        self.btn_search = QPushButton('Pesquisar', self)
        self.btn_register = QPushButton('Cadastrar', self)
        self.font = QFont("fontes/Signika-Light.ttf")
        self.setWindowTitle("Syscad :: Janela Principal")
        self.setGeometry(300, 300, 1000, 700)
        self.setStyleSheet('background-color: rgb(7, 104, 114)')
        self.build_form()

    def build_form(self):
        self.font.setPointSize(10)

        """BUTTONS"""
        self.btn_register.setFont(self.font)
        self.btn_register.setGeometry(0, 0, 170, 50)
        self.btn_register.setStyleSheet('color: rgb(255, 255, 255)')
        self.btn_register.clicked.connect(self.register_frame)

        self.btn_search.setFont(self.font)
        self.btn_search.setGeometry(0, 50, 170, 50)
        self.btn_search.setStyleSheet('color: rgb(255, 255, 255)')
        self.btn_search.clicked.connect(self.search_frame)

        self.btn_report.setFont(self.font)
        self.btn_report.setGeometry(0, 100, 170, 50)
        self.btn_report.setStyleSheet('color: rgb(255, 255, 255)')
        self.btn_report.clicked.connect(self.report_frame)

        self.btn_edit.setFont(self.font)
        self.btn_edit.setGeometry(0, 150, 170, 50)
        self.btn_edit.setStyleSheet('color: rgb(255, 255, 255)')
        self.btn_edit.clicked.connect(self.edit_frame)

        """FRAMES"""
        global frame_register
        self.frame_register.setGeometry(170, 0, 830, 700)
        self.frame_register.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.frame_register.setVisible(False)

        self.lbl_name = QLabel('Nome', self.frame_register)
        self.lbl_name.setGeometry(20, 50, 55, 16)
        self.txt_name = QLineEdit(self.frame_register)
        self.txt_name.setGeometry(80, 50, 721, 22)

        self.lbl_address = QLabel('Endereço', self.frame_register)
        self.lbl_address.setGeometry(20, 90, 55, 16)
        self.txt_address = QLineEdit(self.frame_register)
        self.txt_address.setGeometry(80, 90, 721, 22)

        self.lbl_cpf = QLabel('CPF', self.frame_register)
        self.lbl_cpf.setGeometry(20, 130, 55, 16)
        self.txt_cpf = QLineEdit(self.frame_register)
        self.txt_cpf.setGeometry(80, 130, 721, 22)

        self.btn_clean = QPushButton('Limpar', self.frame_register)
        self.btn_clean.setGeometry(20, 650, 115, 22)

        self.btn_save = QPushButton('salvar', self.frame_register)
        self.btn_save.setGeometry(700, 650, 115, 22)
        self.btn_save.clicked.connect(self.register(self.txt_name.text(), self.txt_address.text(), self.txt_cpf.text()))

        global frame_search
        self.frame_search.setGeometry(170, 0, 830, 700)
        self.frame_search.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.frame_search.setVisible(False)

        self.lbl_name = QLabel('Nome', self.frame_search)
        self.lbl_name.setGeometry(20, 50, 55, 16)
        self.txt_name = QLineEdit(self.frame_search)
        self.txt_name.setGeometry(80, 50, 600, 22)

        self.btn_search = QPushButton('Pesquisar', self.frame_search)
        self.btn_search.setGeometry(700, 50, 80, 22)

        global frame_report
        self.frame_report.setGeometry(170, 0, 830, 700)
        self.frame_report.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.frame_report.setVisible(False)

        data = self.search()
        self.model = CustomTableModel(data)

        self.table = QTableView(self.frame_report)
        self.table.setGeometry(20, 20, 800, 650)
        self.table.setModel(self.model)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 300)

        self.header = self.table.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.Interactive)
        self.header.setStretchLastSection(True)

        global frame_edit
        self.frame_edit.setGeometry(170, 0, 830, 700)
        self.frame_edit.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.frame_edit.setVisible(False)

        self.edition_field = QLineEdit(self.frame_edit)
        self.edition_field.setGeometry(350, 20, 95, 22)
        self.edition_field.setPlaceholderText("000.000.000-00")

        self.lbl_name_edit = QLabel('Nome', self.frame_edit)
        self.lbl_name_edit.setGeometry(20, 50, 55, 16)
        self.txt_name_edit = QLineEdit(self.frame_edit)
        self.txt_name_edit.setGeometry(80, 50, 721, 22)

        self.lbl_address_edit = QLabel('Endereço', self.frame_edit)
        self.lbl_address_edit.setGeometry(20, 90, 55, 16)
        self.txt_address_edit = QLineEdit(self.frame_edit)
        self.txt_address_edit.setGeometry(80, 90, 721, 22)

        self.lbl_cpf_edit = QLabel('CPF', self.frame_edit)
        self.lbl_cpf_edit.setGeometry(20, 130, 55, 16)
        self.txt_cpf_edit = QLineEdit(self.frame_edit)
        self.txt_cpf_edit.setGeometry(80, 130, 721, 22)

        self.btn_save_edit = QPushButton('salvar', self.frame_edit)
        self.btn_save_edit.setGeometry(700, 650, 115, 22)

        global frames
        self.frames = (self.frame_register, self.frame_report, self.frame_search, self.frame_edit)

    def search(self):
        Connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='9479854532441919Lb',
                                             db='camerge')
        cursor = Connection.cursor()
        sql = 'SELECT * FROM customers'
        cursor.execute(sql)
        results = cursor.fetchall()

        len(cursor.description)
        name_col = [i[0] for i in cursor.description]
        return results, name_col

    def register(self, name, address, CPF):
        Connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='9479854532441919Lb',
                                             db='camerge')
        cursor = Connection.cursor()
        try:
            sql = "INSERT INTO customers (Nome, Endereço, CPF) VALUES(?, ?, ?)"
            cursor.execute(sql, (name, address, CPF))
            Connection.commit()
            QMessageBox.information(self, "Success", "Person has been added")
        except:
            QMessageBox.information(self, "Success", "Person has been added")

    def ocult_frames(self):
        global frames
        for f in self.frames:
            if f.isVisible():
                f.setVisible(False)

    def register_frame(self):
        global frame_register
        self.ocult_frames()
        self.frame_register.setVisible(True)

    def search_frame(self):
        global frame_search
        self.ocult_frames()
        self.frame_search.setVisible(True)

    def report_frame(self):
        global frame_report
        self.ocult_frames()
        self.frame_report.setVisible(True)

    def edit_frame(self):
        global frame_edit
        self.ocult_frames()
        self.frame_edit.setVisible(True)


def execution():
    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)

    window = Window()
    window.show()
    myApp.exec_()


# execution()
