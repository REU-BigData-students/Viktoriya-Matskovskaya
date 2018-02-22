import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import tkinter as tk
import patoolib
import os
import json
from urllib import request



def func1(url1) :
#getting curent directory
    curent_dir=os.getcwd()                                      
    file_name='results.zip'
    folder_name='unpack'
#download archived file from url
    request.urlretrieve(url1,file_name)   
#extracting the archive in a folder
    patoolib.extract_archive(file_name,outdir=folder_name)      
    file=os.listdir(folder_name)
#changing curent directory
    os.chdir(folder_name)                                      
#writing data to a varible
    myfile=open(file[0], mode="r")    
    data1=json.load(myfile)
    myfile.close()
#changing the curent directory to the first one
    os.chdir(curent_dir) 
    return data1


 
#widget in which items can be selected
def widget(subjects):
#function for an OK button wich closes the widget
    def Quit():                                     
        global root
        root.destroy()
    def select_all():
        for i in range(0,len(subjects)):
            var[i]=tk.BooleanVar()    
            check=tk.Checkbutton(root,text=subjects[i],variable=var[i],onvalue=1,offvalue=0,pady=3)
            check.grid(row=i+2, column=1, sticky='W')
            check.select()
    global root
    var=[]
    var1=""
    root=tk.Tk()                                    
    root.geometry("400x520+300+250")
    tk.Label(text="Выберите предметы:",padx=10,pady=6).grid(row=0, column=0, sticky="W")
    tk.Checkbutton(root,text="Выбрать все",variable=var1,onvalue=1,offvalue=0, command=select_all).grid(row=1, column=1, sticky="W") 
    for i in range(0,len(subjects)):
        var.append("")
        var[i]=tk.BooleanVar()
        check=tk.Checkbutton(root,text=subjects[i],variable=var[i],onvalue=1,offvalue=0,pady=3)
        check.grid(row=i+2, column=1, sticky='W')
    tk.Button(root, text = 'OK', command=Quit).grid(column=1,pady=10)
    root.mainloop()
    subject=[]
    #list of items for analysis
    for i in range(0,len(subjects)):                       
        if var[i].get()==True:
            subject.append(subjects[i])
    return(subject)


def func2(subject):
    #function that calculates average score and number of paticipants for a particular subject
    def aver_point(subject,data):                                    
        aver=0                                               
        count=0
        for i in range (0,len(data)):
            if data[i]["SubjectName"]==subject:
                count=count+data[i]["PassedQuantity"]
                aver=aver+data[i]["PassedQuantity"]*data[i]["AVGScore"]
        return ([aver/count,count])
    
    data=func1(url)
    points=[]
    num=[]
    mark=[]
#filling in the array with values using the function        
    for i in range(0,len(subject)):                 
        points.append(aver_point(subject[i],data))
# changing the format of data representation
    for i in range(0,len(subject)):                   
        num.append(points[i][1])
        mark.append(points[i][0])
    data_new=pd.DataFrame({"Средний балл":mark, "Число сдававших":num}, index=subject)
    print(data_new)
    return(mark)

  
    
def func3(subject,mark):
#finding values of local maximum and minimum and their indexes  
    loc_min=min(mark)                                        
    ind_min=mark.index(loc_min)
    loc_max=max(mark)
    ind_max=mark.index(loc_max)
#setting the graphic options
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
    
    

subjects=["английский", "биология", "география", "информатика","испанский", 
          "история", "литература", "математика", "немецкий", "обществознание", 
          "русский", "физика", "французский", "химия"]

url='https://op.mos.ru/EHDWSREST/catalog/export/get?id=7080'
subject=widget(subjects)    
func3(subject,func2(subject))
                   
