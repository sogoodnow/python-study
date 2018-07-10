import os ,sys

# 下载源码包

# 判断是否为root用户
if os.getuid()!= 0:
    print('不是root用户，请切换root用户登录')
    sys.exit(1)

# 选择版本号
def_ver = '1.15.1'
ver = input("请输入需要的版本号：(默认版本：{})".format(def_ver))
ver = ver or def_ver

# 安装目录配置 /usr/local/nginx
def_path = ' /usr/local/nginx '
path = input("请输入安装目录：(默认目录：{})".format(def_path))
path = path or path

# 下载源码包
url = "http://nginx.org/download/nginx-{}.tar.gz".format(ver)
file = "nginx-{}.tar.gz".format(ver)
cmd ='wget '+url
# print(cmd)
res = os.system(cmd)
if res !=0: # 等于0则成功
    print('下载出错！')
    sys.exit(1)

# 解压缩
cmd = 'tar -zxf '+ file
if os.system(cmd) !=0:
    print('解压缩错误！')
    sys.exit(1)

# 安装依赖
cmd = 'apt install -y gcc make libpcre3-dev zlib1g-dev openssl libssl-dev'
if os.system(cmd) != 0:
    print('安装依赖失败')
    sys.exit(1)

# 配置
cmd = " cd nginx-{} && ./configure --prefix".format(ver)+ def_path
if os.system(cmd) != 0:
    print('配置失败！')
    sys.exit(1)

# 编译
cmd = " make && make install"
if os.system(cmd) != 0:
    print('编译失败！')
    sys.exit(1)