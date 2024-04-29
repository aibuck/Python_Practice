import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QComboBox
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lbResult = QLabel('선택 결과')
        self.initUI()

    def initUI(self):
        
        widget = QWidget()
        grid = QGridLayout()
        widget.setLayout(grid)

        grid.addWidget(QLabel('좋아하는 과일 : '), 0, 0)

        cb = QComboBox(self)
        cb.addItem('사과')
        cb.addItem('딸기')
        cb.addItem('포도')
        cb.addItem('앵두')


        #콤보박스 활성화시 동작할 함수에는 자동으로 text 결과가 전달된다.
        cb.activated[str].connect(self.onActivated)

        grid.addWidget(cb, 0, 1)
        grid.addWidget(self.lbResult, 1, 0)

        self.setCentralWidget(widget)

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.show()

    def onActivated(self, text):
        self.lbResult.setText(text)

if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
