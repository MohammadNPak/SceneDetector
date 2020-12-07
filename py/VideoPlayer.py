from PyQt5.QtCore import QUrl, QDir,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QListWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.video_widget = QVideoWidget(parent=self)
        self.media_player = QMediaPlayer(self, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)
        self.setup_ui()
        self.open_file()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "open video file", QDir.homePath())
        if file_name != '':
            media = QMediaContent(QUrl.fromLocalFile(file_name))
            self.media_player.setMedia(media)
            # self.media_player.play()
            print(self.media_player.errorString())

    def setup_ui(self):
        main_layout = QVBoxLayout()
        media_list = QListWidget()
        video_list_layout = QHBoxLayout()
        video_list_layout.addWidget(media_list)
        video_list_layout.addWidget(self.video_widget)
        main_layout.addLayout(video_list_layout)
        # main_layout.addWidget(self.video_widget)
        control_box = QHBoxLayout()
        self.play_button = QPushButton(icon=QIcon('ui\\icon\\play.svg'))
        self.play_button.clicked.connect(lambda: self.media_player.play())


        self.pause_button = QPushButton(icon=QIcon('ui\\icon\\pause.svg'))
        self.pause_button.clicked.connect(lambda: self.media_player.pause())


        self.stop_button = QPushButton(icon=QIcon('ui\\icon\\stop.svg'))
        self.stop_button.clicked.connect(lambda: self.media_player.stop())

        self.forward_button = QPushButton(icon=QIcon('ui\\icon\\next.svg'))
        self.forward_button.clicked.connect(lambda: self.media_player.setPosition(100000))


        self.backward_button = QPushButton(icon=QIcon('ui\\icon\\before.svg'))
        self.ff_button = QPushButton(icon=QIcon('ui\\icon\\fast_forward.svg'))
        self.fb_button = QPushButton(icon=QIcon('ui\\icon\\fast_backward.svg'))
        self.time_slider = QSlider(parent=self, orientation=Qt.Horizontal)
        control_box.addWidget(self.fb_button)
        control_box.addWidget(self.backward_button)
        control_box.addWidget(self.play_button)
        control_box.addWidget(self.pause_button)
        control_box.addWidget(self.stop_button)
        control_box.addWidget(self.forward_button)
        control_box.addWidget(self.ff_button)
        control_box.addWidget(self.time_slider)
        main_layout.addLayout(control_box)

        self.setLayout(main_layout)
