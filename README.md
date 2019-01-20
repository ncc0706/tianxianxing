# TianXianXing

## 初始化环境

```shell
virtualenv --no-site-packages .venv

cd .venv/Script


set PIPENV_VENV_IN_PROJECT=true

pipenv install 
```

## 安装依赖

```shell

pipenv install flask
pipenv install requests

```

## error

这种错误都是templates文件夹放错位置，应该将此templates文件夹放置在运行程序的文件夹中，就是说templates文件夹和运行文件位于同一级。