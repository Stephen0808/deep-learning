=================================os===============================
import os
 
print( os.path.basename('/root/runoob.txt') )   # 返回文件名runoob.txt
print( os.path.dirname('/root/runoob.txt') )    # 返回目录路径/root
print( os.path.split('/root/runoob.txt') )      # 分割文件名与路径root, runoob.txt
print( os.path.join('root','test','runoob.txt') )  # 将目录和文件名合成一个路径
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
===============================torch==============================

import torch
# 指定device
device = torch.device('cuda' if torch.cuda.is_available else 'cpu')

# 指定训练状态
model.eval()

# 指定模型存放位置
model = model.to(device)
