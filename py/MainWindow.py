from PyQt5.QtWidgets import QMainWindow

from UI.UI_MainWindow import Ui_MainWindow
from py.SceneExtraxtor import SceneExtractor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene_ex = SceneExtractor()
        self.scene_ex.start_process()
        self.scene_ex.progress_percent_changed.connect(self.update_)
        print("dd")

    def update_(self,value):
        print("value",value)
        print('pts second', self.scene_ex.pts_second)
        print('duration', self.scene_ex.duration_second)
        self.ui.horizontalSlider.setValue(int(value*self.ui.horizontalSlider.maximum()))
        self.show()