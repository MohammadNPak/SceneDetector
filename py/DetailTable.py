import typing
import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt


class MovieDetailModel(QAbstractTableModel):
    def __init__(self):
        super(MovieDetailModel, self).__init__()
        self.scene_data = []

    def set_scene_data(self, scene_data):
        self.scene_data = scene_data

    def add_scene_data(self, scene_data):
        self.layoutAboutToBeChanged.emit()
        self.scene_data.append(scene_data)
        self.layoutChanged.emit()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if len(self.scene_data):
            return len(self.scene_data)
        else:
            return 0

    def columnCount(self, parent: QModelIndex = ...) -> int:
        if len(self.scene_data):
            return len(self.scene_data[0])
        else:
            return 0

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            if len(self.scene_data):
                if index.column() == 1:
                    return self.scene_data[index.row()]
                elif index.column() == 2:
                    float_seconds = float(self.scene_data[index.row()])
                    return datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(float_seconds), "%H:%M:%S:%f")



            else:
                return 0
