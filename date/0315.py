# class Car:
    # def __init__(self, model, color):
        # self.model = model
        # self.color = color
    # def info(self):
        # print('Model : ', self.model, ' , Color : ',self.color)
# 
# class CarDrive(Car):
    # def speedChange(self, v):
        # self.speed = v
        # print('speedChange : ', self.speed)
# 
# bmw = CarDrive('BMW', 'white')
# bmw.info()
# bmw.speedChange(100)##
# 



# class Car:
    # def __init__(self, model, color):
        # self.model = model
        # self.color = color
    # def info(self):
        # print('Model : ', self.model, '\tColor : ', self.color)
# 
# class CarDrive(Car):
    # def info(self):#메소드 오버라이딩
        # super().info() # 부모 클래스에서 가져오고 싶은 값 super().~~
        # print('The model of this car is %s.'%self.model)
        # print('The color is %s.'%self.color)
    # def speedChange(self, v):
        # self.speed = v
# 
        # print('speedChange :', self.speed)
# 
# bmw = CarDrive('BMW', 'white')
# bmw.info() ##



# class Apple:
    # def intro(self):
        # print('This is apple.')
# class Fruit(Apple):
    # def intro(self, fruit):
        # print('This is %s.'%fruit)
# 
# obj = Fruit()
# obj.intro('banana')
# 
# Apple.intro(obj) # 오버라이딩 했을때 부모 클래스의 값을 가져오려면
                ## 부모클래스이름.함수이름(자식클래스)
                ## 위에서는 obj = Fruit() 이므로 Apple.intro(obj)



# class Character:
#     def __init__(self, name, weapon):
#         self.name = name #인스턴스 변수
#         self.weapon = weapon
#     def intro(self):
#         print('Name :', self.name)
#         print('Weapon :', self.weapon)
# lugo = Character('Lugo', 'gun') #인스터스화
# lugo.intro()

#Character 클래스 상속
# class Action(Character):#부모함수의 __init__이 상속됨
#                         #자식함수에도 __init__ 삽입 가능
#     step = 0

#     def move_forward(self,n):#s앞으로 n만큼 이동하는 메소드
#         self.step += n #인스턴스 변수
#         print('Current location is %d.'%self.step)

#     #s뒤로 n만큼 이동하는 메소드
#     def move_backward(self,n):
#         self.step -= n #int() 명시 안해도 됨

#     #s오른쪽으로 회전하는 메소드
#     def turn_right(self):
#         print('Turn right.')

#     #왼쪽으로 회전하는 메소드
#     def turn_left(self):
#         print('Turn left.')

# lugo = Character('Lugo','gun') #loc= Action('Lugo, gun') #정답
# lugo.intro()

# loc = Action(0,0)
# loc.move_forward(10)
# loc.move_backward(3)
# loc.turn_right()
# loc.turn_left()
        


# class Student:
#     def __init__(self):
#         pass
# std = Student()

# print(isinstance(std, Student)) 
            ## isinstance()함수는
            ## isinstance(인스턴스, 클래스) 형식으로 쓰며
            ## (인스턴스 값이 클래스에 만들어져 있는지)
            ## True,False로 출력해줌



# class Student:
#     def study(self):
#         print('공부를 합니다.')
    
# class Teacher:
#     def teach(self):
#         print('학생을 가르칩니다.')

# croom = [Student(), Student(), Teacher(), Student(), Student()]

# for person in croom:
#     if isinstance(person, Student):
#         person.study()
#     elif isinstance(person, Teacher):
#         person.teach()



# class Student: #문자열로 변환
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
    
#     def get_sum(self):
#         return self.korean + self.math + self.english +\
#             self.science

#     def get_average(self):
#         return self.get_sum() / 4
    
#     def __str__(self):
#         return '{}\t{}\t{}'.format(
#             self.name,
#             self.get_sum(),
#             self.get_average())
    
# st = [
#     Student('ㄱ',87,98,88,95),
#     Student('ㄴ',92,98,96,98),
#     Student('ㄷ',76,96,94,90),
#     Student('ㄹ',98,92,96,92),
#     Student('ㅁ',95,98,98,98),
#     Student('ㅂ',64,88,92,92)
# ]

# print('이름','총점','평균', sep = '\t')
# for std in st:
#     print(str(std))



# class Student: #다양한__~~__ 함수 지정(활용)해보기
#     c=0

#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
    
#     def get_sum(self):
#         return self.korean + self.math + self.english +\
#             self.science

#     def get_average(self):
#         return self.get_sum() / 4
    
#     def __str__(self):
#         return '{}\t{}\t{}'.format(
#             self.name,
#             self.get_sum(),
#             self.get_average())
    
#     def __eq__(self,value):
#         return self.get_sum == value.get_sum()
#     def __ne__(self, value):
#         return self.get_sum() != value.get_sum()
#     def __gt__(self, value):
#         return self.get_sum() > value.get_sum()
#     def __ge__(self, value):
#         return self.get_sum() >= value.get_sum()
#     def __it__(self, value):
#         return self.get_sum() < value.get_sum()
#     def __le__(self, value):
#         return self.get_sum() <= value.get_sum()
    
# st = [
#     Student('ㄱ',87,98,88,95),
#     Student('ㄴ',92,98,96,98),
#     Student('ㄷ',76,96,94,90),
#     Student('ㄹ',98,92,96,92),
#     Student('ㅁ',95,98,98,98),
#     Student('ㅂ',64,88,92,92)
# ]

# st_a = Student('ㄱ',87,98,88,95),
# st_b = Student('ㄴ',92,98,96,98),

# print('st_a == st_b =', st_a == st)
# print(st_a != st_b)
# print(st_a > st_b)
# print(st_a >= st_b)
# print(st_a < st_b)
# print(st_a <= st_b)



