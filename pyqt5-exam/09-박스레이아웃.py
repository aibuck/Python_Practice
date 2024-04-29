import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        #메인윈도우는 메뉴바와 상태바가 지원되는 창을 만든다.
        #큐위젯은 다양한 위젯을 추가할 수 있는 공간을 만든다.
        #따라서 큐위젯을 메인윈도우에 포함할 수 있다.

        widget = QWidget()
        datetime = QDateTime.currentDateTime()

        label1 = QLabel(datetime.toString('d.M.yy hh:mm:ss'))
        label1.setAlignment(Qt.AlignCenter)
        font2 = label1.font()
        font2.setPointSize(12)
        label1.setFont(font2)
        label1.resize(100, 50)

        label2 = QLabel(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
        label2.setAlignment(Qt.AlignCenter)
        font3 = label2.font()
        font3.setPointSize(12)
        label2.setFont(font3)
        label2.resize(100, 50)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(label1)
        hbox.addStretch(1)
        hbox.addWidget(label2)
        hbox.addStretch(1)

        vbox = QVBoxLayout(widget)
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setCentralWidget(widget)

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