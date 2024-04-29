"""c = 0

def f(n):
    print("f({})를 구합니다.".format(n))
    global c #함수 안에 있으므로 전역변수 선언
    c += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)
    
f(10)
print('---')
print('f(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.'.format(c))sss"""

"""dic={
    1:1,
    2:1
}

def fib(n):
    if n in dic:
        return dic[n]
    else:
        o = fib(n-1) + fib(n-2)
        dic[n] = o
        return o
    
print(fib(10))
print(fib(20))
print(fib(30))
print(fib(40))
print(fib(50))sss"""



'''def fl(d):
    o= []
    for i in d:
        if type(i) == list: 
            o += fl(i)
        else: #정수가 여기로 들어감
            o.append(i)
    return o


ex= [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본",ex)
print("변환:", fl(ex))ssss'''

'''[a,b]=[10,20]#튜플
[c,d]=(10,20)

print(a)
print(b)
print(c)
print(d)'''



'''tu= 10, 20, 30 ,40 #튜플 괄호없이
print(tu)
print(type(tu))

a,b,c = 10,20,30

print(a)
print(b)
print(c)'''


'''a,b=10,20 #괄호 없는 튜플 활용
print(a)
print(b)

a,b = b,a
print(a)
print(b)'''



'''def t():
    return(10, 20)
a,b = t()

print(a)
print(b)'''

'''def c(f):
    for i in range(10):
        f()

def print_hi():
    print('안녕하세요')

c(print_hi)#함수(함수)출력'''


'''
def p(i):
    return i*i
def u(i):
    return i<3

la=[1,2,3,4,5]

oa= map(p, la)
print(oa)#map object at 0x00000208CF189D50
print(list(oa))

ob=filter(u,la)
print(ob)#filter object at 0x00000208CF189EA0
print(list(ob))

p = lambda x: x*x
u = lambda x: x <3

print(oa)#<filter object at 0x00000208CF189EA0>
print(list(oa))
print(ob)#filter object at 0x000002110675A0B0
print(list(ob)) #map,filter,lambda 조금'''


'''la= [1,2,3,4,5]

oa= map(lambda x: x*x, la)
print(oa)#<map object at 0x0000018C599F9E10>
print(list(oa))

ob= filter(lambda x: x<3, la)
print(ob)#<filter object at 0x0000018C599FA170>
print(list(ob))#lambda 함수식'''

'''
a = lambda x,y: x*y#S1

def a(x,y):
    return x*y#S2 둘다 같은 방법임'''
'''
l1= [1,2,3,4,5]
l2= [2,3,4,5,6]

a= lambda x,y: x*y
r= map(a, l1, l2)
print(list(r))'''


'''
file = open('C:\\Users\\202-4\\Desktop\\basic.txt', 'w')
file.write("Hello Python")

file.close()'''#파일 사용법, close()꼭 써주기

'''with open('C:\\Users\\202-4\\Desktop\\basic.txt','w') as file:
    file.write("Hello Python Program!!")'''

'''with open('C:\\Users\\202-4\\Desktop\\basic.txt','r') as file:
    contents = file.read()
print(contents)'''



'''
import random

ha = list('가나다라마바사아자차카타파하')

with open('C:\\Users\\202-4\\Desktop\\info.txt','w') as file:
    for i in range(1000):
        name = random.choice(ha) + random.choice(ha)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write('{},{},{}\n'.format(name, weight, height))



with open('C:\\Users\\202-4\\Desktop\\info.txt','r') as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")
        
        if (not name) or (not weight) or (not height):
            continue
        bmi = int(weight)/((int(height)/100)**2)
        re = ""
        if 25 <= bmi:
            re = '과체중'
        elif 18.5 <= bmi:
            re = '정상체중'
        else:
            re = '저체중'
        
        print('\n'.join([
            '이름: {}'
            '몸무게: {}'
            '키: {}'
            'BMI: {}'
            '결과: {}'
        ]).format(name, weight, height, bmi, re))
        print() ??'''



'''
my_list= [1,2,3,4,5]#이터레이터 > 리스트 요소 하나씩 뽑기
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

for i in my_list:#위와 같은 결과//모두 뽑음
    print(i)'''



'''
def test():
    print('함수호출')#yield가 들어가면 제너레이터 함수이므로 출력X
    yield 'test'

print('A pass')
test()

print('B pass')
test()
print(test())#sss'''


'''
def test():
    print('A pass')
    yield 1
    print('B pass')
    yield 2
    print('C pass')

o= test()
print('D pass')
a= next(o)
print(a)
print('E pass')
b= next(o)
print(b)
print('F pass')
c=next(o)
print(c)
next(o)#sss'''


'''
n= [1,2,3,4,5,6]

print('::'.join(str(n)))
print('::'.join(map(str,n)))'''



'''n = list(range(1, 10+1)) # [1,2,3,4,5,6,7,8,9,10]
a = lambda x: x*x #매개변수, 뒤 return값

print(list(filter(lambda x: x % 2 == 1 , n)))#홀수만  출력하기

print(list(filter(lambda x: 3<=x<7 , n)))#3이상, 7미만 출력하기

print(list(filter(lambda x: x*x<50 , n)))#제곱해서 50미만 추출하기
'''

#for 변수 in list,dict,range: 중요!!!
    #수행할 문장1
    #수행할 문장2


'''n = [1,2,3,4,5]
s = 0
for nl in n:
    s += nl
print('avg:%d' % (sum//len(n)))'''




'''al=[1,2,3]
bl=[10, 100, 1000]
for a in al: #줄을 의미
    for b in bl:
        print(a*b, end = ' ')
    print()'''


'''
#1부터 입력받은 정수까지 차례로
i = int(input('숫자 입력'))
for a in range(1,i+1):
    print(a, end = ' ')#end는 키워드 매개변수 / 입력하지 않으면 기본 end=\n

#1부터 100까지 짝수만 출력
i2 = range(1,100+1)#range()에서는 : (슬라이싱) 사용하지않음
for b in i2:
    if b%2==0:
        print(b,end = ' ')

i=2
while (i<=100) and (i%2==0):
    print(i,end=' ')
    i += 2

i=1
while i<=50:
    print(i*2, end = " ")
    i+=1'''


'''
#문자를 입력받고 입력받은 문자를 5번 출력
a= input('문자 입력')
for b in range(5):
    print(a, end = ' ')



#입력받은 정수부터 50까지 출력
b = int(input('숫자 입력'))
for i in range(b,50+1):
    print(i,end = ' ')'''


sum = 0
a= {}
for i in range(5):
    name=input('이름 입력')
    score=int(input('점수 입력'))
    a[name]=score
    print(sum({score}))
#집에서 하기 딕셔너리 활용해서 밸류값 더하기

'''
sum = 0
for _ in range(5):
   h = int(input('입력: '))
   sum += h

print(sum)
print(sum/5)
'''