import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QRadioButton
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.rbList = [QRadioButton('돈까스'), QRadioButton('햄버거'), QRadioButton('감자탕')]
        self.initUI()

    def initUI(self):
        
        widget = QWidget()
        
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(QLabel('좋아하는 음식을 하나만 고르시오'))
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.rbList[0])
        hbox2.addWidget(self.rbList[1])
        hbox2.addWidget(self.rbList[2])
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        btn = QPushButton('선택 항목 확인')
        btn.clicked.connect(self.showCheckedFood)
        hbox3.addWidget(btn)
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

    def showCheckedFood(self) : 
        for cb in self.rbList :
            if cb.isChecked() :
                print(cb.text())

if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
