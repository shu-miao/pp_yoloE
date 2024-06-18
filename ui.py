import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk
# pillow
import os
import re


# 选择并显示图片
def choosepic():
    path_ = tkinter.filedialog.askopenfilename()
    path_pic.set(path_)
    # print(path)
    # print(path_)
    img_open = Image.open(entry_pic.get()).resize((400, 300), Image.ANTIALIAS)
    # print(entry_pic.get())
    # img = ImageTk.PhotoImage(img_open.resize((200,200)))
    img = ImageTk.PhotoImage(img_open)
    lableShowpic.config(image=img)
    lableShowpic.image = img


# D:/PycharmProjects/PaddleDetection/output_inference/new_pdparams
# output_inference/ppyoloe_crn_l_80e_sliced_visdrone_640_025
def inferpic(moder_dir="output_inference/ppyoloe_crn_l_80e_sliced_visdrone_640_025",
             img_file="image_file=NV10-dataset/images/002.jpg",
             output_dir="D:/PycharmProjects/PaddleDetection/newoutput"):
    img_file = str(entry_pic.get())
    os.system(
        f"python deploy/python/infer.py --model_dir={moder_dir} --image_file={img_file} --output_dir={output_dir} --run_mode=paddle --device=gpu")
    # os.system("python deploy/python/infer.py --model_dir=output_inference/ppyoloe_crn_l_80e_sliced_visdrone_640_025 "
    #          "--image_file=NV10-dataset/images/002.jpg --run_mode=paddle --device=gpu")
    # print(img_file)
    a = img_file
    b = []
    while img_file:
        img_file = a
        a = re.findall(r"/(.+?.jpg)", str(img_file))
        # print(a)
        if a == b:
            break
    # print('img_file=',img_file)
    output_file = str(output_dir) + '/' + str(img_file[0])
    # regular = re.findall(r"/(\d+.jpg)", str(img_file))
    # print(regular)
    # output_file = str(output_dir) + '/' + str(regular[0])
    # output_file = r'D:\PycharmProjects\PaddleDetection\newoutput\001.jpg'
    # print('output_file=',output_file)
    path_out.set(output_file)
    img_open = Image.open(output_file).resize((400, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_open)
    lableShowoutpic.config(image=img)
    lableShowoutpic.image = img


if __name__ == '__main__':
    # 生成tk界面 app即主窗口
    app = tk.Tk()
    # 修改窗口titile
    app.title("遥感图像小目标检测")
    # 设置主窗口的大小和位置
    app.geometry("1200x400+200+200")
    # Entry widget which allows displaying simple text.
    path_pic = tk.StringVar()
    path_out = tk.StringVar()
    entry_pic = tk.Entry(app, state='readonly', text=path_pic, width=85)
    entry_pic.grid(column=0, row=0)
    entry_out = tk.Entry(app, state='readonly', text=path_out, width=85)
    entry_out.grid(column=1, row=0)
    # canvas = tk.Canvas(app,bg='white',height=600,width=1200)
    # pic = tk.PhotoImage(file=entry.get())
    # out_pic = tk.PhotoImage(file=entry.get())
    # canvas.grid(column=1,row=1)

    # 使用Label显示图片
    lableShowpic = tk.Label(app)
    lableShowpic.grid(column=0, row=1)
    lableShowoutpic = tk.Label(app)
    lableShowoutpic.grid(column=1, row=1)
    # 选择图片的按钮
    buttonSelImage = tk.Button(app, text='选择图片', command=choosepic)
    buttoninferImage = tk.Button(app, text='检测图片', command=inferpic)
    buttonSelImage.grid(column=0, row=2)
    buttoninferImage.grid(column=1, row=2)
    # buttonSelImage.pack(side=tk.BOTTOM)
    # Call the mainloop of Tk.
    app.mainloop()
