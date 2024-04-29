import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        widget = QWidget() # 메인 위젯 (창을 채우는 용도)
        tab1 = QWidget() # 탭 메뉴에 포함될 하위 위젯
        tab2 = QWidget() # 탭 메뉴에 포함될 하위 위젯

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        vbox = QVBoxLayout(widget)
        vbox.addWidget(tabs)

        self.setCentralWidget(widget) #메인 위젯을 창에 넣다

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(400, 300)
        self.show()
        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
