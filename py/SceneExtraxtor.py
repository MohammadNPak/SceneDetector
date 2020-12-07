from PyQt5.QtCore import QProcess, pyqtSignal, QObject, QDir, QUrl
import re
import logging
import os
import time

logging.getLogger().setLevel(logging.DEBUG)


class SceneExtractor(QObject):
    progress_percent_changed = pyqtSignal(float)

    def __init__(self):
        super(SceneExtractor, self).__init__()
        self.sub_process = QProcess()
        self.ffmpeg_url = QUrl('ffmpeg.exe')
        self.video_url = QUrl('E:\movie\harryPotter\Harry PotterandtheDeathlyHallowsPart2_2011.mkv')

        self.read_err = 0
        self.read_out = 0
        self.duration = None
        self.duration_second = None
        self.progress_item = []
        self.pts = []
        self.pts_second = []
        self.progress_percent = 0
        self.sub_process.readyReadStandardError.connect(self.read_std_error)
        self.sub_process.readyReadStandardOutput.connect(self.read_std_out)
        self.sub_process.finished.connect(self.reading_finished)

    def start_process(self):
        scene_sensitivity = 0.4
        output = self.output_frames_address()
        logging.debug("dddddddddddddddddddddddd"+os.path.join(output, '%05d.jpg'))

        self.sub_process.start(
            self.ffmpeg_url.path(),
            ['-i',
             self.video_url.path(),
             '-filter_complex',
             f'select=\'gt(scene,{scene_sensitivity})\' ,showinfo',
             '-vsync',
             'vfr',
             os.path.join(output, '%05d.jpg')
             ]
        )

    def read_std_error(self):
        self.read_err += 1
        data = self.sub_process.readAllStandardError()
        std_error = bytes(data).decode("utf8")
        logging.debug([self.read_err, std_error])
        if self.duration_second:
            self.process_spec(std_error)
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
        self.read_out += 1
        data = self.sub_process.readAllStandardOutput()
        std_output = bytes(data).decode("utf8")

    def reading_finished(self):
        pass

    def find_pts(self, std_error):
        result = re.search(r"pts_time:\d*.\d*", std_error)
        if result:
            self.pts.append(result.group()[9:])
            self.pts_second.append(float(result.group()[9:]))

    def process_spec(self, std_error):
        result_time = re.search(r" time=\d*:\d*:\d*.\d*", std_error)
        result_frame = re.search(r"frame= *\d*", std_error)
        result_fps = re.search(r" fps=\d*.\d* ", std_error)
        result_speed = re.search(r" speed= *\d*.\d*", std_error)
        if result_time and result_speed:
            time = result_time.group()[6:].strip()
            time_second = self.pts_to_second(time)
            frame = int(result_frame.group()[6:].strip())
            fps = float(result_fps.group()[5:].strip())
            speed = float(result_speed.group()[7:-1].strip())
            self.progress_item = {"time": time, "time_second": time_second, "speed": speed, "frame": frame, "fps": fps}
            logging.debug(self.progress_item)

    def output_frames_address(self):
        from PyQt5.QtCore import QFileInfo

        dirname, _ = os.path.split(os.path.abspath(__file__))
        file_info = QFileInfo(self.video_url.path())
        output_path = os.path.join(dirname, 'template')
        output_path = os.path.join(output_path, file_info.fileName() + "_" + str(time.strftime("%Y-%m-%d-%H-%M-%S")))

        try:
            if not os.path.exists(output_path):
                os.makedirs(output_path)
        except OSError as e:
            print('Error: Creating directory. ' + output_path)
            print(e)

        return output_path
