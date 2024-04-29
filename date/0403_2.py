# import random

# lotto_range = range(1,46)


# for i in range(5):
#     # print(random.sample(lotto_range,6))
#     lotto_numbers = random.sample(lotto_range, 6)
#     lotto_numbers.sort()  # 정렬
#     print(lotto_numbers)


##콘솔에 표시됨
# import tkinter
# import tkinter.font
# import random

# lotto_num = range(1,46)

# def buttonClick():
#     print(random.sample(lotto_num,6))

# window=tkinter.Tk()
# window.title("lotto")
# window.geometry("400x200")
# window.resizable(False, False)

# button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
# button.pack()

# window.mainloop()



##화면에 표시됨
# import tkinter
# import tkinter.font
# import random

# lotto_range = range(1,46)

# def buttonClick():
#     lotto_numbers = random.sample(lotto_range, 6)
#     lotto_numbers.sort()  # 정렬
#     label = tkinter.Label(window, text=str(lotto_numbers))#S1
#     # label = tkinter.Label(window, text=str(random.sample(lotto_range,6)))#S2
#     label.pack()

# window = tkinter.Tk()
# window.title("lotto")
# window.geometry("400x200")
# window.resizable(False,False)

# button = tkinter.Button(window, overrelief="solid",text="번호확인",width=15,\
#                 command=buttonClick, repeatdelay=1000, repeatinterval=100)
# button.pack()

# window.mainloop()



##폰트 크기 조정하기! 72번 , 73번 라인에 font = ... 추가함!
import tkinter
import tkinter.font
import random

lotto_range = range(1,46)

def buttonClick():
    lotto_numbers = random.sample(lotto_range, 6)
    lotto_numbers.sort()  # 정렬
    label = tkinter.Label(window, text=str(lotto_numbers), font = tkinter.font.Font(size=20))#S1
    # label = tkinter.Label(window, text=str(random.sample(lotto_range,6)), font=("Arial", 12))#S2
    label.pack()

window = tkinter.Tk()
window.title("lotto")
window.geometry("500x300")
window.resizable(False,False)

button = tkinter.Button(window, overrelief="solid",text="번호확인",width=15,\
                command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()