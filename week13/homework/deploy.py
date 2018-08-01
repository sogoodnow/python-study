import paramiko

"""
服务器环境条件：
ZIP
Psutil
Scrapy : apt-get install build-essential libssl-dev libffi-dev python3-dev
            pip3 install scrapy
Docker
Redis  应用pip命令安装
Scrapy_redis
"""

class Deploy:
    def __init__(self,ip,username,password,port):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

    @classmethod
    def host(cls):
        return cls(
            ip =  "192.168.204.128",
            username = "root",
            password="root",
            port=22,
        )

    def do_deploy(self):
        # 服务器定义
        IP = self.ip
        USER = self.username
        PASSWORD = self.password
        PORT = self.port
        print(IP+"___"+USER+"___"+PASSWORD+"___")
        transport = paramiko.Transport(IP,PORT)
        transport.connect(username=USER,password=PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(transport)
        # 爬虫项目上传

        sftp.put("./W10csdnMS.zip","/root/W10csdnMS.zip")
        sftp.put("./W10csdnS1.zip","/root/W10csdnS1.zip")
        # sftp.listdir()
        sftp.close()
        transport.close()
        # 启动paramiko连接
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname=IP,username=USER,password=PASSWORD,port=PORT)
        # 通过paramokio进行解压
        command = "unzip /root/W10csdnMS.zip && unzip /root/W10csdnS1.zip"
        stdin,stdout,stderr =ssh.exec_command(command)
        print(stdout.read().decode())
        print(stderr.read().decode())
        # 判断是否有redis镜像，没有则安装redis镜像
        command = "docker images|awk '/^redis/ {print $1}'"
        stdin1,stdout1,stderr1 =ssh.exec_command(command)
        if (stdout1.read().decode())=="":
            command = "docker pull redis"
            stdin2, stdout2, stderr2 = ssh.exec_command(command)
            print(stdout2.read().decode())

        # ============运行redis容器==========
        # 1.创建数据挂载目录
        # 2.启动容器映射端口

        # 容器会自动创建挂载目录
        command = "docker run -d --name redis -v /root/redis/data:/data -p 6379:6379 redis"
        stdin3,stdout3,stderr3 =ssh.exec_command(command)
        if stderr3.read().decode():
            print("Docker  Error=====>" +stderr3.read().decode())
        print("Docker OK")

        # 运行爬虫
        # Master
        command = "cd /root/W10csdnMS/Master/spiders && scrapy runspider Mcsnd.py"
        ssh.exec_command(command)
        stdin3,stdout3,stderr3 =ssh.exec_command(command)
        # print(stdout3.read().decode())
        # print(stderr3.read().decode())
        # if stderr3.read().decode()=="":
        #     print("Master爬取========>完成")


        # Slave
        command = "cd /root/W10csdnS1/S1/spiders && scrapy runspider slave_spider.py"
        ssh.exec_command(command)
        # stdin3,stdout3,stderr3 =ssh.exec_command(command)
        # print(stdout3.read().decode())
        # print(stderr3.read().decode())
        # if stderr3.read().decode()=="":
        #     print("Slave爬取========>完成")

        ssh.close()
        return "=========================================Done====================================="