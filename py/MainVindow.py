from PyQt5.QtWidgets import QMainWindow
from ui.UI_MainWindow import Ui_MainWindow
from py.VideoPlayer import VideoPlayer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.video_widget = VideoPlayer()
        self.video_widget.setParent(self)
        self.video_widget.setGeometry(100, 100, 800, 600)
