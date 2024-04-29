# print('%10s'%'cat','%10s'%'dog','%10s'%'turtle', sep = '\n')
# print('%10d'%3,'%10d'%127,'%10d'%54321, sep = '\n')
# print('%10.2f'%3.14,'%10.3f'%1.234,'%10.1f'%10.1 , sep = '\n')

# print('{:>10s}'.format('dog')) #{:s} 안에 >가 있으면 오른쪽으로 정령
#                                 # <가 있으면 왼쪽으로 정렬
# print(f'{'dog':>10s}')



# a = 'CarpeDiem!'
# print(a[-5:-1])#S1
# print(a[5:-1])#S2
# print(a[:5])


# print('Hello world'.count('l'))
# print('python'.find('p'))# = .index('p')

# print('oh','my','god', sep ='!')#S1
# print('oh!my!god'.split('!'))



# n = int(input('몇줄?> '))
# #다이아몬드 1)1~n까지 공백 + '*'찍기
# #2)역으로 재생
# for i in range(1,n+1): #1~n까지 순서대로
#     print(" "*(n-i)+"*"*(i*2-1)) #예를들어 4를 넣었을 때 4-1=3 공백, 1*(범위 내 반복)
# for j in range(n-1, 0, -1): #n-1~1까지 순서대로 감소하는 범위(예를들어 4넣었을 때 3~1 반복)
#     print(" "*(n-j)+"*"*(j*2-1)) #4-3=1 공백 + 3*2-1=5*
# print()

# #모래시계 다이아몬드 과정 1),2) 반대
# for j in range(n-1, 0, -1): #n-1~1까지 순서대로 감소하는 범위(예를들어 4넣었을 때 3~1 반복)
#     print(" "*(n-j)+"*"*(j*2-1)) #4-3=1 공백 + 3*2-1=5*
# for i in range(1,n+1): #1~n까지 순서대로
#     print(" "*(n-i)+"*"*(i*2-1))

# print('%3s'%'*')#노가다
# print('%4s'%'***')
# print('%5s'%'*****')
# print('%4s'%'***')
# print('%3s'%'*')



# x = 10
# print(not x)#파이썬에서는 정수 = True 이므로 not '정수'면 False 출력



# y = int(input('연도 > '))
# if (y % 4 ==0 and y % 100 != 0) or y%400 == 0:
#     print('윤년입니다.')
# else:
#     print('윤년이 아닙니다.')



# menu = "===== menu =====\n1. burger\n2. sandwitch\n3. Hotdog\n4. coke\n5. milk\n================"
# print(menu)
# n = input('1부터 5까지 입력해보세요~')
# if n == '1':
#     print('Burgers are not available.')
# elif n == '2'or n=='3':
#     print('What would you like to drink?')
# elif n == '4':
#     print('i like coke, too')
# elif n == '5':
#     print('Would you like got or cold?')



# import random #S1 내가 쓴 답 / 잘 작동함

# com = random.randint(1,3)
# me = int(input('1=가위 2=바위 3=보 > '))
# print('com{}:me{}'.format(com,me))

# if com==me:
#     print('Draw')
# elif com==1 and me==2:
#     print('Win')
# elif com==1 and me==3:
#     print('Lose')
# elif com==2 and me==3:
#     print('Win')
# elif com==2 and me==1:
#     print('Lose')
# elif com==3 and me==1:
#     print('Win')
# elif com==3 and me==2:
#     print('Lose')
# else:
#     print('1~3의 숫자만 입력하세요!')


# import random#S2 답

# com = random.randint(1,3)
# me = int(input('1=가위 2=바위 3=보 > '))

# lis = ['가위','바위','보']
# print('com({}):me({})',format(lis[com-1],lis[me-1])) #-1은 인덱스값 찾기위함

# if com == me:
#     print('Draw')
# elif com == 1:
#     if me ==2:
#         print('Win')
#     elif me ==3:
#         print('Lose')
# elif com == 2:
#     if me == 3:
#         print('Win')
#     elif me ==1:
#         print('Lose')
# elif com == 3:
#     if me == 1:
#         print('Win')
#     elif me== 2:
#         print('Lose')



# import random as r

# lis = ['월', '화', '수', '목', '금', '토', '일']

# i = r.randint(0,6)
# print(lis[i])



# a = ['fun', 'fun', 'python']
# s = ','.join(a) #문자열로 만들어주기
# print(s)
# print(s.split(',')) #구분해서 리스트로 만들어주기



# a = ['c', 'e', 'a', 'd', 'b']
# a.sort()#오름차 정렬
# print(a)
# a.pop()#리스트 맨 뒤 인덱스 제거
# print(a)


