import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QProgressBar
from PyQt5.QtCore import QBasicTimer # 시간 세는 넘


class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initialize() # 이 메소드 안에서 설정을 진행

    def initialize(self):

        self.pbar = QProgressBar(self) #self 인스턴스 !self 지역변수
        self.pbar.setGeometry(30, 40, 200, 25) #위치랑 크기 한꺼번에 정함

        self.btn = QPushButton('Start', self)
        self.btn.move(60,80)

        self.timer = QBasicTimer() #시간 셈
        self.step = 0 # 세어진 시간을 기록하는 넘
        self.btn.clicked.connect(self.doAction)





        #메인 창에 대한 설정
        self.setWindowTitle("Review Program")
        self.move(0,0)
        self.resize(230,150)
        self.show()


    #시계가 돌 때마다 뭐할지 정하기
    #-> 큐티는 시계가 돌때의 동작을 정의하는 메소드를 갖고있다!
    def timerEvent(self, event):

        if self.step >= 100:
            self.step = 0
            self.timer.stop()
            self.btn.setText('Restart')
            return

        self.step += 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100,self)
            self.btn.setText('Stop')


if __name__ == '__main__':#시스템 변수, 시스템 메서드
    master = QApplication(sys.argv) #sys.argv 에는 이 파일의 이름이 포함되어 있다.
    view = App()
    sys.exit(master.exec_())


# App() #메인윈도우 기능을 포함한 앱 객체가 생성된다.