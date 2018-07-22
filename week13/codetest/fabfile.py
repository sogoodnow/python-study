from fabric.api import *

# 定义环境变量
# 登录用户名

env.user = 'root'
# 多台主机列表
env.hosts = ['192.168.119.148','192.168.119.149','192.168.119.150']

# def hello():
#     # 本地执行
#     local('touch hello')
#     # 远程执行 fab hello -H 192.168.119.148 -u qiuguochang
#     # 会在远程用户的home目录下执行,默认为root用户
#     local('touch hello')
#     put() 传输文件
#     cd() 进入目录
def pack():
    local('cd test && tar -czf ../temp.tar.gz --exclude=dic.bz2 .')

def deploy():
    remote_temp_tar = '/temp/temp/tar.gz'
    run('rm -rf '+remote_temp_tar)
    put('temp.tar.gz',remote_temp_tar)

    with cd():
        run()
    with settings(warn_only=True): #出错只做警告
        run()

