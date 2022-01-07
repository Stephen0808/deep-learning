
=========================str >> list============================
str1 = "12345"
list1 = list(str1)
 
str2 = "123 sjhid dhi"
list2 = str2.split() #or list2 = str2.split(" ")

str3 = "www.google.com"
list3 = str3.split(".")
===========================list >> str==========================
str1 = "".join(list1)

===========================OrderedDict()============================
# 字典值的排序
from collections import OrderedDict

d={}
d['a']='A'
d['b']='B'
d['c']='C'
for k,v in d.items():
    print k,v
 
print '\nOrderedDict:'
d=collections.OrderedDict()
d['a']='A'
d['b']='B'
d['c']='C'

============================glob==================================
# glob是支持linux通配符的文件操作模块
import glob

imagePath = sorted(glob.glob(os.path.join(folder, '*')))
=================================os===============================
import os
 
print( os.path.basename('/root/runoob.txt') )   # 返回文件名runoob.txt
print( os.path.dirname('/root/runoob.txt') )    # 返回目录路径/root
print( os.path.split('/root/runoob.txt') )      # 分割文件名与路径root, runoob.txt
print( os.path.join('root','test','runoob.txt') )  # 将目录和文件名合成一个路径

# 将文件名和拓展名分开
(imgname, imgext) = os.path.splitext(os.path.basename(path))
==============================argparse============================
import argparse

parser = argparse.ArgumentPaser()
parser.add_argument('--model_path', type=str, default='model/sth.pth')

arg = parser.parse_arg()
if os.path.exist(arg.model_path):
    print(f'loading model from {arg.model_path}')
else:
    os.makedirs(os.path.dirname(arg.model_path), exist_ok=True)  # exist_ok 为True时不抛出异常，创建路径
    url = 'https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/{}'.format(os.path.basename(args.model_path))
    r = requests.get(url, allow_redirects=True)
    print(f'downloading model {args.model_path}')
    open(args.model_path, 'wb').write(r.content)
# print("{:=^50s}".format("Split Name"))
================================cv2===============================
import cv2
'''基本描述

    详细描述

    Args:
        path (str): The path of the file to wrap
        field_storage (FileStorage): The :class:`FileStorage` instance to wrap
        temporary (bool): Whether or not to delete the file when the File instance is destructed

    Returns:
        BufferedFileStorage: A buffered writable file descriptor
    '''
img_gt = cv2.imread(path, cv2.IMREAD_COLOR).astype(np.float32) / 255. # 1代表彩色，数值为0-255，通道HCW-BGR

# HWC_BGR转CHW_RGB,np.transpose和切片操作
img_gt_CHW_RGB = np.transpose(img_gt if img_gt.shape[2]==1 else img_gt[:, :, [2, 1, 0]], (2, 0, 1))

# torch中需要batchsize维度
img_gt_CHW_RGB = torch.from_numpy(img_gt_CHW_RGB).float().unsqueeze(0).to(device)

# pad
_, _, h_old, w_old = img_lq.size()
h_pad = (h_old // window_size + 1) * window_size - h_old
w_pad = (w_old // window_size + 1) * window_size - w_old

# flip&cat
img_lq = torch.cat([img_lq, torch.flip(img_lq, [2])], 2)[:, :, :h_old + h_pad, :]
img_lq = torch.cat([img_lq, torch.flip(img_lq, [3])], 3)[:, :, :, :w_old + w_pad]
===============================torch==============================

import torch
# 指定device
device = torch.device('cuda' if torch.cuda.is_available else 'cpu')

# 指定训练状态
model.eval()

# 指定模型存放位置
model = model.to(device)

# 存储模型
torch.save(net.state_dict(), PATH)

# 加载模型
model_dict = model.load_state_dict(torch.load(PATH), strict=True)  # True时要求模型keys全字匹配，False就只提取match的部分
