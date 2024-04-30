# 查看conda帮助信息
conda --help  //或者：conda -h

# 查看conda版本
conda --version

# 更新conda
conda update conda
# 降级conda版本
conda install -n base conda==4.6.7

# 升级conda和anaconda
conda update conda

conda update anaconda


# 卸载anaconda
rm -rf anaconda


# conda环境管理：创建、切换、删除等

## 创建conda环境
conda create --name 环境名 包名（多个包名用空格分隔）  
例如：conda create --name my_env python=3.7 numpy pandas scipy

## 活（切换）conda环境
conda activate 环境名  
例如：conda activate base

## 退出当前环境，默认进入上一个使用或的conda中python环境
conda deactivate


## 显示已安装的conda环境
conda info --envs  或者：conda info -e，亦或者conda env list

## 删除指定的conda环境

### 通过环境名删除
conda remove --name 要删除的环境名 --all

### 通过指定环境文件位置删除（这个方法可以删除不同位置的同名环境）
conda remove -p 要删除的环境所在位置 --all  
例如：conda remove -p C:\Users\user_name\.conda\envs\env_name --all


## 复制conda环境
conda create --name 新环境名 --clone 被复制的环境名  
例如：conda create --name base --clone new_base

# 环境软件包的管理：安装、卸载、查看等
查看当前环境中已安装的包
conda list
1
查看指定环境中的Python软件包
conda list --name 环境名
1
显示当前环境中的指定包
conda list 包名
1
conda命令在当前激活环境中安装需要的包
conda install 包名  //例如：conda install numpy
1
定conda环境安装制定版本的包
conda install --name 环境名 要安装的包名=版本号  //注意这里的版本号不是必须的
1
conda命令删除当前环境中安装的包
conda uninstall 包名
1
精确查找当前环境中可以安装的包
conda search --full-name 包的准确名字
1
模糊查找当前环境中可以安装的包
codna search 包的模糊名字
1
conda从requirements.txt文件安装需求包
conda install --file  requirements.txt --yes
1
conda的Python软件包安装源管理
conda的Python软件包安装源设置后会在Windows系统当前用户目录下下面声场一个.condarc文件，可以通过记事本打开。
例如：博主将conda的Python软件包下载源设置成清华大学镜像源后，.condarc文件内容如下：

channels:
  - conda-forge
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: true
1
2
3
4
5
6
7
8
PS：💡那么问题来了，是否可以直接在用户文件夹下面创建.condarc文件，并将相关设置内容复制进去进而达成conda的Python元件包安装源设置呢？💯🉑答案是肯定的，而且很方便！！

查看安装源
conda config --show-sources
1
添加安装源
清华大学
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
1
2
3
4
5
删除镜像源
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
1
设置安装Python软件包时显示镜像源地址
conda config --set show_channel_urls yes
1
使用environment.yml文件导出或者创建conda的Python虚拟环境
导出当前虚拟环境到指定environment.yml文件
conda env export > environment.yml  # 在当前目录下生成环境文件
1
conda env export > "environment.yml文件路径"  # 指定文件路径
1
根据指定environment.yml文件创建conda虚拟环境
conda env create --n 环境名 --f "environment.yml文件路径"
1
使用requirements.txt文件管理conda虚拟环境中的Python软件包
导出虚拟环境中的Python软件包到requirements.txt文件
conda list -e > requirements.txt
1
使用requirements.txt文件安装Python软件包
conda install --yes --file requirements.txt
1
conda指令执行技巧
在指令后输入-y或者--yes可以制动确认指令，避免后期再次输入y确认，例如：
pip create --name demo python=3.8 --yes  # 自动创建python环境demo，并指定python版本为3.8
1
pip install numpy pandas matplotlib -y  # 自动安装numpy、pandas和matplotlib软件包
