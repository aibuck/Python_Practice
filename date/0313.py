'''sum=0
for i in range(5):
    n = int(input('점수> '))
    sum += n
print('sum: %d' %sum)
print('avg: %.2f' % (sum/5))'''


'''
for i in range(3):
    for j in range(1,6):
        print(j, end = ' ')
    print()

for i in range(5):
    for j in range(5):
        print('*',end = '')
    print()'''


'''
for i in range(2,10):
    print('< %d 단 >' % i)
    for j in range(1, 10):
        print('%d * %d = %2d' % (i,j,i*j))
    print()'''



'''
#1부터 입력받은 정수까지의 수 중 3의 배수의 합
n= int(input('숫자를 입력하시면 3의 배수의 합이 나와요>'))
a = 0
for i in range(1,n+1):
    if i%3==0:
        a += i
print(a)

#양의 정수를 입력받아 입력받은 정수의 각 자리 숫자의 합
m = input('숫자를 입력하시면 각 자리 숫자 합이 나옵니다')
b = 0
for l in m:
    b += int(l)
print(b)sss'''



'''
#정수 n개를  2번 입력받아 짝이 되는 n개 정수의 합 !중요
lis=[]
for _ in range(2): 
    a = input().split()
    sum=0
    for i in range(len(a)):
        sum += int(a[i])
    print(sum)
    lis.append(sum)
for i in lis:
    print(i, end=' ')
# [13, 24, 35, 57, 79]
# [4, 6, 8, 12, 16]ssss'''


'''
#정수 10개를 입력받아 그중 가장 큰 수를 출력하는 프로그램
l = [] #1번, 내가한 방법
for _ in range(10):
    a = input('숫자 입력> ')
    l.append(a)
print('큰 수는>',int(max(l)))


a = input().split() #2번 답안
mx = 0
for i in range(len(a)):
    if mx < int(a[i]):
        mx = int(a[i])
print(mx)sss'''


'''
#정수 n을 입력 받아 n단의 왼쪽 직각 이등변 삼각형을 그리기
n = int(input('몇단?>'))#S1
for i in range(n):
    print('*'*(i+1))

n = int(input('몇단?>'))#S2
for i in range(n):
    for j in range(i+1):
        print('*', end = '')
    print()
'''


'''
#정수 n을 입력 받아 n단의 오른쪽 직각 이등변 삼각형을 그리기
n = int(input('몇단?>')) #S1
for i in range(n):
    print(" " * (n - (i+1)), end="")
    print('*'*(i+1))

n = int(input('몇단?>'))#오답
for i in range(n):
    print(' '*(n-(i+1)),end = '')
    for a in i:
        print('*'*(a+1))

n = int(input('몇단?>'))#S2
for i in range(n):
        print(' ', end = '')
    for j in range(i+1):
        print('*', end = '')
    print()?'''


'''
try:
    n= int(input('정수 입력> '))
    print('원의 반지름:', n)
    print('원의 둘레:',2*3.14*n)
    print('원의 넓이', 3.14*n*n)
except:
    print('무언가 잘못되었습니다.')
else:
    print('예외가 발생하지 않았습니다.')
finally:
    print('프로그램을 종료합니다.')



# la= ['52', '273', '32', '스파이', '103']
# ln= []
# for i in la:
#     try:
#         float(i)
#         ln.append(i)
#     except:
#         pass

# print('{}내부에 있는 숫자는'.format(la))
# print('{}입니다.'.format(ln))
'''


'''
try:
    file = open('info.txt','w')
    예외.발생해라

except Exception as e:
    print(e)

file.close()
print('#파일이 제대로 닫혔는지 확인하기')
print('file.closed:', file.closed)
'''

'''
def test():
    print('test() 함수의 첫줄.')
    try:
        print('try 구문이 실행')
        return#return 이후의 값은 출력(실행)하지 않음
        print('try 구문의 return 키워드 뒤')
    except:
        print('except 구문이 실행')
    else:
        print('else 구문이 실행')
    finally:
        print('finally 구문이 실행')
    print('test() 함수의 마지막줄')
test()'''

'''
print('프로그램이 시작되었습니다.')
while True:
    try:
        print('try 실행')
        break#반복문 멈추기
        print('try 구문 break키워드 뒤')
    except:
        print('except 실행')
    finally:
        print('finally 실행')
    print('while 반복문의 마지막 줄입니다.')
print('프로그램 종료')
'''

'''
n= [52,273,32,103,90,10,275]

print('# (1) 요소 내부에 있는 값 찾기')
print('- {}는 {} 위치에 있습니다.\n'.format(52,n.index(52)))

print('# (2) 요소 내부에 있는 값 찾기')
na = 10000
try:#if:
    print(' {}는 {}위치에 있습니다.'.format(na,n.index(na)))
except:#else: / if: else: 구문으로도 사용가능
    print('- 리스트 내부에 없는 값입니다.\n')
print('---정상적으로 종료되었습니다---')
'''

'''
try:
    n= int(input('정수 입력> '))
    print('원의 반지름:', n)
    print('원의 둘레:',2*3.14*n)
    print('원의 넓이', 3.14*n*n)
except Exception as exception:
    print('type(exception):',type(exception))
    print('exception:', exception)
'''


'''
a= [52,273,32,72,100]

try:
    n=int(input('점수 입력> ')) 
    print('{}번째 요소: {}'.format(n, a[n]))
except ValueError as Exception:
    print('정수를 입력해 주세요!')
    print('Exception:',Exception)
except IndexError as Exception:
    print('리스트의 인덱스를 벗어났어요!')
    print('Exception',Exception)'''##


'''
import math
print(math.sin(1))
print(math.cos(1)
      )
print(math.tan(1))
print(math.floor(2.5))
print(math.ceil(2.5))

import math as m
'''


'''
import random as r
print('#random 모듈')

print('- random():', r.random())
print('- uniform(10,20):', r.uniform(10,20))
print('- randrange(10)', r.randrange(10))
print('- choice[1,2,3,4,5]',r.choice([1,2,3,4,5]))
print('- suffle[1,2,3,4,5]', r.shuffle([1,2,3,4,5]))
print('- sample([1,2,3,4,5],k=2)',r.sample([1,2,3,4,5], k=2))
'''

'''
import os
print('현재 운영체제:',os.name)
print('현재 폴더:', os.getcwd())
print('현재 폴더 내부의 요소:', os.listdir())

os.mkdir('hello')
os.rmdir('hello')

with open('original.txt','w') as file:
    file.write('hello')
os.rename('original.txt', 'new.txt')

os.remove('new.txt')

os.system('dir')'''


'''
import datetime as d
n = d.datetime.now()
print('시간 더하기')
after = n +d.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1,)#\= 가독성을 위해 한줄임을 표시
print(after.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초'))
print()

print('1년 더하기')
o = n.replace(year=(n.year +1))
print(o.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초'))

'''##


'''
import time
print('지금부터 5초 동안 정지합니다!')
time.sleep(5)
print('프로그램 종료')
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '<hi>Hello World!</h1>'