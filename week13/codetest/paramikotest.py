"""
paramiko

"""
import paramiko



# 获取客户端对象
ssh = paramiko.SSHClient()

# set_missing_host_key_policy方法，是制定连接远程主机没有本地密钥或HostKeys对象是的策略，有三种策略：
# 1、AutoAddPolicy,自动添加主机名及主机密钥到本地HostKeys对象，并保存，不依赖load_system_host_keys()的配置，即使~/.ssh/known_hosts不存在也不产生影响。
# 2、WarningPolicy,用于记录一个未知的主机密钥的python警告，并接受它，功能上与AutoAddPolicy相似，但未知主机会有告警
# 3、RejectPolicy,自动拒绝不知的主机名和密钥，依赖 load_system_host_keys()的配置
# awk使用正则 free -m|awk '/^Mem/{print $7}'
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='192.168.119.148',username='root',password='root') #不要密码明码,还用ssh
command = "df -h"
stdin ,stdout,stderr = ssh.exec_command(command)
res =stdout.read().decode()
print(res)