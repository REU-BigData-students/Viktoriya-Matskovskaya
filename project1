%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data="C:\data.xlsx"
points=pd.read_excel(data, sheet_name=0, header=0, index_col=0)

def aver_predm(predm):
    count=0
    aver=0
    for i in range (0,len(points)):
        if points.iloc[i][2]==predm:
            count=count+points.iloc[i][3]
            aver=aver+points.iloc[i][3]*points.iloc[i][4]
    return (aver/count)

predmety=["английский", "биология", "география", "информатика","испанский", 
          "история", "литература", "математика", "немецкий", "обществознание", 
          "русский", "физика", "французский", "химия"]
ball=[0]*len(predmety)
for i in range(0,len(ball)):
    ball[i]=aver_predm(predmety[i])
tabl=pd.Series(ball, index=predmety)
data=pd.DataFrame({"Средний балл":tabl})
print(data)

loc_min=min(ball)
ind_min=ball.index(loc_min)
loc_max=max(ball)
ind_max=ball.index(loc_max)

fig, ax=plt.subplots(figsize=(14,5))
plt.plot(predmety, ball)
ax.set_xticklabels(predmety, rotation=60)
plt.title("Средний балл ГИА в Москве")
plt.ylabel("Значение")
plt.xlabel("Предмет")
ax.annotate('Локальный максимум', xy=(ind_max, loc_max),xytext=(ind_max+1, loc_max-0.3),                     
            arrowprops=dict(arrowstyle='->',facecolor='black'),   
            annotation_clip=False)
ax.annotate('Локальный минимум', xy=(ind_min, loc_min),xytext=(ind_min+1, loc_min+0.3),                    
            arrowprops=dict(arrowstyle='->',facecolor='black'),   
            annotation_clip=False)
plt.show()
