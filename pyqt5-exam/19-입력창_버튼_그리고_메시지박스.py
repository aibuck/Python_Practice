import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, \
QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lineEdit = None
        self.initUI()

    def initUI(self):
        
        # 메인윈도우는 메뉴바와 상태바가 지원되는 창을 만든다.
        # 큐위젯은 다양한 위젯을 추가할 수 있는 공간을 만든다. 
        # 따라서 큐위젯을 메인윈도우에 포함할 수 있다.

        widget = QWidget()

        label = QLabel("아무 내용이나 입력하세요")
        label.setAlignment(Qt.AlignCenter)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(label)
        hbox1.addStretch(1)

        lineEdit = QLineEdit()
        self.lineEdit = lineEdit

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(lineEdit)
        hbox2.addStretch(1)

        pushButton = QPushButton("입력 확인")
        pushButton.clicked.connect(self.showMessage)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(pushButton)
        hbox3.addStretch(1)

        vbox = QVBoxLayout(widget)
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)

        self.setCentralWidget(widget)

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(400, 300)
        self.show()

    def showMessage(self) : 
        QMessageBox.question(self, 'Message', self.lineEdit.text(),
                                    QMessageBox.Close, QMessageBox.Close)
        

if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
