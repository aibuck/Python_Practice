'''
#pip install Flas
from flask import Flask #웹페이지를 만들 수 있는 모듈
app = Flask(__name__) # cmd- pip install Flask

@app.route("/")
def hello():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000,debug=True)
    '''##


'''
from urllib import request
from bs4 import BeautifulSoup#cmd-pip install BeautifulSoup4

t= request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnid=108')

s = BeautifulSoup(t,'html.parser')

for location in s.select('location'):
    print('도시', location.select_one('city').string)
    print('날씨', location.select_one('wf').string)
    print('최저기온', location.select_one('tmn').string)
    print('최고기온', location.select_one('tmx').string)
    print()
    '''##


'''
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')

def hello():
    t = request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnid=108')
    s = BeautifulSoup(t,'html.parser')
    o=''
    
    for location in s.select('location'):#select()>전체 select_one()하나의 항목만
        o += '<h3>{}<h3>'.format(location.select_one('city').string)
        o += '날씨:{}<br/>'.format(location.select_one('wf').string)
        o += '최저/최고 기온: {}/{}'\
            .format(\
                location.select_one('tmn').string,
                location.select_one('tmx').string\
            )
        o += '<hr/>'
    return o
app.run('0.0.0.0', port=5000,debug=True)'''##


'''#S1 딕셔너리 값을 일일이 설정(노가다)
st = [
    {'name':'윤인성','korean':87,'math':98,'english':88,'science':95},
    {'name':'연하진','korean':92,'math':98,'english':96,'science':98},
    {'name':'구지연','korean':76,'math':96,'english':94,'science':90},
    {'name':'나선주','korean':98,'math':92,'english':96,'science':92},
    {'name':'윤아린','korean':95,'math':98,'english':98,'science':98},
    {'name':'윤명월','korean':64,'math':88,'english':92,'science':92}
]

print('이름', '총점', '평균', sep='\t')

for std in st:
    score_sum = std['korean'] + std['math']+\
        std['english'] + std['science']
    score_average = score_sum / 4

    print(std['name'], score_sum, score_average, sep = '\t')
    '''##



'''
def cs(name, korean, math, english, science):#S2 딕셔너리에 대응되는 키값을 함수로 표현
    return{
        'name':name,
        'korean':korean,
        'math':math,
        'english':english,
        'science':science
    }

st = [
    cs('윤인성', 87, 98, 88, 95),
    cs('연하진', 92, 98, 96, 9//////8),
    cs('구지연', 76, 96, 94, 90),
    cs('나선주', 98, 92, 96, 92),
    cs('윤아린', 95, 98, 98, 98),
    cs('윤명월', 64, 88, 92, 92),
]

print('이름', '총점', '평균', sep = '\t')
for std in st:
    score_sum = std['korean'] + std['math']+\
        std['english'] + std['science']
    score_average = score_sum / 4 #4=(len(std)-1) < (딕셔너리 키값 -1) [name 키값]은 제외 했으므로

    print(std['name'], score_sum, score_average, sep = '\t')
    '''##


'''
def cs(name, korean, math, english, science):#S3 함수 선언 후 def stdstring(std) 함수로 묶기
    return{
        'name':name,
        'korean':korean,
        'math':math,
        'english':english,
        'science':science
    }

def stdsum(std):
    return std['korean'] + std['math']+\
        std['english'] + std['science']

def stdaver(std):
    return stdsum(std) /4

def stdstring(std):
    return '{}\t{}\t{}\t'.format(
        std['name'],
        stdsum(std),
        stdaver(std))

st = [
    cs('윤인성', 87, 98, 88, 95),
    cs('연하진', 92, 98, 96, 98),
    cs('구지연', 76, 96, 94, 90),
    cs('나선주', 98, 92, 96, 92),
    cs('윤아린', 95, 98, 98, 98),
    cs('윤명월', 64, 88, 92, 92),
]

print('이름', '총점', '평균', sep = '\t')

for std in st:
    print(stdstring(std))
    '''##


