

# 环境

1. Python2 

   (我是python2最新的version)

2. `opencv-contrib-python`

   需要卸载原有的`opencv-python`, 并安装指定版本的`opencv-contrib-python` （否则会有些玄学报错）`

   ```shell
   python2/Scripts> pip install opencv-contrib-python==3.4.2.17
   ```

3. `numpy`, `scipy`

这部分就老生常谈



# 使用

使用`sift`算子提取特征点并展示

```
> test.py
```

输入图片和输出txt文件路径都在代码里写死了。

原图

![](D:\github\SE340-HCI\中期\sift提取模型特征点\m5_0_512x512.png)

结果：

![](D:\github\SE340-HCI\中期\sift提取模型特征点\result.png)

效果有些不大好，可能需要对原图进行处理，避免干扰。