import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Push Button', self)
        btn.resize(100, 50) # 버튼 크기 설정 
        btn.clicked.connect(QCoreApplication.instance().quit) # 클릭 시 어플리케이션 종료
        btn.move(250, 175) 

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(600, 400)
        self.show()


if __name__ == '__main__':
   print(sys.argv) #arguments verb : 시스템에 전달된 인자
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
