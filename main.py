from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QLineEdit,
)

from py.MainVindow import MainWindow


def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == "__main__":
    main()
