# Experimental-platform
## Install

使用pipenv来进行包版本控制，在目录下使用

```shell
$pipenv install
$pipenv shell
```

之后都会在虚拟环境之中进行操作，不会污染主目录

## 思路

### 服务器

服务器作为模型的汇总，将client传输上来的数据进行汇总，与client使用websocket来进行通信，为异步通信

TODO:

- [ ] 服务器退出的时候自动保存模型（这里应该是dashboard那里进行操纵服务器？

### 客户端

客户端都是单核心操作，如果部署到各个主机上应该放开限制（深度模型自身问题？

可以多主机进行尝试训练效果

使用向量化进行计算化简？许多貌似都是使用for循环效率比较低