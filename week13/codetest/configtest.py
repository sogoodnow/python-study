from string import Template
import psutil,os

# 读取模板文件
with open('./nginx.config.tpl') as f:
    res = f.readlines()
    res = ''.join(res)
# 配置模板参数
params = {
    # 替换模板中的$参数
    'worker_processes' : psutil.cpu_count(),
    'server_name': '120.77.242.173', #服务器名称或地址
    'listen': 80 , #监听端口
    'root' : '/webs/myweb' #项目根目录
}
# 替换模板内容
tmp = Template(res).safe_substitute(**params)
# 将替换后的内容写入sites-available
tmp_path = '/etc/nginx/sites-available/nginx.conf.temp'
with open(tmp_path,'w') as f:
    f.write(res)

# 执行服务器命令


Template()