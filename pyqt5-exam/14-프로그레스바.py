import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QBasicTimer

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(60, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(230, 150)
        self.show()

    # QObject 및 하위 클래스 기반 객체들은 timerEvent()를 갖는다.
    # self.timer에 대한 이벤트 핸들러 역할을 수행한다.
    def timerEvent(self, e):
        if self.step >= 100:
            self.step = 0
            self.timer.stop()
            self.btn.setText('Restart')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())