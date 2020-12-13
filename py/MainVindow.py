from PyQt5.QtWidgets import QMainWindow, QTableView
from ui.UI_MainWindow import Ui_MainWindow
from py.VideoPlayer import VideoPlayer
from py.SceneExtraxtor import SceneExtractor

from py.DetailTable import MovieDetailModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.video_widget = VideoPlayer()
        self.video_widget.setParent(self)
        self.video_widget.setGeometry(10, 10, 400, 300)
####################################################################
        self.movie_detail_model = MovieDetailModel()
        self.table = QTableView()
        self.table.setModel(self.movie_detail_model)
        self.table.show()
        # self.ui.formLayoutWidget.layout().addWidget(self.movie_detail)


###################################################################3
        self.scene_ex = SceneExtractor()
        self.scene_ex.start_process()
        self.scene_ex.progress_percent_changed.connect(self.update_)
###################################################################



    def update_(self,value):
        print("value",value)
        print('pts second', self.scene_ex.pts_second)
        print('duration', self.scene_ex.duration_second)