# class Student: #계산한 학생 수 출력하기++
#     c=0
    
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science

#         Student.c += 1
#         print('{}번째 학생이 생성되었습니다.'.format(Student.c))

# st = [
#     Student('ㄱ',87,98,88,95),
#     Student('ㄴ',92,98,96,98),
#     Student('ㄷ',76,96,94,90),
#     Student('ㄹ',98,92,96,92),
#     Student('ㅁ',95,98,98,98),
#     Student('ㅂ',64,88,92,92)
# ]

# print()
# print('현재 생성된 총 학생 수는 {}명입니다.'.format(Student.c))



# def test(fun):
#     def wrapper():
#         print('인사가 시작되었습니다.')
#         fun()
#         print('인사가 종료되었습니다.')
#     return wrapper
    
# @test
# def hi():
#     print('hi')

# hi()



# class Student:
#     c = 0
#     st = []

#     @classmethod
#     def print(cls):
#         print('---- 학생목록 ----')
#         print('이름\t총점\t평균')
#         for std in cls.st:
#             print(str(std))
#         print('---- ---- ----')
    
#     def __init__(self,name,korean,math,english,science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#         Student.c += 1
#         Student.st.append(self)

#     def get_sum(self):
#         return self.korean + self.math+\
#             self.english + self.science
    
#     def get_average(self):
#         return self.get_sum() / 4
    
#     def __str__(self):
#         return '{}\t{}\t{}'.format(
#             self.name,
#             self.get_sum(),
#             self.get_average())
    

# Student('ㄱ',87,98,88,95),
# Student('ㄴ',92,98,96,98),
# Student('ㄷ',76,96,94,90),
# Student('ㄹ',98,92,96,92),
# Student('ㅁ',95,98,98,98),
# Student('ㅂ',64,88,92,92)


# Student.print()



# class Test:##가비지 컬렉터
#     def __init__(self,name):
#         self.name = name
#         print('{} - 생성되었습니다'.format(self.name))
#     def __del__(self):
#         print('{} - 파괴되었습니다'.format(self.name))
# Test('A')
# Test('B')
# Test('C')



# import math

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius #__ = 프라이빗 변수
#     def get_circumference(self):
#         return 2 * math.pi *self.__radius
#     def get_area(self):
#         return math.pi * (self.__radius **2)
    
#     def get_radius(self):
#         return self.__radius
#     def set_radius(self, value):
#         self.__radius = value

# circle = Circle(10)
# # circle = Circle(int(input('반지름')))
# print('#원의 둘레와 넓이')
# print('둘레 : ',circle.get_circumference())
# print('넓이 : ',circle.get_area())
# print()

# print('#__radius에 접근합니다.')
# print(circle.get_radius())
# print()

# circle.set_radius(2)
# print('# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.')
# print('둘레 : ',circle.get_circumference())
# print('원의 넓이:',circle.get_area())



# import math
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius #__ = 프라이빗 변수
#     def get_circumference(self):
#         return 2 * math.pi *self.__radius
#     def get_area(self):
#         return math.pi * (self.__radius **2)
    
#     @property
#     def radius(self):
#         return self.__radius
#     @radius.setter
#     def radius(self, value):
#         if value <= 0:
#             raise TypeError('길이는 양의 숫자여야 합니다.')
#             self.__radius = value

# print('# 데코레이터를 사용한 Getter와 Setter')
# circle = Circle(10)
# print('원래 원 반지름: ', circle.radius)
# circle.radius = 2
# print('변경된 원 반지름: ',circle.radius)
# print()

# print('# 강제로 예외 발생')
# circle.radius = -10



# class Parent:
#     def __init__(self):
#         self.value = '테스트'
#         print('Parent 클래스의 __init()__ 메소드가 호출되었습니다.')
#     def test(self):
#         print('Parent 클래스의 test() 메소드입니다.')

# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         print('Child 클래스의 __init()__ 메소드가 호출되었습니다.')

# child = Child()
# child.test()
# print(child.value)



##다중상속 (책에 없음)
# class Animal:
#     def __init__(self, species):
#         self.species = species
    
#     def move(self):
#         print('움직입니다.')

# class Fish:
#     def __init__(self, scale_color):
#         self.scale_color = scale_color
#     def swim(self):
#         print('수영합니다.')

# class Bird:
#     def __init__(self, feather_color):
#         self.feather_color = feather_color
    
#     def fly(self):
#         print('날아갑니다.')

# class FishBird(Animal, Fish, Bird):
#     def __init__(self, species, scale_color, feather_color):
#         Animal.__init__(self, species)
#         Fish.__init__(self, scale_color)
#         Bird.__init__(self, feather_color)


# fish_bird = FishBird('Fugu', 'Silver', 'Blue')
# print('종: ',fish_bird.species)
# print('비늘 색상: ', fish_bird.scale_color)
# print('털 색상', fish_bird.feather_color)


# fish_bird.move()
# fish_bird.swim()
# fish_bird.fly()



# class CustomException(Exception):
#     def __init__(self):
#         super().__init__()

# raise CustomException



# class CustomException(Exception):
#     def __init__(self):
#         super().__init__()
#         print('#### 내가 만든 오류가 생성되었어요! ####')
#     def __str__(self):
#         return '오류가 발생했어요!'
    
# raise CustomException



# class CustomException(Exception):
#     def __init__(self, message, value):
#         super().__init__()
#         self.message = message
#         self.value = value

#     def __str__(self): #재정의
#         return self.message
    
#     def print(self):
#         print('#### 오류 정보 ####')
#         print('메시지: ', self.message)
#         print('값:',self.value)
    
# try:
#     raise CustomException('딱히 이유없음', 273)
# except CustomException as e:
#     e.print()