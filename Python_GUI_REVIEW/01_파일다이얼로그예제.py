##01파일다이얼로그
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5.QtCore import QCoreApplication
import sys
import os


class App(QMainWindow):#메인 윈도우를 사용해야지만 상태창을 만들수있음.
    
    def __init__(self):
        super().__init__()#부모클래스 기반의 생성자 호출
        self.initUI()
    
    def initUI(self):#self는 객체 자신(나 자신,메인윈도우)
        
        #메뉴바 생성 및 메뉴 추가
        menubar = self.menuBar() #창에 추가할 메뉴바 생성
        menu1 = menubar.addMenu('파일')
        menu2 = menubar.addMenu('편집')

        #액션 생성 및 추가
        loadfile = QAction('불러오기',self)
        savefile = QAction('저장하기',self)
        quitApp = QAction('종료하기',self)

        loadfile.triggered.connect(self.load)
        savefile.triggered.connect(self.save)
        quitApp.triggered.connect(QCoreApplication.instance().quit) #프로그램 종료

        menu1.addAction(loadfile)#기능을 추가할때는 함수를 연결한다.
        menu1.addAction(savefile)
        menu1.addAction(quitApp)

        #메인 창에 대한 설정
        self.setWindowTitle('Review Program')
        self.move(0, 0)
        self.resize(400, 300)
        self.show()#보여준다는 선언
    
    def load(self):
        fname = QFileDialog.getOpenFileName(self, '불러오기', './')
        os.system(fname[0])

    def save(self):
        fname = QFileDialog.getSaveFileName(self, '저장하기', './')
        if fname[0] != '':#파일의 이름이 존재한다면
            with open(fname[0], 'w', encoding='utf8') as f:
                f.write('저장할 내용')


#이 파일을 직접적으로 실행시킬 때만!
if __name__ == '__main__':#시스템 변수, 시스템 메서드
    master = QApplication(sys.argv) #sys.argv 에는 이 파일의 이름이 포함되어 있다.
    view = App()
    sys.exit(master.exec_())