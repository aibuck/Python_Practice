import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
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

    # 파일을 선택하면 해당 파일이 열림(실행됨)
    def add_open(self):
        fname = QFileDialog.getOpenFileName(self, '불러오기', './')
        os.system(fname[0])

    # 파일명을 입력하고 저장하면 폴더에 파일이 추가됨
    def add_save(self):
        fname = QFileDialog.getSaveFileName(self, '저장하기', './')
        if fname[0] != '' :
            with open(fname[0], 'w', encoding='utf8') as f :
                f.write('저장할 내용')
            
 
if __name__ == '__main__':
   print(sys.argv)
   app = QApplication(sys.argv)
   view = App()
   sys.exit(app.exec_())
