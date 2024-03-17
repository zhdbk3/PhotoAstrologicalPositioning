# 照片测星定位
> 就像每个星星都有自己的位置，每个人也都有自己的轨迹。
> ——ChatGPT瞎编的

## 作者
[MC着火的冰块](https://space.bilibili.com/551409211)

## 使用方法
使用`-h`参数获取帮助
```
$ python pap.py -h
usage: pap.py [-h] {zenith} ...

照片测星定位(Photo Astrological Positioning)

options:
  -h, --help  show this help message and exit

子命令:
  {zenith}
    zenith    天顶位置确定
```

1. **天顶位置确定**
```
$ python pap.py zenith -h
usage: pap.py zenith [-h] [-c COLOUR] image_path
                                                
positional arguments:                           
  image_path            标注好直线的图片的路径  
                                                
options:                                        
  -h, --help            show this help message and exit
  -c COLOUR, --colour COLOUR
                        直线颜色，可选red,green,blue，默认为green
```
首先将照片中指向天顶的直线用红色、绿色或蓝色（推荐绿色）标注出来
然后执行：
```commandline
python pap.py zenith path/to/img -c green
```
输出的坐标记录下来，后面要用
