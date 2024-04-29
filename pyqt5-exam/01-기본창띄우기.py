import sys
from PyQt5.QtWidgets import QApplication, QWidget


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Application')
        self.move(600, 400)
        self.resize(600, 400)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
