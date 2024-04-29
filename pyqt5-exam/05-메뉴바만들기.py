import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        menubar = self.menuBar()
        menu1 = menubar.addMenu("파일")
        menu2 = menubar.addMenu("편집")

        loadFile = QAction('불러오기', self)
        saveFile = QAction('저장하기', self)
        quitApp = QAction('종료하기',self)
 
        # 클릭 시 동작 추가하기 
        loadFile.triggered.connect(self.add_open)
        saveFile.triggered.connect(self.add_save)
        quitApp.triggered.connect(QCoreApplication.instance().quit)
 
        menu1.addAction(loadFile)
        menu1.addAction(saveFile)
        menu1.addAction(quitApp)

        self.setWindowTitle('PyQt5 Application')
        self.setWindowIcon(QIcon('penguin-icon.ico'))
        self.move(600, 400)
        self.resize(400, 300)
        self.show()

    def add_open(self):
        pass

    def add_save(self):
        pass
 
if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
