#python -m venv guivenv
#guivenv\Scripts\activate.bat



##01_기본 창 띄우기
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget


# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('PyQt5 Application')
#         self.move(600, 400)
#         self.resize(600, 400)
#         self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     view = App()
#     sys.exit(app.exec_())



##02_아이콘추가하기
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QIcon


# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('penguin icon')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(600, 400)
#         self.show()


# if __name__ == '__main__':
#    print(sys.argv) #단순히 전달된 인자를 보는 용도
#    app = QApplication(sys.argv) #전달 인자를 응용프로그램에 전달
#    view = App()
#    sys.exit(app.exec_())



##03_버튼추가및창닫기
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QCoreApplication, Qt


# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         btn = QPushButton('Push Button', self)
#         btn.resize(100, 50)#버튼 크기 설정
#         btn.clicked.connect(QCoreApplication.instance().quit) # 클릭 시 어플리케이션 종료
#         btn.move(250, 175)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600,400)
#         self.resize(600,500)
#         self.show()


# if __name__ == '__main__':
#     print(sys.argv) #arguments verb : 시스템에 전달된 인자
#     app = QApplication(sys.argv)
#     view = App()
#     sys.exit(app.exec_())



##04_버튼및툴팁구현
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtGui import QIcon


# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
    
#     def initUI(self):
#         btn1 = QPushButton('BUTTON 3',self)
#         btn1.setGeometry(250, 175, 100, 50) # 위치와 크기를 한번에 설정하기
        
#         btn2 = QPushButton('BUTTON 2',self)
#         btn2.setGeometry(150, 175, 100, 50)

#         btn3 = QPushButton('BUTTON 3',self)
#         btn3.setGeometry(50, 175, 100, 50)
#         btn3.setToolTip('코드에선 3번이지만 화면에선 1번')

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()


# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##05_메뉴바만들기
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QCoreApplication

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         menubar = self.menuBar()
#         menu1 = menubar.addMenu('파일')
#         menu2 = menubar.addMenu('편집')

#         loadFile = QAction('불러오기', self)
#         saveFile = QAction('저장하기', self)
#         quitApp = QAction('종료하기', self)

#         #클릭 시 동작 추가하기
#         loadFile.triggered.connect(self.add_open)
#         saveFile.triggered.connect(self.add_save)
#         quitApp.triggered.connect(QCoreApplication.instance().quit)

#         menu1.addAction(loadFile)
#         menu1.addAction(saveFile)
#         menu1.addAction(quitApp)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

#     def add_open(self):
#         pass

#     def add_save(self):
#         pass

# if __name__ == '__main__':
#     print(sys.argv)
#     app = QApplication(sys.argv)
#     view = App()
#     sys.exit(app.exec_())



##06_파일다이얼로그추가
# import os
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QWidget
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QCoreApplication, Qt

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         menubar = self.menuBar()
#         menu1 = menubar.addMenu('파일')
#         menu2 = menubar.addMenu('편집')

#         loadFile = QAction('불러오기', self)
#         saveFile = QAction('저장하기', self)
#         quitApp = QAction('종료하기', self)

#         #클릭 시 동작 추가하기
#         loadFile.triggered.connect(self.add_open)
#         saveFile.triggered.connect(self.add_save)
#         quitApp.triggered.connect(QCoreApplication.instance().quit)

#         menu1.addAction(loadFile)
#         menu1.addAction(saveFile)
#         menu1.addAction(quitApp)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

#     #파일을 선택하면 해당 파일이 열림(실행됨)
#     def add_open(self):
#         fname = QFileDialog.getOpenFileName(self,'불러오기','./')
#         os.system(fname[0])

#     #파일명을 입력하고 저장하면 폴더에 파일이 추가됨
#     def add_save(self):
#         fname = QFileDialog.getSaveFileName(self, '저장하기', './')
#         with open(fname[0],'w',encoding='utf8') as f:
#             f.write('저장할 내용')


# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##07_날짜와시간
# from PyQt5.QtCore import QDateTime

# datetime = QDateTime.currentDateTime()

# print(datetime.toString())
# print(datetime.toString('d.M.yy hh:mm:ss'))
# print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))


##08_날짜와시간라벨
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtCore import Qt, QDateTime
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
    
#     def initUI(self):

#         datetime = QDateTime.currentDateTime()

#         label = QLabel(datetime.toString(), self)
#         label.setAlignment(Qt.AlignCenter)

#         font = label.font()
#         font.setPixelSize(12)

#         label.setFont(font)
#         label.setGeometry(100, 100, 200, 100)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##09_박스레이아웃
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout
# from PyQt5.QtCore import Qt, QDateTime
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
        
#         #메인윈도우는 메뉴바와 상태바가 지원되는 창을 만든다.
#         #큐위젯은 다양한 위젯을 추가할 수 있는 공간을 만든다.
#         #따라서 큐위젯을 메인윈도우에 포함할 수 있다.

#         widget = QWidget()
#         datetime = QDateTime.currentDateTime()

#         label1 = QLabel(datetime.toString('d.M.yy hh:mm:ss'))
#         label1.setAlignment(Qt.AlignCenter)
#         font2 = label1.font()
#         font2.setPointSize(12)
#         label1.setFont(font2)
#         label1.resize(100, 50)

#         label2 = QLabel(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
#         label2.setAlignment(Qt.AlignCenter)
#         font3 = label2.font()
#         font3.setPointSize(12)
#         label2.setFont(font3)
#         label2.resize(100, 50)

#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(label1)
#         hbox.addStretch(1)
#         hbox.addWidget(label2)
#         hbox.addStretch(1)

#         vbox = QVBoxLayout(widget)
#         vbox.addStretch(3)
#         vbox.addLayout(hbox)
#         vbox.addStretch(1)

#         self.setCentralWidget(widget)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##10_그리드레이아웃
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
        
#         widget = QWidget()
#         grid = QGridLayout()
#         widget.setLayout(grid)

#         grid.addWidget(QLabel('보낸 사람:'), 0, 0)
#         grid.addWidget(QLabel('받는 사람:'), 1, 0)
#         grid.addWidget(QLabel('내용:'), 2, 0)

#         grid.addWidget(QLineEdit(), 0, 1)
#         grid.addWidget(QLineEdit(), 1, 1)
#         grid.addWidget(QTextEdit(), 2, 1)

#         # 메인윈도우 안에서 다른 요소를 모아만든 위젯을 추가할때
#         self.setCentralWidget(widget)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##11_체크박스
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QCheckBox
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.cbList = [QCheckBox('돈까스'), QCheckBox('햄버거'), QCheckBox('감자탕')]
#         self.initUI()

#     def initUI(self):
        
#         widget = QWidget()
        
#         hbox1 = QHBoxLayout()
#         hbox1.addStretch(1)
#         hbox1.addWidget(QLabel('좋아하는 음식을 모두 고르시오'))
#         hbox1.addStretch(1)

#         hbox2 = QHBoxLayout()
#         hbox2.addStretch(1)
#         hbox2.addWidget(self.cbList[0])
#         hbox2.addWidget(self.cbList[1])
#         hbox2.addWidget(self.cbList[2])
#         hbox2.addStretch(1)

#         hbox3 = QHBoxLayout()
#         hbox3.addStretch(1)
#         btn = QPushButton('선택 항목 확인')
#         btn.clicked.connect(self.showCheckedFood)
#         hbox3.addWidget(btn)
#         hbox3.addStretch(1)

#         vbox = QVBoxLayout(widget)
#         vbox.addStretch(1)
#         vbox.addLayout(hbox1)
#         vbox.addLayout(hbox2)
#         vbox.addLayout(hbox3)
#         vbox.addStretch(1)


#         self.setCentralWidget(widget)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

#     def showCheckedFood(self) : 
#         for cb in self.cbList :
#             if cb.isChecked() : #체크박스 선택여부
#                 print(cb.text())

# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##12_라디오버튼
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QRadioButton
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.rbList = [QRadioButton('돈까스'), QRadioButton('햄버거'), QRadioButton('감자탕')]
#         self.initUI()

#     def initUI(self):
        
#         widget = QWidget()
        
#         hbox1 = QHBoxLayout()
#         hbox1.addStretch(1)
#         hbox1.addWidget(QLabel('좋아하는 음식을 하나만 고르시오'))
#         hbox1.addStretch(1)

#         hbox2 = QHBoxLayout()
#         hbox2.addStretch(1)
#         hbox2.addWidget(self.rbList[0])
#         hbox2.addWidget(self.rbList[1])
#         hbox2.addWidget(self.rbList[2])
#         hbox2.addStretch(1)

#         hbox3 = QHBoxLayout()
#         hbox3.addStretch(1)
#         btn = QPushButton('선택 항목 확인')
#         btn.clicked.connect(self.showCheckedFood)
#         hbox3.addWidget(btn)
#         hbox3.addStretch(1)

#         vbox = QVBoxLayout(widget)
#         vbox.addStretch(1)
#         vbox.addLayout(hbox1)
#         vbox.addLayout(hbox2)
#         vbox.addLayout(hbox3)
#         vbox.addStretch(1)


#         self.setCentralWidget(widget)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

#     def showCheckedFood(self) : 
#         for cb in self.rbList :
#             if cb.isChecked() :
#                 print(cb.text())

# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##13_콤보박스
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QComboBox
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.lbResult = QLabel('선택 결과')
#         self.initUI()

#     def initUI(self):
        
#         widget = QWidget()
#         grid = QGridLayout()
#         widget.setLayout(grid)

#         grid.addWidget(QLabel('좋아하는 과일 : '), 0, 0)

#         cb = QComboBox(self)
#         cb.addItem('사과')
#         cb.addItem('딸기')
#         cb.addItem('포도')
#         cb.addItem('앵두')


#         #콤보박스 활성화시 동작할 함수에는 자동으로 text 결과가 전달된다.
#         cb.activated[str].connect(self.onActivated)

#         grid.addWidget(cb, 0, 1)
#         grid.addWidget(self.lbResult, 1, 0)

#         self.setCentralWidget(widget)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.show()

#     def onActivated(self, text):
#         self.lbResult.setText(text)

# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##14_프로그래스바
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QProgressBar
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QBasicTimer

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
        
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 200, 25)

#         self.btn = QPushButton('Start', self)
#         self.btn.move(60, 80)
#         self.btn.clicked.connect(self.doAction)

#         self.timer = QBasicTimer()
#         self.step = 0

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(230, 150)
#         self.show()

#     # QObject 및 하위 클래스 기반 객체들은 timerEvent()를 갖는다.
#     # self.timer에 대한 이벤트 핸들러 역할을 수행한다.
#     def timerEvent(self, e):
#         if self.step >= 100:
#             self.step = 0
#             self.timer.stop()
#             self.btn.setText('Restart')
#             return

#         self.step = self.step + 1
#         self.pbar.setValue(self.step)

#     def doAction(self):
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('Start')
#         else:
#             self.timer.start(100, self)
#             self.btn.setText('Stop')

# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##15_탭메뉴
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
        
#         widget = QWidget() # 메인 위젯 (창을 채우는 용도)
#         tab1 = QWidget() # 탭 메뉴에 포함될 하위 위젯
#         tab2 = QWidget() # 탭 메뉴에 포함될 하위 위젯

#         # # 추가된 코드: tab1 안에 또 다른 탭 추가
#         # nested_tabs = QTabWidget()
#         # nested_tab1 = QWidget()
#         # nested_tab2 = QWidget()
#         # nested_tabs.addTab(nested_tab1, 'Nested Tab1')
#         # nested_tabs.addTab(nested_tab2, 'Nested Tab2')

