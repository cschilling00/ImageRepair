from PyQt5.QtWidgets import (QMainWindow, QProgressBar, QCheckBox, QLineEdit,
                             QPushButton, QApplication, QLabel)
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
import sys
import time
import Main

global win

class ProgressCounter(QThread):

    ProgressChange = pyqtSignal(int)

    def run(self):
        print('in run')
        while (Main.i + 1) * one_time_step < 100:
            print("in while")
            print(round((Main.i + 1) * one_time_step))
            self.ProgressChange.emit(round((Main.i + 1) * one_time_step))
            time.sleep(1)
        self.ProgressChange.emit(round((Main.i + 1) * one_time_step))



class ImageProcessing(QThread):

    ImagesLoaded = pyqtSignal(bool)

    def run(self):
        data, file_names = Main.load_all_images()
        self.ImagesLoaded.emit(True)
        steps = len(data)
        global one_time_step
        one_time_step = 100 / steps

        ProgressCounter.prog = ProgressCounter()
        ProgressCounter.prog.ProgressChange.connect(win.on_progress_change)
        ProgressCounter.prog.start()

        Main.main(data, file_names)
        win.btn.setDisabled(False)


class ImageRepair(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblsource = QLabel(self)
        self.lbltarget = QLabel(self)
        self.lblread = QLabel(self)
        self.lblsource.setText('Enter source directory:')
        self.lbltarget.setText('Enter target directory:')

        self.qlesource = QLineEdit(self)
        self.qletarget = QLineEdit(self)
        self.qlesource.setText("../DamagedImages/")
        self.qletarget.setText("../RepairedImages0/")

        # self.qlesource.move(200, 100)
        # self.qletarget.move(200, 200)
        self.qlesource.setGeometry(200, 100, 300, 25)
        self.qletarget.setGeometry(200, 200, 300, 25)
        self.lblsource.setGeometry(50, 100, 150, 25)
        self.lbltarget.setGeometry(50, 200, 150, 25)
        self.lblread.move(50, 350)

        self.pbar = QProgressBar(self)
        self.pbar.setMaximum(100)
        self.pbar.setGeometry(320, 400, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(200, 400)

        self.setGeometry(600, 600, 650, 650)
        self.setWindowTitle('ImageRepair')
        self.btn.clicked.connect(self.on_click)

    def on_click(self):
        Main.src_img_dir = self.qlesource.text()
        Main.target_dir = self.qletarget.text()
        self.lblread.setText('Loading all images ...')

        # data, file_names = Main.load_all_images()

        self.btn.setDisabled(True)

        self.improc = ImageProcessing()
        self.improc.ImagesLoaded.connect(self.images_loaded)
        self.improc.start()

        # Main.main(data, file_names)

    def images_loaded(self, value):
        if value:
            self.lblread.setText("")

    def on_progress_change(self, value):
        print("value change")
        print(value)
        self.pbar.setValue(value)


def main():
    app = QApplication(sys.argv)
    global win
    win = ImageRepair()
    win.show()
    sys.exit(app.exec_())


main()
