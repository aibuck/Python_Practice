# import matplotlib.pyplot as plt # pip install matplotlib
# plt.plot([15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4])
# plt.show()


# X = [1,2,3,4,5,6,7]
# X = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]

# plt.plot(X,Y)
# plt.xlabel('day')
# plt.ylabel('temperature')
# plt.show()


# X = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
# Y2 = [20.1, 23.1, 23.8, 25.9, 23.4, 25.1, 26.3]

# plt.plot(X, Y1, label= 'Seoul')
# plt.plot(X, Y2, label= 'Busan')
# plt.xlabel('day')
# plt.ylabel('temperature')
# plt.legend(loc='best')#범례
# plt.title('Temperatures of Cities')
# plt.show()



# plt.plot([15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4], '^m--')
# plt.show()

# X = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
# Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
# plt.bar(X,Y)
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# #3차원 축 얻기.
# axis = plt.axes(projection='3d')

# #3차원 데이터를 넘파이 배열로 생성
# Z = np.linspace(0,1,100)
# X = Z*np.sin(30*Z)
# Y = Z*np.cos(30*Z)

# #3차원 그래프 그리기
# axis.plot3D(X,Y,Z)
# plt.show()



# import numpy as np
# fternp = [63, 73, 80, 86, 84, 78, 66, 54, 45, 63]

# F = np.array(fternp)
# print((F-32)*5/9)
# 
# import matplotlib.pyplot as plt
# plt.plot(F)
# plt.show()


# import numpy as np
# A = np.array([1,2,3,4])
# B = np.array([5,6,7,8])

# result = A*B
# print(result)



# a = np.array([0,9,21,3])
# print(a<10)



# b= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b[0][2])



#BMI 계산
# import numpy as np
# heights = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
# weights = np.array([86, 77, 59, 95, 80, 68])
# bmi= weights/heights**2

# print(bmi)



# import numpy as np
# a = np.arange(1, 10, 2)

# import matplotlib.pyplot as plt
# plt.figure(figsize=(3,2))
# plt.plot(a,'*')
# plt.show()


# import numpy as np
# a = np.linspace(0, 10, 100)#0부터 10까지 100개의 숫자 만들기

# import matplotlib.pyplot as plt
# plt.plot(a,'.')
# plt.show()



# import numpy as np
# np.random.seed(100)#시드가 생성되면 0~1안에서 난수를 만드는 함수
# print(np.random.rand(5))
# print(np.random.rand(5,3))



# import numpy as np
# print(np.random.randn(5))#randn = 정규분포
# print(np.random.randn(5,4))#4개씩 5번

# m, sigma = 10, 2
# print(m+sigma*np.random.randn(5))


# import numpy as np
# import matplotlib.pyplot as plt

# pure = np.linspace(1,10,100)
# noise = np.random.normal(0,1,100)#평균 0 , 표준편차 1 인 100개의 난수생성

# signal = pure + noise

# plt.plot(signal)
# plt.show()



# import numpy as np
# s = np.array([[99,93,60],[98,82,93],[93,65,81],[78,82,81]])

# print(s.sum())
# print(s.min())
# print(s.max())
# print(s.mean(axis=0))
# print(s.std())#표준편차 구하는 함수
# print(s.var())#분산 구하는 함수
# print(a.shape)



# import numpy as np
# import matplotlib.pyplot as plt

# n = np.random.normal(size=10000)

# plt.hist(n)#히스토그램
# plt.xlabel('value')
# plt.ylabel('freq')
# plt.show()



# import numpy as np###중요
# import matplotlib.pyplot as plt
# np.random.seed(10)
# m, sigma = 10, 0.8
# a = m+sigma*np.random.randn(1000)
# b = np.random.randn(1000)


# plt.hist(a, label='a')
# plt.hist(b, label='b')
# plt.legend(loc = 'best')
# plt.show()



#-2*np.pi ~2*np.pi 까지 100개
# import numpy as np
# import matplotlib.pyplot as plt

# a = np.linspace(-2*np.pi,2*np.pi,100)
# b = np.sin(a)
# c = b*2
# plt.plot(a,b,a,c)#= plt.plot(b) \n plt.plot(c) < a값이 정해져있어서 출력됨
# plt.show()


# import numpy as np

# ypred = np.array([1,0,0,0,0])
# y = np.array([0,1,0,0,0])

# n=5


# m = np.square(ypred-y)#S1
# s = sum(m)
# mse = (1/n)*s


# mse= 1/n * sum(np.square(ypred-y))#S2
# print(mse)



# ypred = [1,0,0,0,0]#S3
# y = [0,1,0,0,0]

# n = 5
# r = 0

# for i in range(len(ypred)):
#     r += (ypred[i]-y[i])**2

# mse = 1/n*r
# print(mse)


import numpy as np

# g = np.array([88,72,93,94])

# print(g[:3])


# ages = np.array([18,19,25,30,28])

# y = ages > 20
# print(ages[ages > 20])


# a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(a[0:2, 1:3])



import matplotlib.pyplot as plt

# a = np.linspace(0,10,100)
# b = a**2
# c = a
# d = a * 0 + 1 # d = np.full(100,1) , d = np.ones(100) // 모두 같은 방법

# plt.plot(a,b,a,c,a,d)
# plt.show()



# x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x.T)#전치행렬 구하기, == print(x.transpose())



# a = np.array([[3,1],[1,2]])
# b = np.array([9,8])
# x = np.linalg.solve(a,b)#a=b 일때 방정식을 만족하는 해
# print(x)



import pandas as pd

# t = pd.read_csv('./titanic.csv')#./ >> 현재 터미널 위치
# t = pd.read_csv('./titanic.csv', index_col=0)

# print(t.head(2)) #처음부터 데이터 2개, 마지막 부터는 .tail()

# print(t.describe())

# print(t.dtypes) #object : 문자열, 타입확인

# b_20 = t[t['Age']<20]
# print(b_20.head(3))

# print(t[t['Pclass'].isin([1,2])])

# print(t.loc[t['Age']<20, ['Name','Age']])

# print(t.iloc[20:23, 5:7])#t.iloc[a,b] // a = 행, b = 열

# print(t.sort_values(by='Age').head(30))
# print(t.sort_values(by=['Pclass','Age'],ascending = False).head())
##ascending = True면 오름차순, False = 내림차순


# data = ['Kim','Park','Lee',"Choi"]
# ser = pd.Series(data)#인덱스 값을
# print(ser)



# data = {'name':['Kim','Park','Lee','Choi'],\
#         'Age':[20,23,21,26]}
# df = pd.DataFrame(data)
# # print(df)
# df = pd.DataFrame(data, index=['학번 1','학번 2','학번 3','학번 4'])
# print(df)



# df = pd.DataFrame(np.random.randint(0,100,size=(5,4)),columns=list('ABCD'))
# print(df)



# c = pd.read_csv('./countries.csv')
# print(c[['code','country','capital']])#대괄호 두개-> 여러 항목 불러오기