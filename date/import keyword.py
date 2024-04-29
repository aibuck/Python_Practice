"""a= [103, 52, 273 ,32, 77]
print(min(a))
print(max(a))
print(sum(a))sss"""



"""a= [1,2,3,4,5]
ra= reversed(a)

print(ra)

for i in ra:
    print("-", i)sss"""



"""a= ["요소A",'요소B','요소C']
i=0
for item in a:
    print("{}번째 요소는 {}입니다.".format (i,a[i])


print(a)
print(enumerate(a))
print(list(enumerate(a)))

for i,v in enumerate(a):
    print("{}번째 요소는{}입니다.".format(i,v))sss"""



"""a= {
    'kA':'pA',
    'kB':'pB',
    'kC':'pC',
}

print(a.items())

for key,el, in a.items():
    print("키와 대응하는 값입니다.{}={}".format(key,el))sss"""

"""a=[]
for i in range(0,20,2):
    a.append(i*i)
print(a)"""

"""a=[i*i for i in range(0,20,2)]

print(a)sss"""



"""a= ['사과','자두','초콜릿','바나나','체리']
o= [f for f in a if f !='초콜릿']

print(o)sss"""

"""print("{:b}".format(10))#2진수 변환
print(int("1010",2))#2진수->10진수
print("{:o}".format(10))#8진수 변환
print("{:x}".format(10))#16진수 변환
print("안녕안녕하세요".count("안"))#안에 .count()문자열 몇개 들어있냐"""

"""o = ({:b},range(1,100+1))
o= [num for num in range(1,100+1)]
    if a.count(0)==1:
    for i in a:
        print("{}:{}".format(i,"{:b}".format(i)))
print("합계", sum(o))오답"""

"""o= [num for num in range(1,100+1) if "{:b}".format (num).count('0')==1]
for i in o:
    print("{}:{}".format(i,"{:b}".format(i)))
print("합계", sum(o))정답sss"""


###마무리 정리
"""print("apple",'juice',sep='~')
print('appple','juice', end= ' is ')#(end = )줄바꿈이랑 대체
print('tasty')

print('%d와 %d는 정수이다.'%(7,8))#여러 값을 넣을땐 괄호필수
print('%.3f는 실수이다.'%1.2345)


x,y= 10,'code'
print(f"x is {x}")
print(f"y is {y}")
print(f"x is {x} and y is {y}")"""

"""a={
    '경기종목':'축구',
    '학년':'2',
    '이긴 반':'3',
    '진 반':'5',
}
print("오늘 파이썬 초등학교에서 {}경기가 열렸습니다.2학년 {}반과 {}반이 치열한 경기를 펼쳤고{}반이 승리했습니다".format(a{0},a{1},a{2},a{3}))오답"""

"""p = input('경기종목: ')
g = input('학년: ')
w = input('이긴 반: ')
l = input('진 반: ')

print('오늘 파이썬 초등학교에서 %s 경기가 열렸습니다. ' %p)
print('%s 학년 %s반과 %s반이 치열한 경기를 펼쳤고' %(g,w,l))
print("%s 반이 승리하였습니다" %w)
print("")

print(f"오늘 파이썬 초등학교에서 (p) 경기가 열렸습니다.")
print(f"(g)학년 (w)반과 (l)반이 치열한 경기를 펼쳤고")
print("")정답sss"""

"""import datetime
a = {
    '연도':'datetime.datetime.year',
    '월':'datetime.datetime.month',
    '일':'datetime.datetime.day',
}
for i in a:
    print("오늘은 {}년 {}월 {}일 입니다.".format (i{0},i{1},i{2}))오답"""

"""y = input("연도 ")
m = input("월: ")
d = input('일: ')

print(f'오늘은 {y}년 {m}월 {d}일 입니다.')
print('오늘은 %d년 %020d월 %020d월 입니다.'%(y,int(m),int(d)))sss"""


"""n= [1,1,1,4,3,5,5,6,6,6,7,8,9,9,9]
a= []

for b in n:
    if b not in a:
        a.append(b)

print(a)


arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]

result1 = dict.fromkeys(arr) # 리스트 값들을 key 로 변경
print(result1)

result2 = list(result1) # list(dict.fromkeys(arr))
print(result2)sss"""


"""l1=set[1,2,3,4,5]
l2=set[3,4,5,6,7]
r=[]

print(l1&l2)


for  in l1,l2:
    if list() in r:
        print(r)
google"""


"""l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
r= []

for i in l1:
    if i in l2:
        r.append(i)

print(r)sss"""

"""o = {} #주문을 저장할 딕셔너리
while True:
    f= input('주문할 음식을 입력하세요(종료하려면 q를 입력)')
    if f.lower()=='q':
        break
    s= int(input('주문할 수량을 입력하세요 >>'))
    if f in o:#더해주는 부분
        o[f] += s
    else:
        o[f] = s
print("주문내역: ")
for a,b in o.items():
    print(a,b) SSSS"""


"""s= {}
while True:
    n=input('이름을 입력하세요> ')
    if n.lower()=='q':
        break
    print(n, end="")
    r=float(input(('의 성적을 입력하세요.>> ')))
    s[n] = r
#추가부분
avg = sum(s.values()/ len(s))
max_s= max(s.values)

print("성적 결과")
print(f"평균 성적: {avg}")
print(f"최고 성적: {max_s}")"""


"""n = input()

for i in range(1,9+1):
    print(n*1, end=' ')

i= 1
while i<10:
    print(n*1, end= ' ')
    i += 1sss"""

"""a=50

while True:
    b=int(input('정답?'))    
    if b==a:
        print('ok')
        break
    elif b<1 or b>100:
        print("1부터 100까지의 숫자입니다.")
    elif a<b:
        print("down")
    elif a>b:
        print("up")
    """

"""a='*'
for i in a:
    print(i*10, end='\n')
for i in range(10):
    print('*')"""


"""for i in a:
    i+=1
    print(i*10)오답

for i in range(10):
    print('*'*i)정답"""

"""for i in range(1,10):
    for j in range(i):
            print('*', end=' ')
    """

"""for i in range(1,10):
    for b in range(i+1):
        i=int(i)
        print(a,'X',i = a*i)구구단오답"""

"""for x in range(2,10): 
    for y in range(1,10):
        print(x, 'X', y, '=', x * y)
        if(y == 9):
            print('----------')구구단정답
            #print(f'{x} X {y} = {x*y}')"""



