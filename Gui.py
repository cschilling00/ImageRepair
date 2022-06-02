from PyQt5.QtWidgets import (QMainWindow, QProgressBar, QLineEdit,
                             QPushButton, QApplication, QLabel, QMessageBox)
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
import sys
import time

global win


# aktualisiert den Fortschrittsbalken
class ProgressCounter(QThread):

    ProgressChange = pyqtSignal(int)

    def run(self):
        import Main
        print('in run')
        while (Main.i + 1) * one_time_step < 100:
            print(Main.i)
            print("in while")
            print(round((Main.i + 1) * one_time_step))
            self.ProgressChange.emit(round((Main.i + 1) * one_time_step))
            time.sleep(1)
        self.ProgressChange.emit(round((Main.i + 1) * one_time_step))


# Lädt die Bilder und startet die Bildverarbeitung jeweils über die Main.py
class ImageProcessing(QThread):

    ImagesLoaded = pyqtSignal(bool)

    def run(self):
        import Main

        if not Main.load_all_images():
            self.ImagesLoaded.emit(False)
            print("ImageProcessing Images Loaded")
            print(self.ImagesLoaded)
        else:
            data, file_names = Main.load_all_images()
            self.ImagesLoaded.emit(True)
            steps = len(data)
            global one_time_step
            one_time_step = 100 / steps

            ProgressCounter.prog = ProgressCounter()
            ProgressCounter.prog.ProgressChange.connect(win.on_progress_change)
            ProgressCounter.prog.start()

            Main.main_processing(data, file_names)
            win.btn.setDisabled(False)

# Initialisiert die GUI
class ImageRepair(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblsource = QLabel(self)
        self.lbltarget = QLabel(self)
        self.lblread = QLabel(self)
        self.lblsource.setText('Quellordner als Pfad angeben:')
        self.lbltarget.setText('Zielordner als Pfad angeben:')

        self.qlesource = QLineEdit(self)
        self.qletarget = QLineEdit(self)
        self.qlesource.setText("../DamagedImages/")
        self.qletarget.setText("../RepairedImages0/")

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
        import Main
        Main.src_img_dir = self.qlesource.text()
        Main.target_dir = self.qletarget.text()
        self.lblread.setText('Loading all images ...')

        self.btn.setDisabled(True)

        self.improc = ImageProcessing()
        self.improc.ImagesLoaded.connect(self.images_loaded)
        self.improc.start()

    def images_loaded(self, value):
        self.lblread.setText("")
        if not value:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Der angegebene Quellordner existiert nicht!")
            msg.setWindowTitle("Warnung")
            msg.setStandardButtons(QMessageBox.Retry)
            retval = msg.exec_()
            win.btn.setDisabled(False)

    def on_progress_change(self, value):
        print("value change")
        print(value)
        self.pbar.setValue(value)


# Öffnet die GUI
def main():
    app = QApplication(sys.argv)
    global win
    win = ImageRepair()
    win.show()
    sys.exit(app.exec_())


main()
