from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# Window Start
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Stopwatch")
        self.setGeometry(100, 100, 400, 500)
        self.UiComponents()

        self.show()

    def UiComponents(self):
        self.count = 0
        self.flag = False

        self.timeLabel = QLabel(self)
        self.timeLabel.setGeometry(75, 100, 250, 70)
        self.timeLabel.setStyleSheet("border: 1em solid black;")

        startBtn = QPushButton("Start", self)
        startBtn.setGeometry(125, 250, 150, 40)
        startBtn.setStyleSheet("""
            font-size: 25px;
            text-transform: uppercase;
            background-color: skyblue;
            color: black;
            padding: 0;
            border: none;
        """)
        # startBtn.pressed.connect(self.startAppTimer)

        pauseBtn = QPushButton("Pause", self)
        pauseBtn.setGeometry(125, 300, 150, 40)
        pauseBtn.setStyleSheet("""
            font-size: 25px;
            text-transform: uppercase;
            background-color: skyblue;
            color: black;
            border: none;
        """)
        # pauseBtn.pressed.connect(self.pauseAppTimer)

        resetBtn = QPushButton("Reset", self)
        resetBtn.setGeometry(125, 350, 150, 40)
        resetBtn.setStyleSheet("""
            font-size: 25px;
            text-transform: uppercase;
            background-color: skyblue;
            color: black;
            border: none;
        """)
        # resetBtn.pressed.connect(self.resetAppTimer)

        timer = QTimer(self)
        # timer.timeout.connect(self.showTime)
        timer.start(100)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())