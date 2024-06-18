import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk
import os
import re


def choosepic():
    path_ = tkinter.filedialog.askopenfilename()
    path.set(path_)
    print(path)
    print(entry.get())
    return 0


def inferpic():
    return 0


if __name__ == '__main__':
    # 生成tk界面 app即主窗口
    app = tk.Tk()
    # 修改窗口titile
    app.title("显示图片")
    # 设置主窗口的大小和位置
    app.geometry("1200x400+200+200")
    # Entry widget which allows displaying simple text.
    path = tk.StringVar()
    entry = tk.Entry(app, state='readonly', text=path, width=100)
    entry.grid(column=0, row=0)
    # 使用Label显示图片
    lableShowImage = tk.Label(app)
    lableShowImage.grid(column=0, row=1)
    # 选择图片的按钮
    buttonSelImage = tk.Button(app, text='选择图片', command=choosepic)
    buttoninferImage = tk.Button(app, text='检测图片', command=inferpic)
    buttonSelImage.grid(column=0, row=2)
    buttoninferImage.grid(column=1, row=2)
    # buttonSelImage.pack(side=tk.BOTTOM)
    # Call the mainloop of Tk.
    app.mainloop()
