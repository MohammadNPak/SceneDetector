from PyQt5.QtWidgets import QDialog
from ui.UI_SettingDialog import Ui_Dialog


class SettingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.sensitivitySlider.valueChanged.connect(self.sensitivity_slider_value_changed)

    def sensitivity_slider_value_changed(self, value):
        self.ui.sensitivityLabel.setText(str(value / 100))