# 3 6 9게임
# n = 1
# while n <= 20:
#     if n%10 == 3 or n%10 == 6 or n%10 == 9:
#         print('X', end = ' ')
#     else:
#             print(n, end = ' ')
#     n += 1


# n = int(input('몇 줄? >'))
# for i in range(1,n+1):
#     print(' '*(n-i), '*'*(i*2-1)  , sep = '')

# n = int(input('반지름 >'))

# area = n**2*3.14
# print('반지름 {}의 원 넓이: '.format(n),area)



# def get_sum(n):###n번 입력, 입력받은 n개의 정수들의 합
#     sum = 0
#     for _ in range(n):
#         sum += int(input('>>'))
#     return sum

# n = int(input('몇번 입력? >'))
# print('sum : ', get_sum(n)) 



# n = int(input('몇번? >')) #n번 정수 입력받아 그 중 최댓값 구하기#S1

# def get_max(n):
#     a = []
#     for i in range(n):
#         b = int(input('>>'))
#         a.append(b)
#         #a.sort()#S2
#         #return lis[-1]
#     return max(a)
# print('max >',get_max(n))


# n = int(input('몇번? >')) #S3
# def get_max(n):
#     mx = 0
#     for _ in range(n):
#         a = int(input('>>'))
#         if mx < a:
#             mx = a
#     return mx 
# print(get_max(n))



# while True:
#     n = input('1 = 사각형, 2 = 삼각형, 3 = 원 (넓이) \n>')
#     def rec():#def rec(w,h)
#             #return w*h >>> print(rec(w,h)) <<< ex: (w,h) = (10,20)
#         a = int(input('사각형 가로(밑변) >'))
#         b = int(input('사각형의 세로(높이) >'))
#         print('{}*{} : '.format(a,b),a*b)
#     def tr():
#         c = int(input('삼각형 가로(밑변) >'))
#         d = int(input('삼각형의 세로(높이) >'))
#         print('{}*{}/2 : '.format(c,d),c*d/2)
#     def cir():
#         e = int(input('원의 반지름 >'))
#         print('{}**2*3.14 : '.format(e),e**2*3.14)

#     if n == '1':
#         rec()
#     elif n == '2':
#         tr()
#     elif n == '3':
#         cir()
#     elif n == 'N' or n== 'n':
#         break
#     else:
#         print('1,2,3 중에 입력해주세요.')



# id = input('아이디 >')#S1 (내가 쓴거, 뭔가 이상함)
# pw = input('비밀번호 >')

# def login(id,pw):
#     id='User'
#     pw='1234'

# def say():
#     print('아이디:{}\n비밀번호:{}'.format(id,pw))

# if id == 'User' and pw == '1234':
#     print('1,', 'Login Succes')
# elif id == 'User' and pw != '1234':
#     print('2,', 'Please check your pw')
# elif id != 'User' and pw == '1234':
#     print('3,', 'Please check your id')
# elif id != 'User' and pw != '1234': 
#     print('4,','Please check your id and pw')
# say()



# def login(id,pw):#S2 정답 ###
#     user_id='User'
#     user_pw='1234'
#     if user_id == id and user_pw == pw:
#         return 1
#     elif user_id == id and user_pw != pw:
#         return 2
#     elif user_id != id and user_pw == pw:
#         return 3
#     elif user_id != id and user_pw != pw:
#         return 4

# def say(result):#result = 매개변수
#     if result == 1:
#         return ('로그인 성공')
#     elif result == 2:
#         return ('아이디만 일치')
#     elif result == 3:
#         return ('비밀번호만 일치')
#     elif result == 4:
#         return ('모두 일치하지 않음')
# id = input('아이디 >')
# pw = input('비밀번호 >')

# print(say(login(id,pw)))#def login 값 -> say()에 넣고 출력


# with open('profile.txt','w') as f:#S1
#     f.write('Name : {}\nAge : {}\nSchool : {}'.format(
#         input('이름 >'),input('나이 >'),input('학교 >')))
    


# name = input('이름 >')
# age = input('나이 >')
# school = input('학교 >')

# file = open('profile.txt','w')
# file.write('name: {}\n'.format(name))#S2
# file.write('age: {}\n'.format(age))
# file.write('school: {}\n'.format(school))

# file.write(f'이름: {name}\nage: {age} \nschool: {school} ')#S3


# file = open('profile.txt','r')#S1
# line = file.readlines()
# print(line[2:3])

with open('profile.txt','r') as file:#S2 딕셔너리화 해서 키값 빼기
    dic = {}
    lines = file.readlines()
    # print(lines)

    for line in lines:
        data = line.split(':') # data = ['name':'이름'],#: 기준으로 리스트화
        key = data[0].strip()#공백제거
        value = data[1].strip()#공백제거
        dic[key] = value
    print(dic['School']) 