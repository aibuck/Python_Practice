import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        datetime = QDateTime.currentDateTime()

        label = QLabel(datetime.toString(), self)
        label.setAlignment(Qt.AlignCenter)

        font = label.font()
        font.setPointSize(12)

        label.setFont(font)
        label.setGeometry(100, 100, 200, 100)

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(400, 300)
        self.show()

if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
