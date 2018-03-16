# 用条件对抗式自动编码器进行人脸老化、退龄

该代码是对论文[《用条件对抗式自动编码器进行人脸老化、退龄》](http://web.eecs.utk.edu/~zzhang61/docs/papers/2017_CVPR_Age.pdf)中算法的Tensorflow实现。

<p align="center">
  <img src="demo/method.png" width="500">
</p>


## 环境要求
* Python 3.5
* Scipy
* TensorFlow (r1.0)

## 训练数据集
* FGNET
* [MORPH](https://ebill.uncw.edu/C20231_ustores/web/product_detail.jsp?PRODUCTID=8)
* [CACD](http://bcsiriuschen.github.io/CARC/)
* UTKFace (通过[Github](https://susanqq.github.io/UTKFace/)或者[Wiki](http://aicip.eecs.utk.edu/wiki/UTKFace)访问)

## 准备训练数据集
你可以使用任何带年龄标签和性别标签的数据集。在该demo中，我们使用了UTKFace数据集。用这种[对齐并裁剪过的人脸照片](https://drive.google.com/file/d/0BxYys69jI14kYVM3aVhKS1VhRUk/view?usp=sharing)更好一些。需要先将UTKFace.tar.gz数据集文件保存并展开到data目录下。

## 训练
```
$ python main.py
```

训练过程在NVIDIA TITAN X (12GB)上进行了测试。在UTKFace数据集(23708张128x128x3大小的图像) 上进行50次epoch的训练时间大约是两个半小时。

在训练过程中，会建立一个新目录`save`，包括四个子目录：`summary`, `samples`, `test` 和 `checkpoint`.

* `samples` 保存每个epoch之后重建的人脸。
* `test` 保存每个epoch之后的测试结果（基于输入人脸生成的不同年龄的人脸）。
* `checkpoint` 保存模型。
* `summary` 保存batch-wise losses和中间输出。

用以下命令来可视化summary, 
```
$ cd save/summary
$ tensorboard --logdir .
```

训练之后，可以在 `samples` 和 `test` 目录中看到重建和测试效果。下图展示了重建（左）和测试（右）的结果。重建结果（左）的第一行是测试样例，他们分别对应的测试结果（右）由上到下按年龄增长顺序排列。

<p align="center">
  <img src="demo/sample.png" width="400">  <img src="demo/test.png" width="400">
</p>

重建损失和epoch的关系见下图, 为了可视化的目的我们对它进行了低通滤波。原始记录保存在`summary`目录中。

<p align="center">
  <img src="demo/loss_epoch.jpg" width="600">
</p>




## 测试
```
$ python main.py --is_train False --testdir your_image_dir
```
输入命令之后，应该显示出下面的信息。

```
  	Building graph ...

	Testing Mode

	Loading pre-trained model ...
	SUCCESS ^_^

	Done! Results are saved as save/test/test_as_xxx.png
```

具体来说，测试人脸会进行两次处理，这两次分别将其视作男性和女性。因此，保存的文件会分别命名为`test_as_male.png`（作为男性测试） 和 `test_as_female.png`（作为女性测试）。如果想实现更好的结果，需要在更大并更多样化的数据集上进行训练。

## 训练过程演示

第一行显示了输入的不同年龄的人脸，其他行显示了每次epoch优化之后输出的人脸。输出的人脸由上到下按年龄递增顺序排列。

<p align="center">
  <img src="demo/demo_train.gif" width="800">
</p>

## 文件说明
* [`FaceAging.py`](FaceAging.py) 建立并初始化模型的类，实现训练和测试的相关功能。
* [`ops.py`](ops.py) 提供函数由 `FaceAging.py` 文件调用，实现卷积，反卷积，全卷积，leaky ReLU激活函数，下载并保存图像等操作。
* [`main.py`](main.py) 用于演示 `FaceAging.py`的功能。
    
## 引用
Zhifei Zhang, Yang Song, and Hairong Qi. "Age Progression/Regression by Conditional Adversarial Autoencoder." *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017.
```
@inproceedings{zhang2017age,
  title={Age Progression/Regression by Conditional Adversarial Autoencoder},
  author={Zhang, Zhifei and Song, Yang and Qi, Hairong},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2017}
}
```
[Spotlight 演讲](https://youtu.be/425rPG580dQ)
