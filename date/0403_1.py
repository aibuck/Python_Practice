import tkinter

window = tkinter.Tk()

#창의 속성 정하기
window.title("My TK Window") #창 제목 정하기
window.geometry("600x300") #창크기 정하기
window.resizable(False,False) #확대/축소 여부 정하기

# 첫 번째 위젯 추가하기
import tkinter.font
# tkinter.font.Font(size=48)
label = tkinter.Label(master = window, text="Hello GUI", font = tkinter.font.Font(size=48))
label.pack() #라벨을 추가하기


window.mainloop() #창의 실행을 유지한다.
