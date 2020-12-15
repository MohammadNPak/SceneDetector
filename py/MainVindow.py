from PyQt5.QtWidgets import QMainWindow, QTableView, QApplication, QFileDialog
from ui.UI_MainWindow import Ui_MainWindow
from py.VideoPlayer import VideoPlayer
from py.SceneExtraxtor import SceneExtractor

from py.DetailTable import MovieDetailModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.video_widget = VideoPlayer()
        # self.video_widget.setParent(self)

        self.ui.ffmpegAddressBtn.clicked.connect(self.ffmpeg_address_btn)
        self.ui.videoAddressBtn.clicked.connect(self.video_address_btn)
        ####################################################################
        self.movie_detail_model = MovieDetailModel()
        self.table = QTableView()
        self.ui.movieDetailTableView.setModel(self.movie_detail_model)

        ###################################################################3
        self.scene_ex = SceneExtractor()
        self.scene_ex.scene_chande_found.connect(self.movie_detail_model.add_scene_data)
        self.scene_ex.progress_percent_changed.connect(self.update_progressbar)
        self.ui.startProcessBtn.clicked.connect(self.scene_ex.start_process)

        ###################################################################

        ###################################################################
    def update_progressbar(self, value):
        self.ui.mainProgressBar.setValue(value * 100)

    def update_(self, value):
        print("value", value)
        print('pts second', self.scene_ex.pts_second)
        print('duration', self.scene_ex.duration_second)

    def ffmpeg_address_btn(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        if file_dialog.exec_():
            file_address = file_dialog.selectedFiles()[0]
            self.scene_ex.set_ffmpeg_url(file_address)
            self.ui.lineEdit.setText(str(self.scene_ex.ffmpeg_url))

    def video_address_btn(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        if file_dialog.exec_():
            file_address = file_dialog.selectedFiles()[0]
            self.scene_ex.set_video_url(file_address)
            self.ui.lineEdit_2.setText(str(self.scene_ex.video_url))
            self.ui.videoPlayer.open_file(file_address)
