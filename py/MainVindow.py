from PyQt5.QtWidgets import QMainWindow
from ui.UI_MainWindow import Ui_MainWindow
from py.VideoPlayer import VideoPlayer
from py.SceneExtraxtor import SceneExtractor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.video_widget = VideoPlayer()
        self.video_widget.setParent(self)
        self.video_widget.setGeometry(100, 100, 800, 600)

###################################################################3
        self.scene_ex = SceneExtractor()
        self.scene_ex.start_process()
        self.scene_ex.progress_percent_changed.connect(self.update_)

    def update_(self,value):
        print("value",value)
        print('pts second', self.scene_ex.pts_second)
        print('duration', self.scene_ex.duration_second)