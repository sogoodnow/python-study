"""
ssh免密码登录
RSA非对称
ssh-keygen -t rsa  /root/.ssh
ssh-copy-id root@192.168.119.148

apt install ansible
/etc/ansible/ansible.cfg 配置文件
/etc/ansible/hosts      机器列表

在hosts文件中编辑如下：
[web]  分组管理
192.168.119.148
192.168.119.149


ansible all -m raw -a "uptime"
all:所有hosts中的机器
-m raw   raw模块执行原生shell命令
-a:     模块参数"uptime"

其他一些模块需要有python环境
ansible all -m ping

scpript 模块：将脚本传送到远程服务器并执行
command 模块：和raw模块类似，但需要远程有python环境，默认的命令执行模块
ansible all -m command -a "uptime"
ansible all -a "uptime"

copy 模块：将本地的文件拷贝到远程服务器
ansibel all -m copy -a "src=./aaa/txt dest=/home/aaa"

file 模块 ：改变文件的读写执行权限
ansible all -m file -a "path=/tmp/test.sh mode=0755"

shell 模块：执行目标机器上的脚本文件
ansible all -m shell -a "/tmp/test.sh"

fetch 模块：从目标机器下载
ansible all -m fetch -a "src=/var/log/auth.log dest=/root"


"""