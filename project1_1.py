import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import tkinter as tk
import patoolib
import os
import json
from urllib import request


url='https://op.mos.ru/EHDWSREST/catalog/export/get?id=7080'
file_name='results.zip'
folder_name='unpack'
request.urlretrieve(url,file_name)

patoolib.extract_archive(file_name,outdir=folder_name)
file=os.listdir(folder_name)

os.chdir(folder_name)


myfile=open(file[0], mode="r")
data=json.load(myfile)


def aver_point(subject):
    count=0
    aver=0
    for i in range (0,len(data)):
        if data[i]["SubjectName"]==subject:
            count=count+data[i]["PassedQuantity"]
            aver=aver+data[i]["PassedQuantity"]*data[i]["AVGScore"]
    return ([aver/count,count])
myfile.close()

subjects=["английский", "биология", "география", "информатика","испанский", 
          "история", "литература", "математика", "немецкий", "обществознание", 
          "русский", "физика", "французский", "химия"]


root=tk.Tk()
root.title("Выберите предметы")
root.geometry("300x450+300+250")

var=[0]*len(subjects)
for i in range(0,len(subjects)):
    var[i]=tk.BooleanVar()
    check=tk.Checkbutton(root,text=subjects[i],variable=var[i],onvalue=1,offvalue=0,padx=20,pady=3)
    check.grid(row=i, column=0, sticky='w')
     
root.mainloop()

subject=[]
points=[]
num=[]
mark=[]

for i in range(0,len(subjects)):
     if var[i].get()==True:
        subject.append(subjects[i])
        
for i in range(0,len(subject)):
    points.append(aver_point(subject[i]))
myfile.close()

for i in range(0,len(subject)):
    num.append(points[i][1])
    mark.append(points[i][0])

data_new=pd.DataFrame({"Средний балл":mark, "Число сдававших":num}, index=subject)
print(data_new)


loc_min=min(mark)
ind_min=mark.index(loc_min)
loc_max=max(mark)
ind_max=mark.index(loc_max)

fig, ax=plt.subplots(figsize=(len(subject),5))
plt.plot(subject, mark)
ax.set_xticklabels(subject, rotation=60)
plt.title("Средний балл ГИА в Москве")
plt.ylabel("Значение")
plt.xlabel("Предмет")
ax.annotate('Локальный максимум', xy=(ind_max, loc_max),xytext=(ind_max, loc_max-0.2),                     
            arrowprops=dict(arrowstyle='->',facecolor='black'),   
            annotation_clip=False)
ax.annotate('Локальный минимум', xy=(ind_min, loc_min),xytext=(ind_min, loc_min+0.2),                    
            arrowprops=dict(arrowstyle='->',facecolor='black'),   
            annotation_clip=False)
plt.show()
os.chdir(curent_dir)
