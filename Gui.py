from PyQt5.QtWidgets import (QMainWindow, QProgressBar, QCheckBox, QLineEdit,
                             QPushButton, QApplication, QLabel)
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import Qt
import sys
import Main


class ImageRepair(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        cb = QCheckBox('Sort images', self)
        cb.move(50, 300)
        cb.setChecked(False)
        cb.stateChanged.connect(self.sort)

        self.lblsource = QLabel(self)
        self.lbltarget = QLabel(self)
        self.lblsource.setText('Enter source directory:')
        self.lbltarget.setText('Enter target directory:')
        self.qlesource = QLineEdit(self)
        self.qletarget = QLineEdit(self)
        self.qlesource.setText("../DamagedImages/")
        self.qletarget.setText("../RepairedImages0/")

        self.qlesource.move(200, 100)
        self.qletarget.move(200, 200)
        self.qlesource.setGeometry(200, 100, 300, 25)
        self.qletarget.setGeometry(200, 200, 300, 25)
        self.lblsource.move(50, 100)
        self.lbltarget.move(50, 200)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(300, 400, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(200, 400)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(600, 600, 650, 650)
        self.setWindowTitle('ImageRepair')
        self.btn.clicked.connect(self.onClick)

    def sort(self, state):
        if state == Qt.Checked:
            print('TODO')
            # execute sorter

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def onClick(self):
        Main.src_img_dir = self.qlesource.text()
        Main.target_dir = self.qletarget.text()
        self.btn.setDisabled(True)
        Main.irmain()
        self.btn.setDisabled(False)


def main():
    app = QApplication(sys.argv)
    win = ImageRepair()
    win.show()
    sys.exit(app.exec_())


main()