'''
class Student: #S4 클래스 선언 클래스 = 속성이랑 메소드를 가지고있음, 객체를 찍어내는 틀

    #생성자
    def __init__(self, name, korean, math, english, science):#__init__
        # self 클래스 내부의 값
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def gsum(self):
        return self.korean + self.math+\
            self.english + self.science
    
    def gaver(self):
        return self.gsum()/4
    
    def to_string(self):
        return '{}\t{}\t{}'.format(\
            self.name,\
            self.gsum(),\
            self.gaver())

st = [
    Student('윤인성', 87, 98, 88, 95),#생성자는 클래스의 이름과 같음
    Student('연하진', 92, 98, 96, 98),
    Student('구지연', 76, 96, 94, 90),
    Student('나선주', 98, 92, 96, 92),
    Student('윤아린', 95, 98, 98, 98),
    Student('윤명월', 64, 88, 92, 92),
]

print('이름', '총점', '평균', sep = '\t')

for std in st:
    print(std.to_string())
'''##


'''
class Car:
    #속성, 멤버 변수
    model = 'BMW'
    color = 'white'
    
    def speedChange(self, v):#메소드
        print('speedChange')
        self.speed = v # self.() 는 클래스를 지정할때 꼭 써줘야함. 
                        #self.() = 인스턴스 변수, self.() != 클래스 변수
'''##


'''
class Car:
    #속성, 멤버 변수
    model = 'BMW'#__init__ 여부가 없음 = 생성자 함수에 매개변수가 없기 때문.
    color = 'white'

bmw = Car() #객체
benz = Car()

benz.model = 'Benz'
benz.color = 'black'

print(bmw.model)
print(bmw.color)

print(benz.model)
print(benz.color)
'''


'''
class Car:
    #멤버 변수
    c = 0
    s = 0
    def speedChange(self,v):
        Car.c += 1 #클래스 변수, 클래스끼리 값 공유 O
        self.s = v #인스턴스 변수, 클래스끼리 값 공유 x
bmw = Car()#객체생성
benz = Car()#객체생성

bmw.speedChange(100)
print('bmw speed :', bmw.s)
print('number of speedChange :', Car.c) #클래스 변수

benz.speedChange(120)
print('Benz speed :',benz.s)
print('number of speedChange', Car.c) #클래스 변수 2 , value = 1->2
'''


'''
class Car:
    #생성자 __init__
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def info(self):
        print('Model: ', self.model,', Color: ',self.color)

bmw = Car('BMW', 'white') #S1
bmw.info()

benz = Car('Benz', 'black')
benz.info()


bmw = Car('BMW', 'white') #S2
benz = Car('Benz', 'black')
bmw.info()
benz.info()
'''##


'''
class Person:
    name = 'kai'

kai = Person() #S1
print(kai.name)

print(person.name)#S2
'''


'''
class Person:
    def say(self):
        print('Welcome.')

kai = Person()
kai.say()
'''


'''
class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
    
    def intro(self):
        print('Name :', self.name)
        print('Weapon :',self.weapon)

lugo = Character('Lugo','gun')
lugo.intro() ##정답~ ^_^
''' ##


'''
class TV:
    
    def __init__(self, ch, vol):#__init__써서 생성자 정의
        self.ch = ch
        self.vol = vol
        self.power = True # = ('on', 'off') or =[0,1]

    def on_off(self):
        if self.power == True: #켜져있다면
            self.power = False #꺼주기
            print('power off')
        else: #꺼져있다면(=켜져있지 않다면)
            self.power = True #켜주기
            print('power on')

    def info(self):
        print('전원: ', self.power)
        print('채널: ', self.ch)
        print('볼륨: ', self.vol)


    def set_channel(self, ch):
        print('{}채널로 변경됨'.format(ch))
        # if self.power: (print 구문 대체)
            # self.ch = ch
        # else: (내가 추가한 구문)
            # print('전원이 꺼져있습니다.')
        
    def set_volume(self, vol):
        print('현재 볼륨:{}'.format(vol))
        # if self.power:
            # self.vol = vol
        # else:
            # print('전원이 꺼져있습니다.')
        
tv = TV(1,16)
tv.info()
tv.on_off()
tv.info()
tv.set_channel(5)
tv.set_channel(12)
tv.set_volume(10)
tv.set_volume(20)
tv.on_off()
tv.on_off()
'''##중요!



