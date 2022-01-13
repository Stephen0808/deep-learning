### How to run the docker
+ You should access the docker container first
```
docker run --gpus all --rm -it airsplay/bottom-up-attention bash
docker run --gpus all -v /home/ysd21/lxmert/data/gopro_imgfeat/gopro_all_sharp:/workspace/images:ro -v /home/ysd21/lxmert/data/gopro_imgfeat:/workspace/features --rm -it airsplay/bottom-up-attention bash
```
+ Access the features directory and execute the extract file in different split.
```
cd /workspace/features
CUDA_VISIBLE_DEVICES=0 python extract_nlvr2_image.py --split train
CUDA_VISIBLE_DEVICES=0 python extract_nlvr2_image.py --split valid
CUDA_VISIBLE_DEVICES=0 python extract_nlvr2_image.py --split test
```
