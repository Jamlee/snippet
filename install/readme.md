# 安装 go 和 node 和 bash 环境

```bash
wget https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -p /data/miniconda3 -b

cat > ~/.condarc <<EOF
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
auto_activate_base: false
EOF


conda create --name snippet python
export CONDA_BUILD=1
conda activate snippet
conda install  nodejs go gcc_linux-64 gxx_linux-64 jupyterlab zeromq make

# node
# sudo apt install python2 
# npm config set python  /usr/bin/python2
cd install/tgz/package; npm pack; mv zeromq-5.3.1.tgz ../; cd -;
cd install/tgz; 
npm install -g jp-kernel-2.0.0.tgz; npm install -g zeromq-5.3.1.tgz; npm install -g ijavascript-5.2.1.tgz; npm install -g jmp-2.0.0.tgz;

# go
export GOPROXY=https://goproxy.io,direct
export PATH=$HOME/go/bin:$PATH
go install github.com/janpfeifer/gonb@latest
gonb --install
go install golang.org/x/tools/cmd/goimports@latest

# bash
pip install bash_kernel&& python -m bash_kernel.install
```


可设置服务开机自动启动。[WSL2支持systemd](https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/)

```
cat > /etc/systemd/system/jupyter.service <<EOF
[Unit]
Description=jupyter
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
User=jam
Group=jam
Type=simple
WorkingDirectory=/data/snippet
ExecStart=/bin/bash -i start.sh
Restart=always
RestartSec=1
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF
systemctl enable jupyter; systemctl daemon-reload; systemctl start jupyter
systemctl status jupyter
```
