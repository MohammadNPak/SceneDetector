from PyQt5.QtCore import QProcess, pyqtSignal, QObject

import re
import datetime


class SceneExtractor(QObject):
    progress_percent_changed = pyqtSignal(float)

    def __init__(self):
        super(SceneExtractor, self).__init__()
        self.sub_process = QProcess()
        self.readed_err = 0
        self.readed_out = 0
        self.duration = None
        self.duration_second = None
        self.pts = []
        self.pts_second = []
        self.progress_percent = 0
        self.ffmpeg_path = "ffmpeg.exe"
        self.video_file_path = '"F:\\code\\python\\SceneDetector\\test.mkv"'
        self.sub_process.readyReadStandardError.connect(self.read_std_error)
        self.sub_process.readyReadStandardOutput.connect(self.read_std_out)
        self.sub_process.finished.connect(self.reading_finished)

    def start_process(self):
        scene_sensitivity = 0.003
        self.sub_process.start(
            self.ffmpeg_path,
            ['-i',
             r'F:\code\python\SceneDetector\test.mkv',
             '-filter_complex',
             f'select=\'gt(scene,{scene_sensitivity})\' ,showinfo',
             '-f',
             'null',
             '-'
             ]
        )

    def read_std_error(self):
        self.readed_err += 1
        data = self.sub_process.readAllStandardError()
        std_error = bytes(data).decode("utf8")
        if self.duration_second:
            self.find_pts(std_error)
            if self.pts_second:
                self.progress_percent = self.pts_second[-1] / self.duration_second
                self.progress_percent_changed.emit(self.progress_percent)
        else:
            self.find_duration(std_error)

    def find_duration(self, std_error):
        duration_re = re.search(r"Duration: \d*:\d*:\d*.\d*", std_error)
        if duration_re:
            self.duration = duration_re.group()[10:]
            self.duration_second = self.pts_to_second(self.duration)

    def pts_to_second(self, pts_time):
        x = pts_time.split(":")
        if len(x) == 3:
            hour = int(x[0])
            minute = int(x[1])
            second = float(x[2])
            return ((hour * 60) + minute) * 60 + second
        elif len(x) == 2:
            minute = int(x[0])
            second = float(x[1])
            return minute * 60 + second
        else:
            second = float(x[0])
            return second

    def read_std_out(self):
        self.readed_out += 1
        data = self.sub_process.readAllStandardOutput()
        std_output = bytes(data).decode("utf8")

    def reading_finished(self):
        pass

    def find_pts(self, std_error):
        result = re.search(r"pts_time:\d*:*\d*:*\d*.\d*", std_error)
        if result:
            self.pts.append(result.group()[10:])
            self.pts_second.append(self.pts_to_second(self.pts[-1]))
