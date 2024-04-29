"""def print_n_times(v,n):
    for i in range(n):
        print(v)
print_n_times("안녕하세요", 5)"""



"""def print_n_times(n,*v):
    for i in range(n):
        for val in v:
            print(val)
        print()

print_n_times(3,'안녕하세요','즐거운','파이썬 프로그래밍')"""



"""def print_n_times(v,n=2):
    for i in range(n):
        print(v)
print_n_times("안녕하세요",3)"""

"""def a(*v,n=2):
    for i in range(n):
        for val in v:
            print(val)
        print()
a("안녕",'즐거운','파이썬',n=3)"""

"""def re():
    print('A 위치입니다.')
    return
    print('B 위치입니다.')

re()"""

"""def re():
    return 100
v=re()
print(v)"""

"""def su(s,e):
    o=0
    for i in range(s,e+1):
        o+=i
    return o

print("0 to 100:", su(0,100))
print("0 to 1000:", su(0,1000))
print("50 to 100:", su(50,100))
print("500 to 1000:", su(500,1000))"""



"""def f(x):
    return x
print(f(10))

def f(x):
    return 2*x+1
print(f(10))

def f(x):
    return (x+1)**2
print(f(10))"""



"""def mul(*v):
    o=1
    for i in v:
        o*=i
    return o
print(mul(5,7,9,10))"""


"""def f(n):
    o = 1
    for i in range(1, n+1):
        o *= i
    return o
print("1!:",f(1))
print("2!:",f(2))
print("3!:", f(3))
print("4!:", f(4))
print("5!:", f(5))
print("6!:", f(6))#팩토리얼 함수"""

"""def f(n):#재귀함수
    if n == 0:
        return 1
    else:
        return n * f(n-1)
print('1!:', f(1))
print('2!:', f(2))
print('3!:', f(3))
print('4!:', f(4))
print('5!:', f(5))"""

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return f(n-1) - f(n-2)
    
print("f(1):", f(1))
print("f(2):", f(2))
print("f(3):", f(3))
print("f(4):", f(4))
print("f(5):", f(5))