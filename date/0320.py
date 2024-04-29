import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t = pd.read_csv('./titanic.csv')
c = pd.read_csv('./countries.csv')
c1 = pd.read_csv('./countries1.csv')

# c['density'] = c['population']/c['area']
# print(c)



# df = pd.DataFrame({'code' : ['CA'], 'country': ['Canada'],\
#                    'area': [9984670], 'capital': ['Ottawa'],\
#                     'population': [34300000]})

# df2 = pd.concat([c,df], ignore_index = True)

# print(df2)



# c.drop(index=2, axis = 0, inplace = True)#인덱스위치, 
# print(c)

# df3 = df2.drop(index=2, axis = 0, inplace = False)
##inplace = True < 원본에서 제거,
## " = False < 지운값을 반환 (df3과 같은 객체변수 선언해줘야함)
## axis = 0 < 행 , " = 1 < 열
# print(df3)


# c.drop(['capital'],axis=1, inplace=True)
# print(c)



# print(t[['Age','Sex']].groupby('Sex').mean()) #.groupby < 그룹별로 분할

# df = pd.DataFrame(t[['Sex','Age']].groupby('Sex').mean())
# print(df)



# print(t.groupby(['Sex','Pclass'])['Fare'].mean())

# print(t['Pclass'].value_counts())



# df = pd.DataFrame({
#     'name':['Kim','Lee','Park', 'Choi', 'Hong', 'Chung', 'Jang'],
#     'age':[22, 26, 78, 17, 46, 32 , 21],
#     'city': ['Seoul','Busan','Seoul','Busan','Seoul','Daejun','Daejun'],
#     'children': [2,3,0,1,3,4,3],
#     'pets':[0,1,0,2,2,0,3]
# })

# df.plot(kind='line', x='name', y= 'pets', color='red')
# plt.show()


# ax = plt.gca()
# df.plot(kind='line', x='name', y='children', ax = ax)
# df.plot(kind='line',x='name',y='pets', color='red', ax=ax)
# plt.show()


# df.groupby('city')['name'].nunique().plot(kind='bar')
# plt.show()


# df[['age']].plot(kind='hist', bins=[0,20,40,60,80,100],rwidth = 0.8)
# plt.show()



# t.drop(['PassengerId','Ticket','Name'], inplace= True, axis=1)
# print(t.head())



# table = pd.pivot_table(data = t , index=['Sex'], aggfunc="sum")
# table.plot(kind='bar')
# plt.show()



# table = pd.pivot_table(t, index= ['Sex','Pclass'],\
#                         aggfunc={'Age':np.mean,'Survived':np.sum})

# print(table)



# table = pd.pivot_table(t, index=['Sex'],\
#                        columns=['Pclass'],values=['Survived'],\
#                        aggfunc=np.sum)
# print(table)
# table.plot(kind='bar')
# plt.show()



# df1 = pd.DataFrame({'employee': ['Kim','Lee','Park','Choi'],
#                     'department':['Accoungting','Engineering','HR','Engineering']})

# df2 = pd.DataFrame({'employee':['Kim','Lee','Park','Choi'],
#                     'age':[27,34,26,29]})

# df3 = pd.merge(df1,df2)#같은 인덱스, 열이 있을때 출력, 없으면 출력X
# print(df3)



# print(c1.info())
# print(c1.dropna(how = 'all'))
##.dropna(how = 'all')< 모든 값이 NAN인 행 지우기
##.dropna()< NAN 값이 있는 행 지우기



# t1_0 = c1.fillna(0)
# print(t1_0)
# print(t1_0.info())



c1.fillna(c1.mean()['area'])
print(c1)