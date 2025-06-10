# Python 命令行项目模板

[模板项目地址](https://github.com/JackyLee3362/py-cli-template)

## 使用模板创建项目

```sh
cookiecutter https://github.com/JackyLee3362/py-cli-template
# 按照步骤填写
cd your-project
```

## 配置环境变量

首先设置环境变量（也可以使用 `.env` 文件）

```sh
# .env 文件
PYTHONPATH="src"
ENV_FOR_DYNACONF="development"

# linux
export PYTHONPATH="src"
export ENV_FOR_DYNACONF="development"

# windows cmd
set PYTHONPATH=src # 使用 echo %var% 查看
set ENV_FOR_DYNACONF=development

# windows powershell
$env:PYTHONPATH="src" # 使用 $env:var 查看
$env:ENV_FOR_DYNACONF="development"
```

## 运行 main.py

```sh
python main.py --help
```

## 打包

```sh
# 直接打包
pyinstaller main.py -p src
# 使用脚本打包
python scripts/package.py
```

## 打包后运行

打包后的文件在 `dist` 中

```sh
cd dist/main
# windows
./main.exe --help
./main.exe hello world
```
