"""
만족시켜야할 최소한의 조건!
-이름, 나이, 지역 을 각각 입력받는 
    입력 요소(LineEdit)를 하나씩 포함하자!

-입력 요소들과 함께 버튼(PushButton) 하나도 함께 있어야 한다.

-실행 흐름은 다음과 같다.

1. 입력 요소에 이름, 나이, 지역을 각각 입력한다.
2. 버튼을 클릭한다.
3. 그러면 이름, 나이, 지역이 쓰여 있는 메시지 박스가 나타난다.
(QMessageBox)
"""


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.quest()
    
    def quest(self):
        widget = QWidget()
        grid = QGridLayout()
        widget.setLayout(grid)

        
        grid.addWidget(QLabel('이름'),0,0)
        grid.addWidget(QLabel('나이'),1,0)
        grid.addWidget(QLabel('지역'),2,0)

        grid.addWidget(QLineEdit(), 0, 1)#QLineEdit()안에 변수참조
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QLineEdit(), 2, 1)


        btn = QPushButton('입력',self)
        btn.resize(50,20)
        grid.addWidget(btn, 3, 0, 1, 2, alignment=Qt.AlignCenter)

        self.setCentralWidget(widget)

        btn.clicked.connect(self.showMessage)


        self.setWindowTitle('신상')
        self.move(600, 400)
        self.resize(400, 300)
        self.show()

    def showMessage(self):
        # 각각의 QLineEdit 위젯에서 텍스트를 가져옵니다.
        name_edit = self.centralWidget().layout().itemAtPosition(0, 1).widget()
        age_edit = self.centralWidget().layout().itemAtPosition(1, 1).widget()
        location_edit = self.centralWidget().layout().itemAtPosition(2, 1).widget()

        name = name_edit.text()
        age = age_edit.text()
        location = location_edit.text()

        # 메시지 상자에 텍스트를 표시합니다.
        QMessageBox.information(self, '입력 결과', f'이름: {name}\n나이: {age}\n지역: {location}', QMessageBox.Ok)


if __name__ == '__main__':#시스템 변수, 시스템 메서드
    master = QApplication(sys.argv) #sys.argv 에는 이 파일의 이름이 포함되어 있다.
    view = App()
    sys.exit(master.exec_())