#         # # 추가된 코드: tab1 안에 또 다른 탭을 포함시키기 위해 QVBoxLayout 사용
#         # tab1_layout = QVBoxLayout()
#         # tab1_layout.addWidget(nested_tabs)
#         # tab1.setLayout(tab1_layout)

#         tabs = QTabWidget()
#         tabs.addTab(tab1, 'Tab1')
#         tabs.addTab(tab2, 'Tab2')

#         vbox = QVBoxLayout(widget)
#         vbox.addWidget(tabs)

#         self.setCentralWidget(widget) #메인 위젯을 창에 넣다

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()
        
# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##16_입력다이얼로그
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QInputDialog
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
        
#         widget = QWidget()
#         grid = QGridLayout()
#         widget.setLayout(grid)

        
#         self.btn = QPushButton('창 띄우기', self)
#         self.btn.clicked.connect(self.showDialog)

#         grid.addWidget(self.btn, 0, 0)

#         self.setCentralWidget(widget)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()
        
#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, '입력 창', '아무거나 쓰세요 :')

#         if ok:
#             print(text)

# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##17_색상다이얼로그
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QColorDialog
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
        
#         widget = QWidget()
#         grid = QGridLayout()
#         widget.setLayout(grid)

        
#         self.btn = QPushButton('창 띄우기', self)
#         self.btn.clicked.connect(self.showDialog)

#         grid.addWidget(self.btn, 0, 0)

#         self.setCentralWidget(widget)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()
        
#     def showDialog(self):
#         color = QColorDialog.getColor()

#         if color.isValid():
#             print('선택한 색상 : %s }' % color.name())
        
# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



#18_메시지박스
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

#     # QObject 및 하위 클래스 기반 객체들은 closeEvent()를 갖는다.
#     # close 에 대한 이벤트 핸들러 역할을 수행한다.    
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
#                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
        
# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())



##19_실습과제
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, \
# QVBoxLayout, QLineEdit, QPushButton, QMessageBox
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QIcon

# class App(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.lineEdit = None
#         self.initUI()

#     def initUI(self):
        
#         # 메인윈도우는 메뉴바와 상태바가 지원되는 창을 만든다.
#         # 큐위젯은 다양한 위젯을 추가할 수 있는 공간을 만든다. 
#         # 따라서 큐위젯을 메인윈도우에 포함할 수 있다.

#         widget = QWidget()

#         label = QLabel("아무 내용이나 입력하세요")
#         label.setAlignment(Qt.AlignCenter)

#         hbox1 = QHBoxLayout()
#         hbox1.addStretch(1)
#         hbox1.addWidget(label)
#         hbox1.addStretch(1)

#         lineEdit = QLineEdit()
#         self.lineEdit = lineEdit

#         hbox2 = QHBoxLayout()
#         hbox2.addStretch(1)
#         hbox2.addWidget(lineEdit)
#         hbox2.addStretch(1)

#         pushButton = QPushButton("입력 확인")
#         pushButton.clicked.connect(self.showMessage)

#         hbox3 = QHBoxLayout()
#         hbox3.addStretch(1)
#         hbox3.addWidget(pushButton)
#         hbox3.addStretch(1)

#         vbox = QVBoxLayout(widget)
#         vbox.addStretch(1)
#         vbox.addLayout(hbox1)
#         vbox.addLayout(hbox2)
#         vbox.addLayout(hbox3)
#         vbox.addStretch(1)

#         self.setCentralWidget(widget)

#         self.setWindowTitle('PyQt5 Application')
#         self.setWindowIcon(QIcon('penguin-icon.ico'))
#         self.move(600, 400)
#         self.resize(400, 300)
#         self.show()

#     def showMessage(self) : 
#         QMessageBox.question(self, 'Message', self.lineEdit.text(),
#                                     QMessageBox.Close, QMessageBox.Close)
        

# if __name__ == '__main__':
#    print(sys.argv)
#    app = QApplication(sys.argv)
#    view = App()
#    sys.exit(app.exec_())