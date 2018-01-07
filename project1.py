%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data="C:\data.xlsx"         #чтение файла
points=pd.read_excel(data, sheet_name=0, header=0, index_col=0)

def aver_predm(predm):          #функция, которая считает средний балл по отдельному предмету
    count=0
    aver=0
    for i in range (0,len(points)):
        if points.iloc[i][2]==predm:
            count=count+points.iloc[i][3]
            aver=aver+points.iloc[i][3]*points.iloc[i][4]
    return (aver/count)

predmety=["английский", "биология", "география", "информатика","испанский",         #список предметов, по которым будет проводиться анализ          
          "история", "литература", "математика", "немецкий", "обществознание",      #лишние предметы можно удалять
          "русский", "физика", "французский", "химия"]
ball=[0]*len(predmety)          #массив из нолей, кол-во элементов эквивалентно кол-ву предметов
for i in range(0,len(ball)):    #заполняем массив значениями, используя функцию
    ball[i]=aver_predm(predmety[i])
tabl=pd.Series(ball, index=predmety)        #создаем таблицу со значениями среднего балла и индексом предмет
data=pd.DataFrame({"Средний балл":tabl})    #даем индекс столбцу
print(data)                                 #вывод таблицы

loc_min=min(ball)                           #находим максимум и минимум, их индексы
ind_min=ball.index(loc_min)
loc_max=max(ball)
ind_max=ball.index(loc_max)

fig, ax=plt.subplots(figsize=(len(predmety),5))     #задаем размер графика   
plt.plot(predmety, ball)                            #задаем график со значениями XY
ax.set_xticklabels(predmety, rotation=60)           #задаем подписям абциссы поворот на 60 градусов
plt.title("Средний балл ГИА в Москве")
plt.ylabel("Значение")
plt.xlabel("Предмет")
ax.annotate('Локальный максимум', xy=(ind_max, loc_max),xytext=(ind_max+1, loc_max-0.3),     #стрелка с указанием локального максимума                
            arrowprops=dict(arrowstyle='->',facecolor='black'),   
            annotation_clip=False)
ax.annotate('Локальный минимум', xy=(ind_min, loc_min),xytext=(ind_min+1, loc_min+0.3),      #минимума              
            arrowprops=dict(arrowstyle='->',facecolor='black'),   
            annotation_clip=False)
plt.show()
