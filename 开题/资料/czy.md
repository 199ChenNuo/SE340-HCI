### 关于Htc Vive


### 关于tilt brush
控件：使用 Tilt Brush 时你第一个注意到的就是控件。控件简单，并且非常丰富。控制器可帮助你自然作画。触发器启动后，将根据控制器的位置和角度保留图画。你可以使用凹形垫调整图画的宽度。

工具箱控制器在控制器周围提供菜单面板。你可以通过轻扫凹形垫来旋转菜单或旋转手中的控制器。例如，你可以选择工具箱控制器调出色轮。选择颜色时，你只需将绘图控制器指向色轮，激光笔会引导你的选择。同样，如果你想选择新的场景、撤销上一笔或远距传动至不同的位置，可以将控制器旋转至这些选项，激光指向相应图标并启动触发器。


**体积素描**： 大部分物体都可分成基本的 3D 形状：球形、方形、圆柱形等等。体积素描的理念是在心目中看到这些 3D 图形，然后在纸上画出相应的 2D 图形。绘制完简单的 3D 图形后，可在 3D 图形周围补充相应的线条和曲线，完成最终的作品。这种技巧可成功应用于 Tilt Brush。建议使用 Mirror 特性。该特性可帮助你专注于绘制脸的一侧，同时计算机会镜像和补充绘制另一侧脸。建议将这种技巧用于技术绘制和体积素描，以此锻炼你的 3D 绘制技巧。最后，生活中的事物都是不对称的，对称非常无聊，因此可将这种不对称视作 3D 绘制训练的终极手段。

### 关于Tilt Brush Unity SDK
Tilt Brush Unity SDK包括以下几个部分：
《Tilt Brush》的初始材质和脚本，将自动绑定到导入的草图，以便在Unity中的效果与在《Tilt Brush》中的草图一致。
《Tilt Brush》的音频响应功能，让画刷响应音乐。
可重用的示例脚本，增加交互或利用导入的草图制作动画。
《Tilt Brush》内容的妙用。

**导入草图**
要在Unity中使用《Tilt Brush》的草图，需要将草图导出为FBX文件并复制到项目中。Tilt Brush SDK会在导入过程中处理文件并指定正确的材质。

导出草图的步骤如下：

打开《Tilt Brush》，加载草图。
单击菜单设置区域的[...]图标。
单击Labs图标。
在弹出对话框中单击Export。

导入草图到Unity场景的步骤如下：

将.FBX文件(Windows：My Documents/Tilt Brush/Exports 或Mac： Documents/Tilt Brush/Exports)复制到Unity项目。
将.FBX文件从项目视图拖至层级视图。

注意：Tilt Brush Unity SDK不会加载.tilt文件；不需要复制FBX包含的纹理贴图到Unity项目。

提示：可以从SDK提供标准的Tilt Brush环境开始学习。Tilt Brush环境位于TiltBrushExamples/Environments/Standard目录下。


[Tilt Brush Unity SDK：在Unity中使用Tilt Brush](http://www.insideria.cn/article/34)