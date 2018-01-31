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

