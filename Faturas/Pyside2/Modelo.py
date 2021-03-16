from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide2.QtGui import QColor


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)

        self.dates = data[0]
        self.titles = data[1]

        self.load_data(self.dates)

    def load_data(self, dados):
        self.num_lines = len(dados)
        self.num_col = len(dados[0])

    def rowCount(self, parent=QModelIndex()):
        return self.num_lines

    def columnCount(self, parent=QModelIndex()):
        return self.num_col

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.titles[section].upper()
        else:
            return section

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            return self.dates[row][column]
        elif role == Qt.TextAlignmentRole:
            if column == 0:
                return Qt.AlignCenter
            if column == 3:
                return Qt.AlignCenter
            return Qt.AlignLeft
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)

        return None



