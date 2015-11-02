#!/usr/bin/env python
#coding:utf-8
#Author:liangpeili

#import datetime  # 如果需要同时记录日志时间，则去掉注释
from Tkinter import *
import sys

#history函数主要包含三个动作：1.追加当前输入到文本daily.log; 2.读取历史记录并打印到Label; 3.删除当前文本框的输入。
def history(event):
    f = open("daily.log","a+")
#    now=datetime.datetime.now()   # 这三行用于打印日志时间，可不用
#    curr=now.strftime("%Y-%m-%d %H:%M:%S")
#    f.write(curr+":"+entry.get()+"\n")
    f.write(entry.get()+"\n")
    f.close()
    f = open("daily.log")
    history_log = f.read()
    label.configure(text=history_log)
    f.close()
    entry.delete(0, END)

root = Tk()
root.title("极简记事本")   #设置标题
#root.geometry('300x200')                 #这边可以定义窗口大小及是否可变，不过定义了之后效果并不好
#root.resizable(width=False, height=True)

#修改字符编码，不然Entry无法接收中文输入
reload(sys)
sys.setdefaultencoding('utf-8')
# 设置Entry
entry = Entry(root)
entry.bind("<Return>",history)
entry.pack()

# 设置Label
label = Label(root)
label.pack()

#在第一次打开时读取历史记录
f = open("daily.log")
history_log = f.read()
label.configure(text=history_log)

#设置Button
button = Button(root, text="QUIT", fg="red", command=root.quit)
button.pack(side=LEFT)

root.mainloop()
