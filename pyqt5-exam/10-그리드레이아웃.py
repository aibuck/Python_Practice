import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        widget = QWidget()
        grid = QGridLayout()
        widget.setLayout(grid)

        grid.addWidget(QLabel('보낸 사람:'), 0, 0)
        grid.addWidget(QLabel('받는 사람:'), 1, 0)
        grid.addWidget(QLabel('내용:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        # 메인윈도우 안에서 다른 요소를 모아담은 위젯을 추가할때
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