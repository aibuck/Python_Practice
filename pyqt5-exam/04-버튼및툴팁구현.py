import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('BUTTON 3', self)
        btn1.setGeometry(250, 175, 100, 50) # 위치와 크기를 한번에 설정하기

        btn2 = QPushButton('BUTTON 2', self)
        btn2.setGeometry(150, 175, 100, 50)

        btn3 = QPushButton('BUTTON 1', self)
        btn3.setGeometry(50, 175, 100, 50)
        btn3.setToolTip('코드에선 3번이지만 화면에선 1번')

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
