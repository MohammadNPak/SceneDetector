import typing

from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt


class MovieDetailModel(QAbstractTableModel):
    def __init__(self):
        super(MovieDetailModel, self).__init__()
        self.scene_data = [1,2,3,4,5,6,7,8]

    def set_scene_data(self, scene_data):
        self.scene_data = scene_data

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return 3

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 5

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            if index.column() == 1:
                return index.row()
            elif index.column() == 2:
                return self.scene_data[index.row()]
