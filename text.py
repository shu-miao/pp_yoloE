import os
import re
import time
# 上面2种方法 是python 执行终端/控制台 命令的常见方法
# os.system('python deploy/python/infer.py --model_dir=output_inference/ppyoloe_crn_l_80e_sliced_visdrone_640_025 --image_file=NV10-dataset/images/002.jpg --output_dir=newoutput --run_mode=paddle --device=gpu')
# ping = os.popen('pint www.baidu.com').read().strip()  返回输出结果
# 注：os.system() 执行完成 会关闭 所以当执行后续 命令需要依赖前面的命令时，请将多条命令写到一个 os.system() 内
#python tools/export_model.py -c configs/smalldet/ppyoloe_crn_l_80e_sliced_visdrone_640_025.yml -o weights=output_inference/new_pdparams/ppyoloe_crn_m_80e_wgisd.pdparams
String = r'E:/Google_download/R-C.jpg'
print(String)
# a= re.findall(r"[^b]/(.*?).jpg", String)
# print(a)
a = String
b = []
while String:
    String = str(a)
    a = re.findall(r"/(.+?.jpg)", String)
    print(a)
    if a == b:
        break
print(String)
    #time.sleep(5)

# regular2 = re.findall(r"/(.+?).jpg",str(regular1))
# print(regular2)
# for i in os.listdir(r'D:\PycharmProjects\PaddleDetection\newoutput'):
#     print(i)